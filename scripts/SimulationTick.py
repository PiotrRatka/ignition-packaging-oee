logger = system.util.getLogger("PackagingLine")

parentPath = "[default]PackagingLine_1"
tagPaths = [
    parentPath + "/State", 
    parentPath + "/ActualSpeed", 
    parentPath + "/SelectedRecipeID", 
    parentPath + "/PartialPcs"
]
vals = system.tag.readBlocking(tagPaths)

rawState = vals[0].value
rawSpeed = vals[1].value
rawRecipe = vals[2].value
rawPartial = vals[3].value

logger.info("TICK -> State: %s | Speed: %s | RecipeID: %s" % (str(rawState), str(rawSpeed), str(rawRecipe)))

state = int(rawState) if rawState is not None else 0
actualSpeed = float(rawSpeed) if rawSpeed is not None else 0.0
recipeId = int(rawRecipe) if rawRecipe is not None else 1
partial = float(rawPartial) if rawPartial is not None else 0.0

if state == 1:
    producedThisSec = (actualSpeed / 60.0) + partial
    wholePcs = int(producedThisSec)
    newPartial = producedThisSec - wholePcs

    targetGoodTag = "%s/GoodRecipe%d" % (parentPath, recipeId)
    targetRejectTag = "%s/RejectRecipe%d" % (parentPath, recipeId)
    
    counts = system.tag.readBlocking([targetGoodTag, targetRejectTag])
    good = int(counts[0].value) if counts[0].value is not None else 0
    reject = int(counts[1].value) if counts[1].value is not None else 0

    good += wholePcs

    if wholePcs > 0 and (good % 40) < wholePcs:
        reject += 1

    system.tag.writeBlocking(
        [targetGoodTag, targetRejectTag, parentPath + "/PartialPcs"],
        [good, reject, newPartial]
    )