IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Recipes]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[Recipes](
        [RecipeID] [int] IDENTITY(1,1) NOT NULL,
        [RecipeName] [varchar](50) NOT NULL,
        [TargetSpeed] [int] NOT NULL,
        [RejectLimit] [float] NOT NULL,
        CONSTRAINT [PK_Recipes] PRIMARY KEY CLUSTERED ([RecipeID] ASC)
    );
END
GO

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DowntimeLog]') AND type in (N'U'))
BEGIN
    CREATE TABLE [dbo].[DowntimeLog](
        [EventID] [int] IDENTITY(1,1) NOT NULL,
        [StartTime] [datetime2](0) NOT NULL DEFAULT (sysutcdatetime()),
        [ReasonCode] [nvarchar](50) NOT NULL,
        [DurationSec] [int] NOT NULL,
        CONSTRAINT [PK_DowntimeLog] PRIMARY KEY CLUSTERED ([EventID] ASC)
    );
END
GO

SET IDENTITY_INSERT [dbo].[Recipes] ON;
GO

MERGE INTO [dbo].[Recipes] AS Target
USING (VALUES
    (1, 'Format_Standard_500g', 120, 5.0),
    (2, 'Format_Family_1000g', 85, 3.0),
    (3, 'Format_Eco_250g', 160, 4.0)
) AS Source (RecipeID, RecipeName, TargetSpeed, RejectLimit)
ON Target.RecipeID = Source.RecipeID
WHEN MATCHED THEN
    UPDATE SET 
        Target.RecipeName = Source.RecipeName,
        Target.TargetSpeed = Source.TargetSpeed,
        Target.RejectLimit = Source.RejectLimit
WHEN NOT MATCHED THEN
    INSERT (RecipeID, RecipeName, TargetSpeed, RejectLimit)
    VALUES (Source.RecipeID, Source.RecipeName, Source.TargetSpeed, Source.RejectLimit);
GO

SET IDENTITY_INSERT [dbo].[Recipes] OFF;
GO