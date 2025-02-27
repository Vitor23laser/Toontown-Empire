from panda3d.core import *

QuietZone = 1
UberZone = 2
WallBitmask = BitMask32(1)
FloorBitmask = BitMask32(2)
CameraBitmask = BitMask32(4)
CameraTransparentBitmask = BitMask32(8)
SafetyNetBitmask = BitMask32(512)
SafetyGateBitmask = BitMask32(1024)
GhostBitmask = BitMask32(2048)
PathFindingBitmask = BitMask32.bit(29)
PickerBitmask = BitMask32(4096)
DefaultCameraFov = 52.0
MaxCameraFov = 120.0
DefaultCameraFar = 800.0
DefaultCameraNear = 1.0
AICollisionPriority = 10
AICollMovePriority = 8
MaxFriends = 200
MaxBackCatalog = 48
MaxCustomMessages = 25
SPInvalid = 0
SPHidden = 1
SPRender = 2
SPDynamic = 5
CENormal = 0
CEBigHead = 1
CESmallHead = 2
CEBigLegs = 3
CESmallLegs = 4
CEBigToon = 5
CESmallToon = 6
CEFlatPortrait = 7
CEFlatProfile = 8
CETransparent = 9
CENoColor = 10
CEInvisible = 11
CEPumpkin = 12
CEBigWhite = 13
CESnowMan = 14
CEGreenToon = 15
CETinyToon = 16
CEGiantToon = 17
CEGhost = 'g'
CEName2Id = {
 'normal': CENormal,
 'bighead': CEBigHead,
 'smallhead': CESmallHead,
 'biglegs': CEBigLegs,
 'smalllegs': CESmallLegs,
 'bigtoon': CEBigToon,
 'smalltoon': CESmallToon,
 'flatportrait': CEFlatPortrait,
 'flatprofile': CEFlatProfile,
 'transparent': CETransparent,
 'nocolor': CENoColor,
 'invisible': CEInvisible,
 'pumpkin': CEPumpkin,
 'bigwhite': CEBigWhite,
 'snowman': CESnowMan,
 'greentoon': CEGreenToon,
 'tinytoon': CETinyToon,
 'gianttoon': CEGiantToon
}
GiantToonScale = 2.3
BigToonScale = 1.5
SmallToonScale = 0.5
TinyToonScale = 0.3
GhostEffectName2Id = {
    'none': 3,
    'fade': 4,
    'poof': 5
}
DisconnectNone = 0
DisconnectBookExit = 1
DisconnectCloseWindow = 2
DisconnectPythonError = 3
DisconnectSwitchShards = 4
DisconnectGraphicsError = 5
DatabaseDialogTimeout = 50.0
DatabaseGiveupTimeout = 45.0
WalkCutOff = 0.5
RunCutOff = 8.0
FloorOffset = 0.025
AvatarDefaultRadius = 1
InterfaceFont = None
InterfaceFontPath = None
SignFont = None
SignFontPath = None
ChalkFont = None
ChalkFontPath = None
NametagFonts = {}
NametagFontPaths = {}
DialogClass = None
GlobalDialogClass = None

def getInterfaceFont():
    global InterfaceFontPath
    global InterfaceFont
    if InterfaceFont == None:
        if InterfaceFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
        else:
            InterfaceFont = loader.loadFont(InterfaceFontPath, lineHeight=1.0)
    return InterfaceFont

def setInterfaceFont(path):
    global InterfaceFontPath
    global InterfaceFont
    InterfaceFontPath = path
    InterfaceFont = None

def getSignFont():
    global SignFont
    global SignFontPath
    if SignFont == None:
        if SignFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
            SignFont = TextNode.getDefaultFont()
        else:
            SignFont = loader.loadFont(SignFontPath, lineHeight=1.0)
    return SignFont

def setSignFont(path):
    global SignFontPath
    SignFontPath = path

def getChalkFont():
    global ChalkFontPath
    global ChalkFont
    if ChalkFont == None:
        if ChalkFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
            ChalkFont = TextNode.getDefaultFont()
        else:
            ChalkFont = loader.loadFont(ChalkFontPath, lineHeight=1.0)
    return ChalkFont

def setChalkFont(path):
    global ChalkFontPath
    ChalkFontPath = path

def getNametagFont(index):
    global NametagFontPaths
    global NametagFonts
    if (index not in NametagFonts) or (NametagFonts[index] is None):
        if (index not in NametagFontPaths) or (NametagFontPaths[index] is None):
            InterfaceFont = TextNode.getDefaultFont()
            NametagFonts[index] = TextNode.getDefaultFont()
        else:
            NametagFonts[index] = loader.loadFont(NametagFontPaths[index], lineHeight=1.0)
    return NametagFonts[index]

def setNametagFont(index, path):
    NametagFontPaths[index] = path

def getDialogClass():
    global DialogClass
    if DialogClass == None:
        from otp.otpgui.OTPDialog import OTPDialog
        DialogClass = OTPDialog
    return DialogClass

def getGlobalDialogClass():
    global GlobalDialogClass
    if DialogClass == None:
        from otp.otpgui.OTPDialog import GlobalDialog
        GlobalDialogClass = GlobalDialog
    return GlobalDialogClass

def setDialogClasses(dialogClass, globalDialogClass):
    global DialogClass
    global GlobalDialogClass
    DialogClass = dialogClass
    GlobalDialogClass = globalDialogClass

NetworkLatency = 1.0
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
STRAFE_LEFT_INDEX = 4
STRAFE_RIGHT_INDEX = 5
ToonStandableGround = 0.707
ToonSpeedFactor = 1.25
ToonForwardSpeed = 16.0 * ToonSpeedFactor
ToonJumpForce = 24.0
ToonReverseSpeed = 8.0 * ToonSpeedFactor
ToonRotateSpeed = 80.0 * ToonSpeedFactor
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
ThinkPosHotkey = 'shift-f1'
PlaceMarkerHotkey = 'f2'
FriendsListHotkey = 'f7'
StickerBookHotkey = 'f8'
OptionsPageHotkey = 'escape'
ScreenshotHotkey = 'f9'
QuestsHotkeyOn = 'end'
QuestsHotkeyOff = 'end-up'
InventoryHotkeyOn = 'home'
InventoryHotkeyOff = 'home-up'
MapHotkeyOn = 'delete'
MapHotkeyOff = 'delete-up'
QuitGameHotKeyOSX = 'meta-q'
QuitGameHotKeyRepeatOSX = 'meta-q-repeat'
HideGameHotKeyOSX = 'meta-h'
HideGameHotKeyRepeatOSX = 'meta-h-repeat'
MinimizeGameHotKeyOSX = 'meta-m'
MinimizeGameHotKeyRepeatOSX = 'meta-m-repeat'
GlobalDialogColor = (1, 1, 0.75, 1)
DefaultBackgroundColor = (0.3, 0.3, 0.3, 1)
toonBodyScales = {
 'mouse': 0.6,
 'cat': 0.73,
 'duck': 0.66,
 'rabbit': 0.74,
 'horse': 0.85,
 'dog': 0.85,
 'monkey': 0.68,
 'bear': 0.85,
 'pig': 0.77
}
toonHeadScales = {
 'mouse': Point3(1.0),
 'cat': Point3(1.0),
 'duck': Point3(1.0),
 'rabbit': Point3(1.0),
 'horse': Point3(1.0),
 'dog': Point3(1.0),
 'monkey': Point3(1.0),
 'bear': Point3(1.0),
 'pig': Point3(1.0)
}
legHeightDict = {
 's': 1.5,
 'm': 2.0,
 'l': 2.75
}
torsoHeightDict = {
 's': 1.5,
 'm': 1.75,
 'l': 2.25,
 'ss': 1.5,
 'ms': 1.75,
 'ls': 2.25,
 'sd': 1.5,
 'md': 1.75,
 'ld': 2.25
}
headHeightDict = {
 'dls': 0.75,
 'dss': 0.5,
 'dsl': 0.5,
 'dll': 0.75,
 'cls': 0.75,
 'css': 0.5,
 'csl': 0.5,
 'cll': 0.75,
 'hls': 0.75,
 'hss': 0.5,
 'hsl': 0.5,
 'hll': 0.75,
 'mls': 0.75,
 'mss': 0.5,
 'rls': 0.75,
 'rss': 0.5,
 'rsl': 0.5,
 'rll': 0.75,
 'fls': 0.75,
 'fss': 0.5,
 'fsl': 0.5,
 'fll': 0.75,
 'pls': 0.75,
 'pss': 0.5,
 'psl': 0.5,
 'pll': 0.75,
 'bls': 0.75,
 'bss': 0.5,
 'bsl': 0.5,
 'bll': 0.75,
 'sls': 0.75,
 'sss': 0.5,
 'ssl': 0.5,
 'sll': 0.75
}
RandomButton = 'Randomize'
TypeANameButton = 'Type Name'
PickANameButton = 'Pick-A-Name'
NameShopSubmitButton = 'Submit'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names\nmust be approved\nby the Toon Council.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'

TeleportFailCooldown = 2.0