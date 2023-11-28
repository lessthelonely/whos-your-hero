import requests
from bs4 import BeautifulSoup

def get_trope_description(url):
    url_start = "https://tvtropes.org"
    url_trope = "https://tvtropes.org/pmwiki/pmwiki.php/Main/"

    if url == "Catchphrase":
        full_url = url_trope + "CharacterCatchphrase" #catchphrase is under construction so we have this special case
    elif url == "NoGoodDeed":
        full_url = url_trope + "NoGoodDeedGoesUnpunished" #NoGoodDeed is under construction so we have this special case
    else:
        full_url = url_trope + url
    page = requests.get(full_url)
    soup = BeautifulSoup(page.content, "lxml")
    find_text = soup.find("h2").find_all_previous("p")
    # reorder the list
    find_text.reverse()
    find_text = find_text[4:]

    text = ""
    for t in find_text:
        # Extract the text within the paragraph (p) tag
        paragraph_text = t.text

        # Find the anchor (a) tag within the HTML
        link_tag = t.find('a')

        if link_tag is None:
            text += paragraph_text
            continue

        # Extract the text within the anchor tag
        link_text = link_tag.text

        # Extract the link (href) attribute
        link = url_start + link_tag['href']

        # Create the formatted text by replacing the link within square brackets
        formatted_text = paragraph_text.replace(link_text, f"{link_text} [\"{link}\"]")
        text += formatted_text

        with open("tropes/" + url + ".txt", "w", encoding="utf-8") as f:
            f.write(text)


# read the tropes from the file
# All original tropes - all_tropes_clean.txt
# New tropes due to Cyclops - new_tropes.txt
tropes_url = []
with open("new_tropes.txt", "r", encoding="utf-8") as f:
    tropes_url = f.readlines()
    tropes_url = [t.strip() for t in tropes_url]

for t in tropes_url:
    print(t)
    get_trope_description(t)

#PopCulturedBadass - page different 
# see what the hell is up with this -> StepfordSnarker; StatuesqueStunner, UselessAccessory, WillTheyorWontThey, ElementalMotifs

# Letsfaceit, ActionHero, NeckLiftNeckSnap, TheRivalShadowArchetype, ArtisticLicense–Physics, BroughtToYouByTheLetterX, Dandere, MessiahCreepDarkMessiah



"""
TallDarkandSnarky
TheLostLenore
PrimaryColorChampion
SunglassesatNight
TheStoic
Hunk
DisappearedDad
PowerIncontinence
SuperHero
TheChessmaster
PoweroftheSun
BarbarianLongHair
DisabilitySuperpower
UnluckyEverydude
AsskickingLeadstoLeadership
SayMyName
JerkassHasaPoint
BeingGoodSucks
BoringbutPractical
HeroInsurance
TheOathBreaker
LoveInterest
BroughtDowntoBadass
BlindWithoutThem
SuperWeight
SchoolyardBullyAllGrownUp
BlindWeaponMaster
StatusQuoIsGod
IDidWhatIHadtoDo
TheGlassesComeOff
NervesofSteel
AwesomebyAnalysis
HazyFeelTurn
HeWhoFightsMonsters
WhatBeautifulEyes
TheDreaded
UnknownRelative
MoreHerothanThou
CoolShades
BigGood
HeartbrokenBadass
CallBack
BigDamnHeroes
ContrivedCoincidence
TrueLoveIsBoring
WillfullyWeak
TheExtremistWasRight
YouWouldntHitaGuywithGlasses
ControlFreak
RelativeError
BlindfoldedVision
ShirtlessScene
WhattheHellHero
TheHero
FourStarBadass
TheLawofPowerProportionatetoEffort
InhumanEyeConcealers
GoodIsNotNice
DeadAllAlong
BigNO
PoorCommunicationKills
PromotiontoParent
PhlebotinumBattery
InterdimensionalTravelDevice
GlowingEyesofDoom
UtopiaJustifiestheMeans
RealMenWearPink
CasualDangerDialogue
FictionIsntFair
FathertoHisMen
AllGirlsWantBadBoys
OneWayVisor
ExtradimensionalPowerSource
GodzillaThreshold
BadassFamily
NobleMaleRoguishMale
CannotSpitItOut
InterruptedCooldownHug
TheSmartGuy
TallDarkandHandsome
ClothesMaketheSuperman
ConflictBall
EmbarrassingNickname
TraumaCongaLine
TheChainsofCommanding
OhCrap
PersonofMassDestruction
WhenHeSmiles
StilltheLeader
SoldierVersusWarrior
Cyclops
ChildSoldiers
GenreBlindness
DissonantSerenity
TheLeader
HeroesWantRedheads
MundaneUtility
EnergyAbsorption
GlassCannon
ShrinkingViolet
BlondeBrunetteRedhead
IronicNickname
HeelRealisation
MindLinkMates
DelayedRippleEffect
BlownAcrosstheRoom
StrongFamilyResemblance
SinglePowerSuperheroes
FightsLikeaNormal
EyeBeams
IAmNotLeftHanded
YouRemindMeofX
TheCaptain
VillainessesWantHeroes
PinballProjectile
PureEnergy
TheStrategist
BatmanGrabsaGun
CurbStompBattle
GreyandGrayMorality
FutureMeScaresMe
DoomMagnet
TokenGoodTeammate
WhyDidYouMakeMeHitYou
HerowithBadPublicity
StandardizedLeader
LuckilyMyPowersWillProtectMe
KnightinSourArmor
UnscrupulousHero
CaptainPatriotic
DeconstructedCharacterArchetype
AlternateUniverseReedRichardsIsAwesome
DarkMessiah
TangledFamilyTree
HorribleJudgeofCharacter
RedEyesTakeWarning
ContainmentClothing
TheSpock
TotalitarianUtilitarian
PyrrhicVictory
PowerLimiter
InSpiteofaNail
ColorBlindConfusion
DidYouJustScamCthulhu
TragicHero
"""