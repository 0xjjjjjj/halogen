# Demon Stone Prototype: Snowblind Engine Source Map

## Overview

**Source:** Forgotten Realms: Demon Stone (Jun 15, 2004 prototype), SLUS_208.04
**Developer:** Stormfront Studios (licensed Snowblind Engine from Snowblind Studios)
**Compiler:** Metrowerks CodeWarrior R5900 (PS2)
**Internal codename:** Phoenix

- **618 source file paths** recovered from .debug section (9.3MB Metrowerks debug info)
- **7326 functions** in .symtab (7305 unique)
- **6133 data objects** in .symtab
- **605 C++ classes** identified from name mangling

## How This Relates to Champions of Norrath

Demon Stone uses the same Snowblind Engine as CoN, but Stormfront used `Cl` prefix
instead of Snowblind's `VI` prefix. The engine layer is structurally identical:

| CoN (Snowblind) | Demon Stone (Stormfront) | Module |
|---|---|---|
| VIRaster | ClGfx / ClGfxDmaBuffer | Rendering / DMA |
| VIScene / VIZone | ClWorld / ClWorldDrawData | World / BSP |
| VIParticle | ClPfxSystem / ClParticleObj | Particles |
| VIColorBuffer / VIPointLight | ClDynamicLightManager | Dynamic per-vertex lighting |
| VISoundDevice | ClAudio / ClAudioData | Audio / SPU2 |
| VIHSprite / VICSprite | ClNoamActor / ClNoamSkeleton | Skeletal animation |
| VICollide | ClCollisionManager / ClCollisionAttrib | Collision |
| VIWorld | ClWorld / ClWorldWater / ClWorldStreamingManager | Terrain / streaming |
| VIWnd | ClMenu / ClShell / ClUI* | UI system |
| AMX/Pawn VM | ClScript | Scripting |
| VILoader | ClWad | Asset loading |
| VIAtmosphere | ClRain / ClWind / ClCloud / ClSkyBox | Weather / atmosphere |

Key: "Noam" = Stormfront's animation system codename (= VIHSprite/VICSprite)

## Engine Source Tree

```
Engine/
  ClEngine.cpp
  ClEnginePS2.cpp
Engine/Actor/
  ClActor.cpp
  ClActor.h
  ClNoamActor.cpp
  ClNoamActor.h
Engine/AlphaSort/
  ClAlphaSortRendererPs2.cpp
Engine/Assets/
  ClAsset.h
  ClAssetMap.cpp
  ClCinematicAsset.cpp
  ClFontAsset.h
  ClIconAssetPs2.h
  ClNavAsset.cpp
  ClObxAsset.cpp
  ClPropAsset.h
  ClRtaAsset.cpp
  ClSubtitleAsset.cpp
  ClTextureAssetPs2.h
Engine/Bard/
  ClBard.cpp
  ClBardCubicCurve.cpp
  ClBardInterface.cpp
  ClBrx.cpp
  ClBrxActorControl.cpp
  ClBrxInterpolator.cpp
Engine/Camera/
  ClCamera.cpp
Engine/Cloth/
  ClCloth.cpp
Engine/Collision/
  ClBoundingInfo.cpp
Engine/Decal/
  ClDecal.cpp
Engine/GameConfig/
  ClGameConfig.cpp
Engine/GfxEffects/
  ClExpandingProp.cpp
  ClFogPS2.cpp
  ClFullScreenShimmer.cpp
  ClHeatHaze.cpp
  ClLightning.cpp
  ClMagicalAttackTrail.cpp
  ClMotionBlur.cpp
  ClPortalRipple.cpp
  ClProcTexture.cpp
  ClSoftFocus.cpp
  ClTeamAttack.cpp
  ClWeaponTrail.cpp
  ClWizardShield.cpp
Engine/Light/
  ClDynamicLightManager.cpp
  ClDynamicLightRendererPS2.cpp
  ClEngineLight.cpp
  ClLightGlow.cpp
Engine/Msg/
  ClMsg.cpp
Engine/Noam/
  ClAnimBin.cpp
  ClAnimStream.cpp
  ClNoamFigure.cpp
  ClNoamFigurePs2.cpp
  ClNoamPs2UcodeInterface.cpp
  ClNoamSkeleton.cpp
Engine/Noam/Mixer/
  ClInterpolator.cpp
  ClMixer.cpp
  ClMixerInput.h
  ClMixerInputHeadTrack.cpp
  ClMixerInputKeyframe.cpp
  ClMixerInputLipLock.cpp
Engine/Noam/Morpher/
  ClMorpher.cpp
Engine/Objects/
  ClAttributeManager.cpp
  ClAttributeManager.h
  ClAttributeObj.cpp
  ClAttributeObj.h
  ClCollisionAttrib.cpp
  ClDrawAttrib.cpp
  ClExplodeAttrib.cpp
  ClExplodeAttribManager.cpp
  ClObject.cpp
  ClPhysicsAttrib.cpp
  ClRTTI.cpp
  ClScriptObj.cpp
  ClScriptObj.h
  ClTickAttrib.cpp
Engine/Particle/
  ClBillboardParticleRendererPs2.cpp
  ClFirePatternRendererPs2.cpp
  ClPfxMachineFuncs.cpp
  ClPfxMachinePs2.cpp
  ClPfxPattern.cpp
  ClPfxSystem.cpp
  ClTrailParticleRendererPs2.cpp
Engine/Physics/
  ClRigidBody.cpp
Engine/Prop/
  ClProp.cpp
  ClPropDrawDataPs2.cpp
  ClPropInstance.cpp
  ClPropRendererPS2.cpp
Engine/Rta/
  ClRta.cpp
  ClRtaRtxOpCallback.cpp
  ClRtaSequence.cpp
  ClRtx.cpp
Engine/Script/
  ClNativeMethod.h
  ClObjHeader.cpp
  ClScript.cpp
  ClScriptLink.cpp
  ClStringTableHeader.cpp
  ClVTableHeader.cpp
Engine/Services/
  ClDelayService.h
  ClFadeService.cpp
  ClLoadBankService.cpp
  ClMotionService.cpp
  ClScriptLinkService.cpp
  ClServiceManager.cpp
  ClSoundService.cpp
  ClTimerEventService.h
Engine/Shader/
  ClRenderFuncPS2.cpp
  ClShaderConfigPS2.cpp
  ClShaderSystem.cpp
  ClShaderTextureManager.cpp
Engine/Simulation/
  ClCharacterSimulation.cpp
  ClCharacterSimulation.h
  ClConstraintList.cpp
  ClConstraintManager.cpp
  ClControlPoint.cpp
  ClControlPointPool.cpp
  ClFlagSimulation.cpp
  ClForceManager.cpp
  ClGenericSimulation.cpp
  ClGenericSimulation.h
  ClMeshSimulation.cpp
  ClMeshSimulation.h
  ClSimulationBase.cpp
  ClSimulationBase.h
  ClSimulationManager.cpp
  ClSimulationRenderer.cpp
  ClTapestrySimulation.cpp
Engine/Simulation/Constraints/
  ClBoneAttachmentConstraint.cpp
  ClCollisionConstraint.cpp
  ClConstraintInstance.cpp
  ClConstraintInstance.h
  ClConstraintSphere.cpp
  ClControlPointAttachmentConstraint.cpp
  ClParallelSegmentConstraint.cpp
  ClSegmentLengthConstraint.cpp
  ClStaticAttachmentConstraint.cpp
Engine/Sky/
  ClCloud.cpp
  ClSkyBoxPS2.cpp
Engine/UI/
  ClControlPs2.cpp
  ClFont.cpp
  ClFontType.cpp
  ClMenu.cpp
  ClObx.cpp
  ClOdometer.cpp
  ClTexture.cpp
  ClUnicode.cpp
Engine/Wad/
  ClWad.cpp
Engine/Weather/
  ClRain.cpp
  ClWind.cpp
Engine/Wind/
  ClWindManager.cpp
Engine/World/
  ClCameraList.cpp
  ClCollisionMaterial.cpp
  ClCollisionTriangle.cpp
  ClGrass.cpp
  ClHangingEdgeData.cpp
  ClLava.cpp
  ClNodeObjectList.cpp
  ClPortalDrawManager.cpp
  ClUcodeInterface.cpp
  ClWorld.cpp
  ClWorldBillboard.cpp
  ClWorldCollisionDataPs2.cpp
  ClWorldCollisionNode.cpp
  ClWorldDrawDataPs2.cpp
  ClWorldNode.cpp
  ClWorldPlant.cpp
  ClWorldStreamingManager.cpp
  ClWorldWater.cpp
Engine/Wrappers/
  SfSoundWrappers.cpp
  SfWorldWrappers.cpp
```

## Machine (PS2 Hardware Abstraction) Source Tree

```
Machine/
  ClMachinePs2.cpp
Machine/Audio/
  ClAudioPs2.cpp
Machine/Clock/
  ClClockPs2.cpp
  ClTimeOfDayPs2.cpp
Machine/Configuration/
  ClConfiguration.cpp
  ClVersion.cpp
Machine/Console/
  ClConsolePs2.cpp
Machine/Dev/
  ClDev.cpp
  ClDevConfiguration.cpp
  ClDevConsolePs2.cpp
  ClDevFontPs2.cpp
  ClLinkedList.cpp
  ClParser.cpp
  ClParser.h
  ClPerfBars.cpp
Machine/FMV/
  ClFMVDeux.cpp
  ClFMVDeuxDecode.cpp
  ClFMVDeuxGraphics.cpp
  ClFMVDeuxMPEGBuffer.cpp
Machine/File/
  ClFilePs2.cpp
Machine/Graphics/
  ClDisplayPs2.cpp
  ClDraw2DPs2.cpp
  ClDrawPrimPS2.cpp
  ClFader.cpp
  ClGSDisplayList.cpp
  ClScreenShot.cpp
  ClViewport.cpp
Machine/IO/
  ClAbIDeviceMgr.cpp
  ClDeviceMgrPS2.cpp
  ClDeviceMgrPS2.h
Machine/Memory/
  ClMemory.cpp
  ClStackedMemory.h
Machine/PS2/DMA/
  ClDmaBuffer.cpp
  ClGfxDmaBuffer.cpp
  ClGfxDmaBuffer.h
  ClScratchpadDMA.cpp
  ClVif0DmaBuffer.cpp
  ClVif0DmaBuffer.h
Machine/PS2/Graphics/
  ClGfx.cpp
  ClPbi.cpp
  ClPixelFormats.cpp
  ClRegList.cpp
  ClTexEnv.cpp
Machine/PS2/InterruptHandlers/
  ClGsIntHandler.cpp
  ClTimer1IntHandler.cpp
  ClVBlankIntHandler.cpp
  ClVif1IntHandler.cpp
Machine/PS2/ResourceManagers/
  ClGfxManager.cpp
  ClVU0Manager.cpp
  ClVU1Manager.cpp
Machine/PS2/System/
  ClExceptions.cpp
  ClIop.cpp
  ClPerfCounters.cpp
Machine/Pad/
  ClAbIInputDevice.cpp
  ClDevicePs2GamePad.cpp
  ClDevicePs2GamePad.h
  ClInputRecorder.cpp
  ClRumbleManager.cpp
Machine/SaveLoad/
  ClSaveDevicePs2.cpp
  ClSaveLoad.cpp
Phoenix/StateMachine/
  ClBoolExpData.cpp
  ClInputs.cpp
  ClStateData.cpp
  ClStateMachine.cpp
  ClStateMachineData.cpp
```

## Game-Specific Source Tree (Demon Stone)

```
Machine/PS2/System/
  ClExceptions.cpp
  ClIop.cpp
  ClPerfCounters.cpp
Math/
  ClCrc.cpp
  ClFrustum.cpp
  ClMathUtil.cpp
  ClMatrix.h
  ClMatrix_ps2.cpp
  ClQuaternion_ps2.cpp
  ClVector3d.h
  ClVector3dPacked.cpp
  ClVector4d.h
  SfMathFunc.cpp
  SfMathFunc_ps2.cpp
Phoenix/
  ClGame.cpp
  SfMainProjectPs2.cpp
Phoenix/AI/
  ClAI.cpp
  ClAIObj.cpp
  ClAction.cpp
  ClAction.h
  ClActionStateMachine.cpp
  ClActionStateMachine.h
  ClActionStateMachineData.cpp
  ClActionUtils.cpp
  ClAdjTable.cpp
  ClBehavior.cpp
  ClBehaviorStackMachine.cpp
  ClNavManager.cpp
  ClNavMesh.cpp
  ClNavTable.cpp
  ClObjectiveObj.cpp
  ClTarget.cpp
  ClTargetMeList.cpp
  ClTargetObj.cpp
  ClTargetting.cpp
  ClTriTable.cpp
Phoenix/AI/Actions/
  ClActionAttack.cpp
  ClActionBlockReact.cpp
  ClActionCastSpell.cpp
  ClActionCliff.cpp
  ClActionControl.cpp
  ClActionDead.cpp
  ClActionDying.cpp
  ClActionFaceMithril.cpp
  ClActionFaceObjective.cpp
  ClActionFaceTarget.cpp
  ClActionFall.cpp
  ClActionFallOffLadder.cpp
  ClActionHoldDragon.cpp
  ClActionJump.cpp
  ClActionJumpAttack.cpp
  ClActionJumpOntoDragon.cpp
  ClActionKillmove.cpp
  ClActionLand.cpp
  ClActionLink.cpp
  ClActionNavHealth.cpp
  ClActionNavMithril.cpp
  ClActionNavObjective.cpp
  ClActionNavShadow.cpp
  ClActionNavTarget.cpp
  ClActionNavTether.cpp
  ClActionPlayAnim.cpp
  ClActionRogueSuper.cpp
  ClActionShoot.cpp
  ClActionSneakAttack.cpp
  ClActionStopSpell.cpp
  ClActionTakeHit.cpp
  ClActionTeamAttack.cpp
  ClActionUserLoco.cpp
  ClActionZoo.cpp
Phoenix/AI/Behaviors/
  ClBehaviorAltCom.cpp
  ClBehaviorCombat.cpp
  ClBehaviorControlled.cpp
  ClBehaviorController.cpp
  ClBehaviorFollow.cpp
  ClBehaviorGetHealth.cpp
  ClBehaviorGetMithril.cpp
  ClBehaviorLoiter.cpp
  ClBehaviorMinigame.cpp
  ClBehaviorObjective.cpp
  ClBehaviorPlayerControl.cpp
  ClBehaviorSeekShadow.cpp
  ClBehaviorSleep.cpp
  ClBehaviorTeamAttack.cpp
  ClBehaviorTeamSuper.cpp
  ClBehaviorZoo.cpp
Phoenix/AI/Encounter/
  ClEncounter.cpp
Phoenix/DB/
  ClAttackDB.cpp
  ClAttackRecord.cpp
  ClAudioHookDB.cpp
  ClAudioHookRecord.cpp
  ClConfigDB.cpp
  ClConfigRecord.cpp
  ClDB.cpp
  ClDefendDB.cpp
  ClDefendRecord.cpp
  ClDifficultyDB.cpp
  ClDifficultyRecord.cpp
  ClEncounterDB.cpp
  ClEncounterRecord.cpp
  ClEnemyDB.cpp
  ClEnemyRecord.cpp
  ClExperienceDB.cpp
  ClExperienceRecord.cpp
  ClFlameDB.cpp
  ClFlameRecord.cpp
  ClItemDB.cpp
  ClItemRecord.cpp
  ClLevelDB.cpp
  ClLevelRecord.cpp
  ClLinkedAnimDB.cpp
  ClLinkedAnimRecord.cpp
  ClLootDB.cpp
  ClLootRecord.cpp
  ClPickupDB.cpp
  ClPickupRecord.cpp
  ClProjectileDB.cpp
  ClProjectileRecord.cpp
  ClPropDB.cpp
  ClSimulationDB.cpp
  ClSimulationRecord.cpp
  ClSkillDB.cpp
  ClSkillRecord.cpp
  ClSpellDB.cpp
  ClSpellRecord.cpp
  ClSuperMeterDB.cpp
  ClSuperMeterRecord.cpp
  ClWeaponDB.cpp
  ClWeaponRecord.cpp
Phoenix/GameAssets/
  ClActionMachineAsset.cpp
  ClBehaviorMachineAsset.cpp
Phoenix/GameAttribs/
  ClCollisionManager.cpp
  ClDebugDrawManager.cpp
  ClDrawManager.cpp
  ClEncounterManager.cpp
  ClFrameInitManager.cpp
  ClPhysicsManager.cpp
  ClTargetAttrib.cpp
  ClTargetAttrib.h
  ClTargetManager.cpp
  ClTickManager.cpp
  ClTriggerAttrib.cpp
  ClTriggerManager.cpp
Phoenix/GameCamera/
  ClBSpline.cpp
  ClCameraMgr.cpp
  ClCameraPath.cpp
  ClCameraPlane.cpp
  ClCameraTransition.cpp
  ClCameraUtils.cpp
  ClConstraintFunctions.cpp
  ClGameCamera.cpp
Phoenix/GameCamera/Effects/
  ClCameraEffects.cpp
  ClDollyZoomEffect.cpp
  ClShakeEffect.cpp
  ClZoomEffect.cpp
Phoenix/GameCamera/Modules/
  ClBardModule.cpp
  ClBardModule.h
  ClBossModule.cpp
  ClBossModule.h
  ClCameraModule.h
  ClDebugModule.cpp
  ClDebugModule.h
  ClDonutModule.cpp
  ClDonutModule.h
  ClDoubleTreadModule.cpp
  ClDoubleTreadModule.h
  ClFollowModule.cpp
  ClFollowModule.h
  ClLookAtModule.cpp
  ClLookAtModule.h
  ClPathModule.cpp
  ClPathModule.h
  ClPlaneBossModule.cpp
  ClPlaneBossModule.h
  ClPlaneModule.cpp
  ClPlaneModule.h
  ClPrisonModule.cpp
  ClPrisonModule.h
  ClReverseTreadModule.cpp
  ClReverseTreadModule.h
  ClTreadModule.cpp
  ClTreadModule.h
Phoenix/GameConfig/
  ClBardInterfaceProject.cpp
  ClGameConfigProject.cpp
  ClGameState.cpp
  ClLevelState.cpp
  ClPlayerState.cpp
  ClSaveDataProject.cpp
Phoenix/GameDebug/
  ClStatCapture.cpp
Phoenix/GameEffects/
  ClGameEffects.cpp
  ClSilverSwordEffect.cpp
  ClTeamAttackEffect.cpp
Phoenix/GameObjs/
  ClBarrierObj.cpp
  ClBoatObj.cpp
  ClBoatObj.h
  ClCameraObj.cpp
  ClCinematicObj.cpp
  ClClothSimObj.cpp
  ClCombatStatus.cpp
  ClExplosionManager.cpp
  ClExplosionObj.cpp
  ClInstancedCharacterManager.cpp
  ClInstancedCharacterManager.h
  ClInstancedCharacterObj.cpp
  ClMineObj.cpp
  ClMithrilFlameObj.cpp
  ClObjectStats.h
  ClParticleManager.cpp
  ClParticleObj.cpp
  ClParticlePlacementObj.cpp
  ClPhysicsRegionObj.cpp
  ClPickupManager.cpp
  ClPickupObj.cpp
  ClPlayers.cpp
  ClRogueShadowObj.cpp
  ClSimMeshObj.cpp
  ClSimulationObj.cpp
  ClSpawnerObj.cpp
  ClStrikableScriptObj.cpp
  ClStruckByHistory.cpp
  ClTeleportTargetObj.cpp
  ClWeaponManager.cpp
  ClWeaponObj.cpp
  ClWickObj.cpp
Phoenix/GameObjs/Character/
  ClArmorPieceObj.cpp
  ClBodyPartObj.cpp
  ClBodyPartObj.h
  ClCharacterManager.cpp
  ClCharacterObj.cpp
  ClCharacterObj.h
  ClCharacterStats.cpp
  ClHeldProjectileObj.cpp
  ClPerceptions.cpp
  ClPlayerObj.cpp
  ClPlayerObj.h
  ClSteering.cpp
  ClUICharacterObj.cpp
  ClUICharacterObj.h
  ClUserInput.cpp
Phoenix/GameObjs/Character/Enemies/
  ClBugbearChieftainObj.cpp
  ClCedarFightGithyankiGeneralObj.cpp
  ClCedarFightSlaadLordObj.cpp
  ClMegaSpiderCaveObj.cpp
  ClMerrshaulkObj.cpp
  ClMerrshaulkObj.h
  ClOrcKingObj.cpp
  ClOrcKingObj.h
  ClRedDragonObj.cpp
  ClRedDragonObj.h
  ClSlaadLordObj.cpp
  ClTrollKingObj.cpp
  ClTrollObj.cpp
Phoenix/GameObjs/Character/NPCs/
  ClDrizztObj.cpp
  ClIronGolemObj.cpp
Phoenix/GameObjs/Character/Players/
  ClRogueObj.cpp
  ClSorcererObj.cpp
  ClWarriorObj.cpp
Phoenix/GameObjs/Projectile/
  ClEndOverProjectile.cpp
  ClPointPredictProjectile.cpp
  ClPointProjectile.cpp
  ClPointProjectile.h
  ClPointSeekerProjectile.cpp
  ClProjectileManager.cpp
  ClProjectileObj.cpp
  ClShaftProjectile.cpp
  ClShaftProjectile.h
  ClSplineProjectile.cpp
  ClSurgeProjectile.cpp
Phoenix/GameObjs/Prop/
  ClAnimPropObj.cpp
  ClNoamPropObj.cpp
  ClPropObj.cpp
  ClPropObj.h
  ClPropPiece.cpp
  ClPropPieceManager.cpp
  ClPropStats.h
  ClStaticPropObj.cpp
  ClWorldPropObj.cpp
Phoenix/GameObjs/Spell/
  ClEnchantSpell.cpp
  ClEnchantSpell.h
  ClLightningSpell.cpp
  ClLightningSpell.h
  ClMagicMissileSpell.cpp
  ClMagicMissileSpell.h
  ClMeteorShowerSpell.cpp
  ClMeteorShowerSpell.h
  ClProtectSpell.cpp
  ClProtectSpell.h
  ClShieldSpell.cpp
  ClShieldSpell.h
  ClSpellManager.cpp
  ClSpellObj.cpp
  SfSpellTypes.cpp
Phoenix/GameRta/
  ClGameRta.cpp
Phoenix/GameServices/
  ClColorPulseService.cpp
  ClEffectService.cpp
  ClEffectService.h
  ClShellServices.cpp
  ClSimulationServices.cpp
  ClUtilServices.cpp
Phoenix/GameUI/
  ClGameConsole.cpp
  ClGameUI.cpp
  ClMessageBox.cpp
  ClOptionsDialogBox.cpp
  ClPlayerHUD.cpp
  ClShell.cpp
  ClStrings.cpp
  ClTrainingHUD.cpp
  ClVoiceOver.cpp
Phoenix/GameUI/ShellMode/
  ClShellMode.cpp
  ClShellMode.h
  ClShellModeAutoBuy.cpp
  ClShellModeAutoBuy.h
  ClShellModeController.cpp
  ClShellModeController.h
  ClShellModeCredits.cpp
  ClShellModeCredits.h
  ClShellModeHUD.cpp
  ClShellModeHUD.h
  ClShellModeLevelEnd.cpp
  ClShellModeLevelEnd.h
  ClShellModeLevelEquipment.cpp
  ClShellModeLevelEquipment.h
  ClShellModeLevelSelect.cpp
  ClShellModeLevelSelect.h
  ClShellModeLevelUp.cpp
  ClShellModeLevelUp.h
  ClShellModeLoadGame.cpp
  ClShellModeLoadGame.h
  ClShellModeMainMenu.cpp
  ClShellModeMainMenu.h
  ClShellModeNewGame.cpp
  ClShellModeNewGame.h
  ClShellModeOptions.cpp
  ClShellModeOptions.h
  ClShellModeSaveGame.cpp
  ClShellModeSaveGame.h
  ClShellModeShow.cpp
  ClShellModeShow.h
  ClShellModeUpgrade.cpp
  ClShellModeUpgrade.h
Phoenix/GameUI/UIParts/
  ClHighlightColor.cpp
  ClImage.cpp
  ClShellBackgroundCloud.cpp
  ClShellForgroundgroup.cpp
  ClText.cpp
  ClText.h
  ClTransitTimer.cpp
  ClUIButtonList.cpp
  ClUIButtonText.cpp
  ClUIElement2d.cpp
  ClUIImage.cpp
  ClUIListing.cpp
  ClUIScrollBar.cpp
  ClUISkillList.cpp
  ClUIText.cpp
  ClUIToggleItem.cpp
Phoenix/Level/
  ClLevel.cpp
Phoenix/MiniGames/
  ClLockPickGameObj.cpp
  ClMiniGameManager.cpp
Phoenix/Mode/
  ClGameMode.cpp
  ClGameMode.h
  ClGameModeBoot.cpp
  ClGameModeBoot.h
  ClGameModeInitialize.cpp
  ClGameModeInitialize.h
  ClGameModePlay.cpp
  ClGameModePlay.h
  ClGameModeShell.cpp
  ClGameModeShell.h
Phoenix/Repository/
  ClAssetRepository.cpp
  ClObjFactory.cpp
  ClObjRepository.cpp
  ClServiceFactory.cpp
  SfCreationCallbacks.cpp
Phoenix/ScriptWrappers/
  SfCameraWrappers.cpp
  SfCharacterWrappers.cpp
  SfDeviceMethods.cpp
  SfEffectsWrappers.cpp
  SfLogicWrappers.cpp
  SfMiscWrappers.cpp
  SfRegObjectMethods.cpp
  SfSimulationWrappers.cpp
  SfTimeMethods.cpp
  SfTriggerWrappers.cpp
  SfUtilWrappers.cpp
  SfWeaponWrappers.cpp
Phoenix/StateMachine/
  ClBoolExpData.cpp
  ClInputs.cpp
  ClStateData.cpp
  ClStateMachine.cpp
  ClStateMachineData.cpp
Sys/
  SfDebugPs2.cpp
  crt0.s
```

## Engine Classes (by method count)

| Class | Methods | Likely CoN Equivalent |
|---|---|---|
| ClCharacterObj | 181 | Creature / Player |
| Cl | 166 |  |
| ClNoamActor | 87 | VIHSprite (skeletal) |
| ClEncounterData | 72 | spawn/encounter system |
| ClWorld | 71 | VIZone / VIWorld |
| ClMenu | 70 | VIWnd |
| ClAudioData | 62 | VISoundDevice data |
| ClPlayerObj | 61 | Player |
| ClScript | 58 | AMX/Pawn VM |
| ClAudio | 56 | VISoundDevice |
| ClDevicePs2GamePad | 55 | pad input |
| ClWorldWater | 47 | VIWorld water |
| ClPlayers | 46 | player management |
| ClShell | 45 | game shell/menu |
| ClGameConfigProject | 44 |  |
| ClPropObj | 43 | VICollide props |
| ClGfx | 41 | VIRaster |
| ClWorldPropObj | 41 | world props |
| ClRedDragonObj | 40 | (game-specific) |
| ClNoamSkeleton | 39 | VIHSprite skeleton |
| ClPlayerState | 38 |  |
| ClGfxDmaBuffer | 38 | VIRaster DMA |
| ClNoam | 37 | animation core |
| ClGameUI | 36 | VIWnd UI |
| ClBardInterfaceProject | 36 |  |
| ClShellModeLevelEquipment | 34 |  |
| ClShellModeLevelUp | 34 |  |
| ClLevelState | 34 |  |
| ClMatrix | 34 | math/matrix |
| ClShellModeUpgrade | 33 |  |
| ClGameModePlay | 33 |  |
| ClDeviceMgrPS2 | 33 |  |
| ClGameCamera | 32 | camera system |
| ClShellModeAutoBuy | 31 |  |
| ClWeaponObj | 31 |  |
| ClSimulationObj | 31 | physics sim |
| ClRogueObj | 31 |  |
| ClAction | 30 |  |
| ClTexEnv | 30 | VIRaster texture env |
| ClProjectileObj | 29 |  |
| ClDraw2D | 29 | 2D rendering |
| ClNoamPs2UcodeInterface | 27 | VU1 microcode interface |
| ClBard | 27 |  |
| ClStaticPropObj | 26 |  |
| ClAnimPropObj | 26 |  |
| ClCollisionAttrib | 26 |  |
| ClGameState | 25 |  |
| ClLevel | 25 |  |
| ClVif0DmaBuffer | 24 |  |
| ClStatCapture | 24 |  |
| ClAnimBin | 23 |  |
| ClRigidBody | 23 |  |
| ClTargetting | 23 |  |
| ClDynamicLightManager | 23 | VIColorBuffer / VIPointLight |
| ClPbi | 23 |  |
| ClCamera | 23 |  |
| ClAttributeObj | 22 |  |
| ClUcodeInterface | 22 |  |
| ClGameRta | 21 |  |
| ClPlaneModule | 21 |  |

## All Source Paths

Total: 618 files

- `C:\Projects\Phoenix\Game\Engine\Actor\ClActor.cpp`
- `C:\Projects\Phoenix\Game\Engine\Actor\ClActor.h`
- `C:\Projects\Phoenix\Game\Engine\Actor\ClNoamActor.cpp`
- `C:\Projects\Phoenix\Game\Engine\Actor\ClNoamActor.h`
- `C:\Projects\Phoenix\Game\Engine\AlphaSort\ClAlphaSortRendererPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClAsset.h`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClAssetMap.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClCinematicAsset.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClFontAsset.h`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClIconAssetPs2.h`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClNavAsset.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClObxAsset.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClPropAsset.h`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClRtaAsset.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClSubtitleAsset.cpp`
- `C:\Projects\Phoenix\Game\Engine\Assets\ClTextureAssetPs2.h`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBard.cpp`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBardCubicCurve.cpp`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBardInterface.cpp`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBrx.cpp`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBrxActorControl.cpp`
- `C:\Projects\Phoenix\Game\Engine\Bard\ClBrxInterpolator.cpp`
- `C:\Projects\Phoenix\Game\Engine\Camera\ClCamera.cpp`
- `C:\Projects\Phoenix\Game\Engine\ClEngine.cpp`
- `C:\Projects\Phoenix\Game\Engine\ClEnginePS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Cloth\ClCloth.cpp`
- `C:\Projects\Phoenix\Game\Engine\Collision\ClBoundingInfo.cpp`
- `C:\Projects\Phoenix\Game\Engine\Decal\ClDecal.cpp`
- `C:\Projects\Phoenix\Game\Engine\GameConfig\ClGameConfig.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClExpandingProp.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClFogPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClFullScreenShimmer.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClHeatHaze.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClLightning.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClMagicalAttackTrail.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClMotionBlur.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClPortalRipple.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClProcTexture.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClSoftFocus.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClTeamAttack.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClWeaponTrail.cpp`
- `C:\Projects\Phoenix\Game\Engine\GfxEffects\ClWizardShield.cpp`
- `C:\Projects\Phoenix\Game\Engine\Light\ClDynamicLightManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Light\ClDynamicLightRendererPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Light\ClEngineLight.cpp`
- `C:\Projects\Phoenix\Game\Engine\Light\ClLightGlow.cpp`
- `C:\Projects\Phoenix\Game\Engine\Msg\ClMsg.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClAnimBin.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClAnimStream.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClNoamFigure.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClNoamFigurePs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClNoamPs2UcodeInterface.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\ClNoamSkeleton.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClInterpolator.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClMixer.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClMixerInput.h`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClMixerInputHeadTrack.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClMixerInputKeyframe.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Mixer\ClMixerInputLipLock.cpp`
- `C:\Projects\Phoenix\Game\Engine\Noam\Morpher\ClMorpher.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClAttributeManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClAttributeManager.h`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClAttributeObj.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClAttributeObj.h`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClCollisionAttrib.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClDrawAttrib.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClExplodeAttrib.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClExplodeAttribManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClObject.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClPhysicsAttrib.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClRTTI.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClScriptObj.cpp`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClScriptObj.h`
- `C:\Projects\Phoenix\Game\Engine\Objects\ClTickAttrib.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClBillboardParticleRendererPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClFirePatternRendererPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClPfxMachineFuncs.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClPfxMachinePs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClPfxPattern.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClPfxSystem.cpp`
- `C:\Projects\Phoenix\Game\Engine\Particle\ClTrailParticleRendererPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Physics\ClRigidBody.cpp`
- `C:\Projects\Phoenix\Game\Engine\Prop\ClProp.cpp`
- `C:\Projects\Phoenix\Game\Engine\Prop\ClPropDrawDataPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Prop\ClPropInstance.cpp`
- `C:\Projects\Phoenix\Game\Engine\Prop\ClPropRendererPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Rta\ClRta.cpp`
- `C:\Projects\Phoenix\Game\Engine\Rta\ClRtaRtxOpCallback.cpp`
- `C:\Projects\Phoenix\Game\Engine\Rta\ClRtaSequence.cpp`
- `C:\Projects\Phoenix\Game\Engine\Rta\ClRtx.cpp`
- `C:\Projects\Phoenix\Game\Engine\Script\ClNativeMethod.h`
- `C:\Projects\Phoenix\Game\Engine\Script\ClObjHeader.cpp`
- `C:\Projects\Phoenix\Game\Engine\Script\ClScript.cpp`
- `C:\Projects\Phoenix\Game\Engine\Script\ClScriptLink.cpp`
- `C:\Projects\Phoenix\Game\Engine\Script\ClStringTableHeader.cpp`
- `C:\Projects\Phoenix\Game\Engine\Script\ClVTableHeader.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClDelayService.h`
- `C:\Projects\Phoenix\Game\Engine\Services\ClFadeService.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClLoadBankService.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClMotionService.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClScriptLinkService.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClServiceManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClSoundService.cpp`
- `C:\Projects\Phoenix\Game\Engine\Services\ClTimerEventService.h`
- `C:\Projects\Phoenix\Game\Engine\Shader\ClRenderFuncPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Shader\ClShaderConfigPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\Shader\ClShaderSystem.cpp`
- `C:\Projects\Phoenix\Game\Engine\Shader\ClShaderTextureManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClCharacterSimulation.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClCharacterSimulation.h`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClConstraintList.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClConstraintManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClControlPoint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClControlPointPool.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClFlagSimulation.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClForceManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClGenericSimulation.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClGenericSimulation.h`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClMeshSimulation.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClMeshSimulation.h`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClSimulationBase.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClSimulationBase.h`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClSimulationManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClSimulationRenderer.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\ClTapestrySimulation.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClBoneAttachmentConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClCollisionConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClConstraintInstance.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClConstraintInstance.h`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClConstraintSphere.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClControlPointAttachmentConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClParallelSegmentConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClSegmentLengthConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Simulation\Constraints\ClStaticAttachmentConstraint.cpp`
- `C:\Projects\Phoenix\Game\Engine\Sky\ClCloud.cpp`
- `C:\Projects\Phoenix\Game\Engine\Sky\ClSkyBoxPS2.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClControlPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClFont.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClFontType.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClMenu.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClObx.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClOdometer.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClTexture.cpp`
- `C:\Projects\Phoenix\Game\Engine\UI\ClUnicode.cpp`
- `C:\Projects\Phoenix\Game\Engine\Wad\ClWad.cpp`
- `C:\Projects\Phoenix\Game\Engine\Weather\ClRain.cpp`
- `C:\Projects\Phoenix\Game\Engine\Weather\ClWind.cpp`
- `C:\Projects\Phoenix\Game\Engine\Wind\ClWindManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClCameraList.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClCollisionMaterial.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClCollisionTriangle.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClGrass.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClHangingEdgeData.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClLava.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClNodeObjectList.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClPortalDrawManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClUcodeInterface.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorld.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldBillboard.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldCollisionDataPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldCollisionNode.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldDrawDataPs2.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldNode.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldPlant.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldStreamingManager.cpp`
- `C:\Projects\Phoenix\Game\Engine\World\ClWorldWater.cpp`
- `C:\Projects\Phoenix\Game\Engine\Wrappers\SfSoundWrappers.cpp`
- `C:\Projects\Phoenix\Game\Engine\Wrappers\SfWorldWrappers.cpp`
- `C:\Projects\Phoenix\Game\Machine\Audio\ClAudioPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\ClMachinePs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Clock\ClClockPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Clock\ClTimeOfDayPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Configuration\ClConfiguration.cpp`
- `C:\Projects\Phoenix\Game\Machine\Configuration\ClVersion.cpp`
- `C:\Projects\Phoenix\Game\Machine\Console\ClConsolePs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClDev.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClDevConfiguration.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClDevConsolePs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClDevFontPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClLinkedList.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClParser.cpp`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClParser.h`
- `C:\Projects\Phoenix\Game\Machine\Dev\ClPerfBars.cpp`
- `C:\Projects\Phoenix\Game\Machine\FMV\ClFMVDeux.cpp`
- `C:\Projects\Phoenix\Game\Machine\FMV\ClFMVDeuxDecode.cpp`
- `C:\Projects\Phoenix\Game\Machine\FMV\ClFMVDeuxGraphics.cpp`
- `C:\Projects\Phoenix\Game\Machine\FMV\ClFMVDeuxMPEGBuffer.cpp`
- `C:\Projects\Phoenix\Game\Machine\File\ClFilePs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClDisplayPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClDraw2DPs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClDrawPrimPS2.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClFader.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClGSDisplayList.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClScreenShot.cpp`
- `C:\Projects\Phoenix\Game\Machine\Graphics\ClViewport.cpp`
- `C:\Projects\Phoenix\Game\Machine\IO\ClAbIDeviceMgr.cpp`
- `C:\Projects\Phoenix\Game\Machine\IO\ClDeviceMgrPS2.cpp`
- `C:\Projects\Phoenix\Game\Machine\IO\ClDeviceMgrPS2.h`
- `C:\Projects\Phoenix\Game\Machine\Memory\ClMemory.cpp`
- `C:\Projects\Phoenix\Game\Machine\Memory\ClStackedMemory.h`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClDmaBuffer.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClGfxDmaBuffer.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClGfxDmaBuffer.h`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClScratchpadDMA.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClVif0DmaBuffer.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\DMA\ClVif0DmaBuffer.h`
- `C:\Projects\Phoenix\Game\Machine\PS2\Graphics\ClGfx.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\Graphics\ClPbi.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\Graphics\ClPixelFormats.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\Graphics\ClRegList.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\Graphics\ClTexEnv.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\InterruptHandlers\ClGsIntHandler.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\InterruptHandlers\ClTimer1IntHandler.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\InterruptHandlers\ClVBlankIntHandler.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\InterruptHandlers\ClVif1IntHandler.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\ResourceManagers\ClGfxManager.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\ResourceManagers\ClVU0Manager.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\ResourceManagers\ClVU1Manager.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\System\ClExceptions.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\System\ClIop.cpp`
- `C:\Projects\Phoenix\Game\Machine\PS2\System\ClPerfCounters.cpp`
- `C:\Projects\Phoenix\Game\Machine\Pad\ClAbIInputDevice.cpp`
- `C:\Projects\Phoenix\Game\Machine\Pad\ClDevicePs2GamePad.cpp`
- `C:\Projects\Phoenix\Game\Machine\Pad\ClDevicePs2GamePad.h`
- `C:\Projects\Phoenix\Game\Machine\Pad\ClInputRecorder.cpp`
- `C:\Projects\Phoenix\Game\Machine\Pad\ClRumbleManager.cpp`
- `C:\Projects\Phoenix\Game\Machine\SaveLoad\ClSaveDevicePs2.cpp`
- `C:\Projects\Phoenix\Game\Machine\SaveLoad\ClSaveLoad.cpp`
- `C:\Projects\Phoenix\Game\Math\ClCrc.cpp`
- `C:\Projects\Phoenix\Game\Math\ClFrustum.cpp`
- `C:\Projects\Phoenix\Game\Math\ClMathUtil.cpp`
- `C:\Projects\Phoenix\Game\Math\ClMatrix.h`
- `C:\Projects\Phoenix\Game\Math\ClMatrix_ps2.cpp`
- `C:\Projects\Phoenix\Game\Math\ClQuaternion_ps2.cpp`
- `C:\Projects\Phoenix\Game\Math\ClVector3d.h`
- `C:\Projects\Phoenix\Game\Math\ClVector3dPacked.cpp`
- `C:\Projects\Phoenix\Game\Math\ClVector4d.h`
- `C:\Projects\Phoenix\Game\Math\SfMathFunc.cpp`
- `C:\Projects\Phoenix\Game\Math\SfMathFunc_ps2.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionAttack.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionBlockReact.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionCastSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionCliff.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionControl.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionDead.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionDying.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionFaceMithril.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionFaceObjective.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionFaceTarget.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionFall.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionFallOffLadder.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionHoldDragon.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionJump.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionJumpAttack.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionJumpOntoDragon.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionKillmove.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionLand.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionLink.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavHealth.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavMithril.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavObjective.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavShadow.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavTarget.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionNavTether.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionPlayAnim.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionRogueSuper.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionShoot.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionSneakAttack.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionStopSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionTakeHit.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionTeamAttack.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionUserLoco.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Actions\ClActionZoo.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorAltCom.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorCombat.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorControlled.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorController.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorFollow.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorGetHealth.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorGetMithril.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorLoiter.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorMinigame.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorObjective.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorPlayerControl.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorSeekShadow.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorSleep.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorTeamAttack.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorTeamSuper.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Behaviors\ClBehaviorZoo.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClAI.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClAIObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClAction.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClAction.h`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClActionStateMachine.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClActionStateMachine.h`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClActionStateMachineData.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClActionUtils.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClAdjTable.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClBehavior.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClBehaviorStackMachine.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClNavManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClNavMesh.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClNavTable.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClObjectiveObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClTarget.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClTargetMeList.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClTargetObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClTargetting.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\ClTriTable.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\AI\Encounter\ClEncounter.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ClGame.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClAttackDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClAttackRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClAudioHookDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClAudioHookRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClConfigDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClConfigRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClDefendDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClDefendRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClDifficultyDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClDifficultyRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClEncounterDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClEncounterRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClEnemyDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClEnemyRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClExperienceDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClExperienceRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClFlameDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClFlameRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClItemDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClItemRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLevelDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLevelRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLinkedAnimDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLinkedAnimRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLootDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClLootRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClPickupDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClPickupRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClProjectileDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClProjectileRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClPropDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSimulationDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSimulationRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSkillDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSkillRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSpellDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSpellRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSuperMeterDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClSuperMeterRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClWeaponDB.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\DB\ClWeaponRecord.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAssets\ClActionMachineAsset.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAssets\ClBehaviorMachineAsset.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClCollisionManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClDebugDrawManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClDrawManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClEncounterManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClFrameInitManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClPhysicsManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTargetAttrib.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTargetAttrib.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTargetManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTickManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTriggerAttrib.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameAttribs\ClTriggerManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClBSpline.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClCameraMgr.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClCameraPath.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClCameraPlane.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClCameraTransition.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClCameraUtils.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClConstraintFunctions.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\ClGameCamera.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Effects\ClCameraEffects.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Effects\ClDollyZoomEffect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Effects\ClShakeEffect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Effects\ClZoomEffect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClBardModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClBardModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClBossModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClBossModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClCameraModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDebugModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDebugModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDonutModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDonutModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDoubleTreadModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClDoubleTreadModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClFollowModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClFollowModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClLookAtModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClLookAtModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPathModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPathModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPlaneBossModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPlaneBossModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPlaneModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPlaneModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPrisonModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClPrisonModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClReverseTreadModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClReverseTreadModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClTreadModule.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameCamera\Modules\ClTreadModule.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClBardInterfaceProject.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClGameConfigProject.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClGameState.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClLevelState.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClPlayerState.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameConfig\ClSaveDataProject.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameDebug\ClStatCapture.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameEffects\ClGameEffects.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameEffects\ClSilverSwordEffect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameEffects\ClTeamAttackEffect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClArmorPieceObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClBodyPartObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClBodyPartObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClCharacterManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClCharacterObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClCharacterObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClCharacterStats.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClHeldProjectileObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClPerceptions.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClPlayerObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClPlayerObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClSteering.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClUICharacterObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClUICharacterObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\ClUserInput.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClBugbearChieftainObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClCedarFightGithyankiGeneralObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClCedarFightSlaadLordObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClMegaSpiderCaveObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClMerrshaulkObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClMerrshaulkObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClOrcKingObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClOrcKingObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClRedDragonObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClRedDragonObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClSlaadLordObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClTrollKingObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Enemies\ClTrollObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\NPCs\ClDrizztObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\NPCs\ClIronGolemObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Players\ClRogueObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Players\ClSorcererObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Character\Players\ClWarriorObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClBarrierObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClBoatObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClBoatObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClCameraObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClCinematicObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClClothSimObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClCombatStatus.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClExplosionManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClExplosionObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClInstancedCharacterManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClInstancedCharacterManager.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClInstancedCharacterObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClMineObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClMithrilFlameObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClObjectStats.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClParticleManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClParticleObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClParticlePlacementObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClPhysicsRegionObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClPickupManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClPickupObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClPlayers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClRogueShadowObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClSimMeshObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClSimulationObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClSpawnerObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClStrikableScriptObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClStruckByHistory.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClTeleportTargetObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClWeaponManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClWeaponObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\ClWickObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClEndOverProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClPointPredictProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClPointProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClPointProjectile.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClPointSeekerProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClProjectileManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClProjectileObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClShaftProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClShaftProjectile.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClSplineProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Projectile\ClSurgeProjectile.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClAnimPropObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClNoamPropObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClPropObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClPropObj.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClPropPiece.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClPropPieceManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClPropStats.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClStaticPropObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Prop\ClWorldPropObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClEnchantSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClEnchantSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClLightningSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClLightningSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClMagicMissileSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClMagicMissileSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClMeteorShowerSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClMeteorShowerSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClProtectSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClProtectSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClShieldSpell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClShieldSpell.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClSpellManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\ClSpellObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameObjs\Spell\SfSpellTypes.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameRta\ClGameRta.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClColorPulseService.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClEffectService.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClEffectService.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClShellServices.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClSimulationServices.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameServices\ClUtilServices.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClGameConsole.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClGameUI.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClMessageBox.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClOptionsDialogBox.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClPlayerHUD.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClShell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClStrings.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClTrainingHUD.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ClVoiceOver.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellMode.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellMode.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeAutoBuy.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeAutoBuy.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeController.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeController.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeCredits.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeCredits.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeHUD.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeHUD.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelEnd.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelEnd.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelEquipment.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelEquipment.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelSelect.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelSelect.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelUp.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLevelUp.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLoadGame.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeLoadGame.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeMainMenu.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeMainMenu.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeNewGame.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeNewGame.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeOptions.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeOptions.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeSaveGame.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeSaveGame.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeShow.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeShow.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeUpgrade.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\ShellMode\ClShellModeUpgrade.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClHighlightColor.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClImage.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClShellBackgroundCloud.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClShellForgroundgroup.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClText.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClText.h`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClTransitTimer.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIButtonList.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIButtonText.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIElement2d.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIImage.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIListing.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIScrollBar.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUISkillList.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIText.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\GameUI\UIParts\ClUIToggleItem.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Level\ClLevel.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\MiniGames\ClLockPickGameObj.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\MiniGames\ClMiniGameManager.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameMode.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameMode.h`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeBoot.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeBoot.h`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeInitialize.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeInitialize.h`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModePlay.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModePlay.h`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeShell.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Mode\ClGameModeShell.h`
- `C:\Projects\Phoenix\Game\Phoenix\Repository\ClAssetRepository.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Repository\ClObjFactory.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Repository\ClObjRepository.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Repository\ClServiceFactory.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\Repository\SfCreationCallbacks.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfCameraWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfCharacterWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfDeviceMethods.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfEffectsWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfLogicWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfMiscWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfRegObjectMethods.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfSimulationWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfTimeMethods.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfTriggerWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfUtilWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\ScriptWrappers\SfWeaponWrappers.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\SfMainProjectPs2.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\StateMachine\ClBoolExpData.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\StateMachine\ClInputs.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\StateMachine\ClStateData.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\StateMachine\ClStateMachine.cpp`
- `C:\Projects\Phoenix\Game\Phoenix\StateMachine\ClStateMachineData.cpp`
- `C:\Projects\Phoenix\Game\Sys\SfDebugPs2.cpp`
- `C:\Projects\Phoenix\Game\Sys\crt0.s`
