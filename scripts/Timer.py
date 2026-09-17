	parentPath = "[default]PackagingLine_1"
	
	tagPaths = [
	    parentPath + "/State", 
	    parentPath + "/ActualSpeed", 
	    parentPath + "/SelectedRecipeID", 
	    parentPath + "/PartialPcs"
	]
	vals = system.tag.readBlocking(tagPaths)
	
	state = int(vals[0].value) if vals[0].value is not None else 0
	actualSpeed = float(vals[1].value) if vals[1].value is not None else 0.0
	recipeId = int(vals[2].value) if vals[2].value is not None else 1
	partial = float(vals[3].value) if vals[3].value is not None else 0.0
	
	if state == 1 and recipeId in [1, 2, 3]:
	    producedThisSec = (actualSpeed / 60.0) + partial
	    wholePcs = int(producedThisSec)
	    newPartial = producedThisSec - wholePcs
	
	    if wholePcs > 0:
	        targetGoodTag = "%s/GoodRecipe%d" % (parentPath, recipeId)
	        targetRejectTag = "%s/RejectRecipe%d" % (parentPath, recipeId)
	        
	        counts = system.tag.readBlocking([targetGoodTag, targetRejectTag])
	        good = int(counts[0].value) if counts[0].value is not None else 0
	        reject = int(counts[1].value) if counts[1].value is not None else 0
	
	        good += wholePcs
	
	        if (good % 40) < wholePcs:
	            reject += 1
	
	        system.tag.writeBlocking(
	            [targetGoodTag, targetRejectTag, parentPath + "/PartialPcs"],
	            [good, reject, newPartial]
	        )
	    else:
	        system.tag.writeBlocking([parentPath + "/PartialPcs"], [newPartial])