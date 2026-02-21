# Demon Stone: Engine Class Members

Extracted from Metrowerks CodeWarrior .debug section (9.3MB)
Member names extracted via C++ name mangling pattern: `member__NClassName`

## ClWorld (72 members)

- `areActiveSectors`
- `distanceToPortal`
- `draw`
- `drawClouds`
- `drawSkyBox`
- `exit`
- `getCollisionMaterial`
- `getCollisionTreeRoot`
- `getCurrentPortalTransformIndex`
- `getFrameFoliageMapMatrix`
- `getGraphicsTreeRoot`
- `getInstance`
- `getInstanceCount`
- `getInstanceDefinition`
- `getInstanceDefinitionCount`
- `getPortalLookFromCamera`
- `getRainDelta`
- `getRainImpactHeight`
- `getRainImpactHeightFromOriginDirectionVU`
- `getSectorCount`
- `getSectorIndex`
- `getSectorName`
- `getSectorStreamingChunkIndexList`
- `getShadowLightHeight`
- `getShadowVector`
- `getSnowTexture`
- `getSnowflakeTexture`
- `getSpecularBrightness`
- `getSpecularColor`
- `getSpecularPower`
- `getStatus`
- `getStreamingChunkInfoById`
- `getSunDirection`
- `hasRain`
- `hasSnow`
- `hideSectorByIndex`
- `initialize`
- `initializePortalDrawManager`
- `initializeTeleportalStatistics`
- `isOBBPenetrating`
- `isPointCollision`
- `isPortalCollision`
- `isSectorActive`
- `isSectorLoaded`
- `isSkyBoxSet`
- `isStable`
- `load`
- `loadWorldHeader`
- `m_iLastFogEntrySetting`
- `outputSectorHeaderToConsole`
- `preDraw`
- `preDrawOffsetSectors`
- `preDrawTeleportal`
- `reset`
- `resetForRespawn`
- `resolveCollisionDataAddressRecursive`
- `resolveDrawDataAddressRecursive`
- `sectorHasTeleportals`
- `sectorSetAsVisible`
- `setCurrentPortalTransformIndex`
- `setCurrentSkyBox`
- `setFrameFoliageMapMatrix`
- `setInitialSectorIndex`
- `setPortalActive`
- `setPortalTexture`
- `smData`
- `teleportalDrawThisFrame`
- `tick`
- `unregisterCollisionDataRecursive`
- `unregisterDrawDataRecursive`
- `userDefinedSectorVisibility`
- `writeLoadInfoToConsole`

## ClGfx (39 members)

- `GetFrameRegister`
- `GetViewportMatrix`
- `GetViewportOffsetX`
- `GetViewportOffsetY`
- `InitializeState`
- `MakeDefaultVP`
- `PopState`
- `PushState`
- `SetAlphaBlending`
- `SetBlendMode`
- `SetClampLowerU`
- `SetClampLowerV`
- `SetClampUpperU`
- `SetClampUpperV`
- `SetColorClamp`
- `SetDefaultState`
- `SetDepthBuffer`
- `SetDithering`
- `SetDstAlphaTestMode`
- `SetDstAlphaTesting`
- `SetFixedAlphaBit`
- `SetFogging`
- `SetFrameBuffer`
- `SetFrameBufferMask`
- `SetOnePassAntialiasing`
- `SetScissor`
- `SetShadeMode`
- `SetSrcAlphaReference`
- `SetSrcAlphaTestFailMode`
- `SetSrcAlphaTestMode`
- `SetSrcAlphaTesting`
- `SetState`
- `SetTexturing`
- `SetViewport`
- `SetWrapU`
- `SetWrapV`
- `SetXYOffset`
- `SetZTestMode`
- `SetZWrite`

## ClAudio (56 members)

- `allocateBank`
- `allocateCue`
- `allocateSegment`
- `areBanksLoading`
- `freeCue`
- `freeSegment`
- `getBankStatus`
- `getCategoryVolume`
- `getPlaylistStatus`
- `getReverbDelay`
- `getReverbDepth`
- `getReverbFeedback`
- `getReverbType`
- `getSegmentStatus`
- `initialize`
- `isBankLoading`
- `isCueIdle`
- `isCuePlaying`
- `keyOnCue`
- `keyOnPlaylist`
- `keyOnSegment`
- `loadBank`
- `loadBankAndWait`
- `loadPlaylist`
- `masterPause`
- `pauseCategory`
- `pauseSegment`
- `playCue`
- `playlistChangeDeferred`
- `playlistChangeInstant`
- `playlistChangeVolume`
- `playlistPause`
- `playlistResume`
- `playlistStop`
- `releaseCue`
- `releaseSegment`
- `reset`
- `setAttenuationScale`
- `setCategoryCueLimitCount`
- `setCategoryGroupVolume`
- `setCategoryVolume`
- `setCuePosition`
- `setCueTargetVolume`
- `setDialogEventCallback`
- `setLanguage`
- `setListener`
- `setListenerAttenuation`
- `setMasterVolume`
- `setMasterVolumeLinear`
- `setPlayCue`
- `setReverb`
- `setSegmentTargetVolume`
- `setSegmentVolume`
- `setSpeakerMode`
- `stopSegment`
- `tick`

## ClAudioData (61 members)

- `allocateBatchCommand`
- `allocateCue`
- `allocateCueHandle`
- `allocateSpuMemory`
- `calculateOutputVolume`
- `correctBankTypeOffsets`
- `flushBatchCommands`
- `freeCue`
- `freeSegment`
- `getBank`
- `getCategory`
- `getCategoryGroup`
- `getCueState`
- `getCueTypeFromBankType`
- `getEntryTypeList`
- `getListTypeFootstep`
- `getLoadedBank`
- `getRandomPitch`
- `getRandomValue`
- `getRandomVolume`
- `getSegmentStatus`
- `getSlot`
- `initSegmentForPlaylist`
- `isExclusive`
- `isInRange`
- `loadPlaylist`
- `purgeBank`
- `reset`
- `sendBatchCommands`
- `setCueEnvelope`
- `setCueIsIdle`
- `setCueMaterial`
- `setCueOutputMute`
- `setCueOutputPause`
- `setCueOutputVolume`
- `setCuePitchChange`
- `setCuePlayTime`
- `setCuePosition`
- `setCueReverb`
- `setCueVolume`
- `setMasterVolumeIop`
- `setOutputPause`
- `setOutputVolume`
- `setSegmentOutputMute`
- `setSegmentOutputPause`
- `setSegmentVolumeIop`
- `setSpeakerModeIop`
- `stepPlaylist`
- `stopBankLoads`
- `stopCue`
- `stopPlaylistLoads`
- `stopSegmentIop`
- `testBankTypeHeader`
- `tickBanks`
- `tickCue3d`
- `tickCues`
- `tickPlaylists`
- `tickSegmentVolume`
- `tickSegments`
- `tickSystemCues`
- `triggerDialogEventCallback`

## ClNoamActor (79 members)

- `__ct`
- `__vt`
- `activateHighResHead`
- `animExists`
- `attachCollisionSpheres`
- `attachToBone`
- `attachToBoneByIndex`
- `bardAttachToBone`
- `buildActor`
- `clearAllAttachments`
- `clearAllBardAttachments`
- `clearAllCollisionSpheres`
- `collSphereAttachToBone`
- `detachFromBone`
- `dispossess`
- `draw`
- `drawDamageSprites`
- `enableLOD`
- `enableLegIK`
- `enableMotionBlur`
- `enableReflection`
- `enableShadow`
- `getAlpha`
- `getAnimData`
- `getAttachmentByBoneIndex`
- `getAttachmentByIndex`
- `getBoneIndex`
- `getBoneIndexByOBBIndex`
- `getBoneIndexByUpdateIndex`
- `getBoneIndexOfAttachment`
- `getGlobalSpeed`
- `getHeadTargetPos`
- `getNumAttachementsOnBoneIndex`
- `getNumAttachments`
- `getNumBoneUpdates`
- `getNumBonesInEnum`
- `getOBBIndexByBoneIndex`
- `getOBBToWorldMatrix`
- `getSkeleton`
- `getVisibilityExtents`
- `getWorldToOBBMatrix`
- `handleBoneUpdate`
- `hasHighResHead`
- `hasMatchingCollisionSpheres`
- `initializeModel`
- `isCustomAnimPlaying`
- `isCustomMorphAnimPlaying`
- `isLODEnabled`
- `isLegIKEnabled`
- `isMotionBlurEnabled`
- `isNewSphere`
- `isReflectionEnabled`
- `isShadowEnabled`
- `linkToSphere`
- `playLinkedAnim`
- `possess`
- `release`
- `setAlpha`
- `setAlphaReferenceValue`
- `setAnim`
- `setAnimSpeed`
- `setBardAnim`
- `setCustomAnimData`
- `setGlobalSpeed`
- `setHeadTargetPos`
- `setLipAnim`
- `setModulationColor`
- `setOverrideFootstep`
- `setSimulationTeleportFlags`
- `setSurfaceType`
- `startDisintegration`
- `startReconstitution`
- `tick`
- `tickDisintegration`
- `tickReconstitution`
- `totalDamageSprites`
- `updateAllButPosition`
- `updatePosition`
- `updateVelocity`

## ClDynamicLightManager (21 members)

- `ABBIntersection`
- `createLightObject`
- `fadeInTick`
- `fadeOutTick`
- `freeLightObject`
- `getAmbient`
- `getEngineLight`
- `getSun`
- `getUIAmbient`
- `getUISun`
- `initialize`
- `killLight`
- `setAmbientProperties`
- `setLightColor`
- `setLightPosition`
- `setLightRadius`
- `setSunProperties`
- `setUIAmbientProperties`
- `setUISunProperties`
- `smData`
- `tick`

## ClParticleManager (17 members)

- `addToFreePool`
- `destroyParticle`
- `generateParticle`
- `getParticleElement`
- `getParticleObject`
- `initialize`
- `killAllParticles`
- `releaseParticle`
- `requestParticle`
- `reset`
- `smElapsedTime`
- `smNumParticles`
- `smParticleFixedList`
- `smParticleHandle`
- `smParticleList`
- `smParticlePool`
- `tick`

## ClScript (65 members)

- `beginEvent`
- `breakpointSet`
- `broadcastEvent`
- `callLatentFunc`
- `callLatentMethod`
- `callNativeAllocator`
- `callNativeFunc`
- `callNativeMethod`
- `clearSavedState`
- `execute`
- `getEventHandler`
- `getParam`
- `getParamByReference`
- `getSlotForFunc`
- `getSlotForMethod`
- `getStringFromId`
- `handleEvent`
- `initialize`
- `initializeObject`
- `loadData`
- `mpObjFactoryCB`
- `mpObjRepositoryCB`
- `mpQueuedTriggerHeader`
- `popFrame`
- `postRegInit`
- `pushFrame`
- `pushParam`
- `refToPtr`
- `regLatentFunc`
- `regNativeAllocator`
- `regNativeFunc`
- `reset`
- `restoreState`
- `resumeEvent`
- `returnValue`
- `saveState`
- `setObjectFactoryCB`
- `setObjectRepositoryCB`
- `setupPointers`
- `smCurrRegisters`
- `smCurrentParamsSize`
- `smCurrentReturnSize`
- `smEventCallState`
- `smEventHandlingStatus`
- `smIsBroken`
- `smStateBufferStatus`
- `smStopNext`
- `smWaitingForConnect`
- `smaBreakFiles`
- `smaBreakLines`
- `smaRegisters`
- `smpCodeSegment`
- `smpCurrEventHandler`
- `smpCurrObjHeader`
- `smpData`
- `smpHeader`
- `smpInstances`
- `smpNativeFuncs`
- `smpStack`
- `smpStateBuffer`
- `smpStrings`
- `smpVTables`
- `verifyNatives`
- `waitForDebuggerConnect`
- `waitOnBreakpoint`

## ClCollisionManager (16 members)

- `__ct`
- `__vt`
- `addAttribute`
- `allocateFromPool`
- `initAll`
- `initializePool`
- `isEllipsoidPenetratingAll`
- `isOBBPenetratingAll`
- `isPointCollisionAll`
- `isSphereIntersectionObject`
- `process`
- `releaseToPool`
- `removeAll`
- `removeAttribute`
- `reset`
- `smManager`

## ClDisplay (26 members)

- `begin`
- `capTo30FPS`
- `clearScreen`
- `devInitialize`
- `end`
- `flip`
- `flush`
- `initialize`
- `initializeMetrics`
- `resurrection`
- `smBorderSizeX`
- `smBorderSizeY`
- `smHalfHeightInt`
- `smHalfInverseRefreshRate`
- `smHalfLineCount`
- `smHalfWidthInt`
- `smHeight`
- `smHeightInt`
- `smIsPal`
- `smLetterBoxHeight`
- `smLineCount`
- `smRefreshRate`
- `smWidth`
- `smWidthInt`
- `viewBuffer`
- `waitForVSync`

## ClEngine (6 members)

- `__ct`
- `__vt`
- `initialize`
- `initializeAfterLoad`
- `initializeLevel`
- `smpEngine`

## ClEnginePS2 (5 members)

- `__vt`
- `initializeAfterLoadPlatform`
- `initializeLevelPlatform`
- `initializePlatform`
- `tick`

## ClShaderSystem (20 members)

- `BeginFrame`
- `EndFrame`
- `GetNumQueuedPasses`
- `GetRegisteredPhaseEnum`
- `GetRegisteredPhaseId`
- `Initialize`
- `QueueShader`
- `RegisterPhase`
- `Reset`
- `SetCamera`
- `getRegisteredPhase`
- `setPhaseEnable`
- `smCurrentContext`
- `smNumPhases`
- `smState`
- `smaContextStartCallbacks`
- `smaPhases`
- `smbInitialized`
- `unregisterPass`
- `unregisterPassByInfo`

## ClPfxSystem (16 members)

- `__ct`
- `allocate`
- `draw`
- `getPattern`
- `hardKill`
- `initialize`
- `isAlive`
- `isDead`
- `release`
- `setPosFollowsSpawn`
- `setRotation`
- `setTarget`
- `setWorldPosition`
- `softKill`
- `startSystem`
- `tick`

## ClMenu (71 members)

- `addButton`
- `addButtonMenu`
- `addButtonMenuItem`
- `addChildItem`
- `addItem`
- `addNoDrawSlider`
- `addRadioButton`
- `addRadioButtonItem`
- `addSlider`
- `addSubMenu`
- `addSubMenuItem`
- `addToggleMenu`
- `addToggleMenuItem`
- `allocateItem`
- `calculateAlpha`
- `disableEvent`
- `draw`
- `drawCursor`
- `drawItem`
- `drawMenu`
- `drawSlider`
- `drawUnderlay`
- `enableEvent`
- `enableItem`
- `getAlpha`
- `getBorderX`
- `getBorderY`
- `getChildCurrentItem`
- `getCurrentItem`
- `getCursorWidth`
- `getFadeAlpha`
- `getState`
- `initialize`
- `isIdle`
- `isInSubMenu`
- `isOff`
- `resume`
- `setActionCallback`
- `setAlpha`
- `setCancel`
- `setChildOffset`
- `setCurrentItem`
- `setCurrentToggleItem`
- `setCurserSize`
- `setDrawDefaultCursor`
- `setDrawUnderlay`
- `setDrawUnderlayFader`
- `setDropShadow`
- `setDropShadowAttrib`
- `setEventCallback`
- `setFadeTime`
- `setFontColor`
- `setFontCursorColor`
- `setFontType`
- `setRadioButtonItem`
- `setSlider`
- `setStartCancel`
- `setSubMenuItem`
- `setTitleFontColor`
- `setTitleFontType`
- `setUnderlayColor`
- `setUnderlayTextureAsset`
- `smpEventCallback`
- `suspend`
- `tick`
- `tickCursorCycle`
- `tickPad`
- `triggerActionCallback`
- `triggerEventCallback`
- `turnOff`
- `turnOn`

## ClVU1Manager (4 members)

- `GetAddressOffset`
- `Initialize`
- `Load`
- `Tick`

## ClUcodeInterface (19 members)

- `BeginFrame`
- `EndFrame`
- `GetCamera`
- `Initialize`
- `IntermediateEnd`
- `ResetState`
- `Set16BitMode`
- `SetCamera`
- `SetCurrentLight`
- `SetEnvmapMatrixAndViewPos`
- `SetIdentityTransform`
- `SetMatrices`
- `SetObjectTransform`
- `SetPropShadowMode`
- `SetPropShadowTransform`
- `SetSingleKick`
- `SetTextureMatrix`
- `SetTripleKick`
- `Setup`

## ClGfxDmaBuffer (38 members)

- `AddCall`
- `AddCallTTE`
- `AddContTTE`
- `AddRef`
- `AddRefTTE`
- `Allocate`
- `BeginCall`
- `BeginChain`
- `BeginCont`
- `BeginContTTE`
- `BeginContTTE2`
- `Commit`
- `DmacInterruptHandler`
- `EndCall`
- `EndChain`
- `EndCont`
- `EndContTTE`
- `EndContTTE2`
- `FlushReserveCache`
- `Free`
- `GenerateInterrupt`
- `GetIssueMode`
- `GetPacketBuildingMode`
- `InternalCommit`
- `InternalReserve`
- `OutOfDMABufferSpace`
- `OutstandingDMA`
- `Reserve`
- `SetIssueMode`
- `SetPacketBuildingMode`
- `Sync`
- `UpdateDmaDrainingPtr`
- `UseBuffer`
- `WaitForDmaToComplete`
- `__vt`
- `allocateGfxBuffers`
- `freeGfxBuffers`
- `initialize`

## ClGfxManager (7 members)

- `AddPhase`
- `BeginFrame`
- `Draw`
- `EndFrame`
- `Initialize`
- `SetCurrentPhase`
- `Tick`

## ClWorldWater (46 members)

- `allocRefBuffersPostPhase`
- `allocRefBuffersPrePhase`
- `allocateOffScreenBuffers`
- `baseCB`
- `basePostOpFn`
- `basePreOpFn`
- `envCB`
- `envPostOpFn`
- `envPreOpFn`
- `freeOffScreenBuffers`
- `freeRefBuffersPostPhase`
- `freeRefBuffersPrePhase`
- `getNumWaterPatchesDrawn`
- `getReflectionCamera`
- `getReflectionPatch`
- `initialize`
- `offscreenCB`
- `offscreenPostOpFn`
- `offscreenPreOpFn`
- `postBasePhase`
- `postEnvPhase`
- `postOffscreenPhase`
- `postRefPhase`
- `postSkyBoxRefPhase`
- `postSpecDrawPhase`
- `postSpecMaskPhase`
- `preBasePhase`
- `preEnvPhase`
- `preOffscreenPhase`
- `preRefPhase`
- `preSkyBoxRefPhase`
- `preSpecDrawPhase`
- `preSpecMaskPhase`
- `refCB`
- `refPostOpFn`
- `refPreOpFn`
- `skyBoxRefCB`
- `skyBoxRefPostOpFn`
- `skyBoxRefPreOpFn`
- `specDrawCB`
- `specDrawPostOpFn`
- `specDrawPreOpFn`
- `specMaskCB`
- `specMaskPostOpFn`
- `specMaskPreOpFn`
- `switchToOffscreenBuffers`

## ClWorldStreamingManager (38 members)

- `getActiveSectorMask`
- `getStreamDataDestination`
- `initialize`
- `initializeChunkStateStatistics`
- `isStable`
- `mActiveSectorMask`
- `mAwaitingTextureFixupMask`
- `mChunkSizeInBytes`
- `mCurrentLoadCount`
- `mCurrentSectorIndex`
- `mCurrentlyLoadedSectorCount`
- `mLoadedSectorMask`
- `mLoadingSectorMask`
- `mMaxConcurrentChunkCount`
- `mNewSectorActivityMask`
- `mStreamStopped`
- `mTotalAlloc`
- `mUnloadingSectorMask`
- `maChunkCountForSector`
- `maChunksLoadedForSector`
- `mbLoadImmediate`
- `mpChunkHeaders`
- `mpCurrentlyLoadingHeader`
- `mpSectorStates`
- `mppChunkPool`
- `queueDataStream`
- `registerDrawAndCollisionDataForMask`
- `registerStreamedNonTextureData`
- `registerStreamedTextureData`
- `setSectorActivityMask`
- `smState`
- `tick`
- `tickSetSectorState`
- `tickStreamingState`
- `unloadStreamData`
- `unregisterStreamedNonTextureData`
- `unregisterStreamedTextureData`
- `updateChunkStateStatistics`

## ClWorldDrawData (15 members)

- `RenderAnimUvCB`
- `RenderEnvmapCB`
- `RenderFoliageShaderCB`
- `RenderPerPixelSpecularCB`
- `RenderSelfIllumCB`
- `RenderUnsortedTranslucentAnimUvCB`
- `correctDmaChainPointers`
- `correctPointers`
- `draw`
- `initialize`
- `setKValueBias`
- `setMipmappingValues`
- `smDeltaTime`
- `smTime`
- `tick`

## ClCharacterObj (173 members)

- `CharacterStaysWithinWorld`
- `__ct`
- `__vt`
- `activate`
- `addArmorPiece`
- `addHeldProjectile`
- `addRandomDeflect`
- `addToTargetMeList`
- `canDoSuper`
- `canExecuteSuper`
- `canPlayLinkedAnim`
- `canTargetThisObj`
- `chooseSpellClassForEnemy`
- `clearInput`
- `clearInputs`
- `deactivate`
- `death`
- `destroySimulations`
- `die`
- `dispossess`
- `doWeaponAoeDamage`
- `draw`
- `dropArmor`
- `fadeOut`
- `fellOutOfWorld`
- `frameInit`
- `getArmorValue`
- `getAttackUpgrade`
- `getBodyPart`
- `getCurActionAnimId`
- `getCurActionType`
- `getCurAnimId`
- `getCurBehaviorType`
- `getDamageOverTimeAmount`
- `getDamageOverTimeAttackMask`
- `getDamageOverTimeCount`
- `getDamageOverTimeVictimPfxID`
- `getDamageOverTimeWeaponPfxID`
- `getDeflectProjectilesValue`
- `getEncounterTarget`
- `getFactionID`
- `getGoalDirection`
- `getGravity`
- `getHeadTargetPos`
- `getHealthRegenRate`
- `getIdleAnim`
- `getJumpDamageModifier`
- `getLinkedMoveType`
- `getNumBodyParts`
- `getProjectileTarget`
- `getProjectileTargetMarker`
- `getProjectileUpgrade`
- `getRangedDamageModifier`
- `getRestoreLifeItem`
- `getReverseDamageShieldValue`
- `getRunAnim`
- `getShield`
- `getShieldLevel`
- `getSpellUpgrade`
- `getStealthAbility`
- `getStealthStrikeTimeModifier`
- `getStealthTimeModifier`
- `getSuperMeterRate`
- `getTarget`
- `getTargettingUpdateBaseTime`
- `getTargettingUpdateTimeVariance`
- `getUserInput`
- `getWalkAnim`
- `getWeaponDamageModifier`
- `getWeaponSlot`
- `giveHealth`
- `giveItem`
- `handleAnimTrigger`
- `handleExplosion`
- `handleFaceAttacker`
- `handleHealthByObj`
- `handleMessage`
- `handleRumble`
- `handleStruck`
- `handleStruckByDevice`
- `handleStruckByFlame`
- `handleStruckByLinkAttack`
- `handleStruckByProjectile`
- `handleStruckByShoulderCharge`
- `handleStruckBySneakAttack`
- `handleStruckBySpell`
- `handleStruckBySplashDamage`
- `handleStruckByWeapon`
- `hasJumpTarget`
- `highlight`
- `holdProjectiles`
- `initialize`
- `initializeAttributes`
- `initializeSimulation`
- `isAlive`
- `isBossDeflecting`
- `isCharacterSeparationEnabled`
- `isCharacterWorldCollisionEnabled`
- `isCollisionFound`
- `isDeflecting`
- `isDisabled`
- `isInputSet`
- `isInvulnerable`
- `isJumping`
- `isTargetable`
- `isTargetableByPlayer`
- `killAttachedParticles`
- `makeTargetable`
- `msRTTI`
- `possess`
- `prepForDestroy`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `removeFromTargetMeList`
- `reset`
- `resurrect`
- `sauAddArmorPiece`
- `sauAddHeldProjectile`
- `sauBlockEvadeSuccess`
- `sauCanDoTeamAttack`
- `sauCharacterInit`
- `sauDisableSuper`
- `sauEnableAI`
- `sauEndSuperAttack`
- `sauEndTeamAttackCharge`
- `sauGetHitPoints`
- `sauGetMaxHitPoints`
- `sauInitializeSimulation`
- `sauObjectiveTeleport`
- `sauSetWeapon`
- `sauSilverSwordDeath`
- `sauStartSuperAttack`
- `sauStartTeamAttackCharge`
- `sauStartTeamSuperAttack`
- `sendEventToMe`
- `setAssetContainer`
- `setEncounterTarget`
- `setEnemyDBName`
- `setGravity`
- `setInput`
- `setInvulnerable`
- `setIsUICharacter`
- `setJumpTarget`
- `setMatrix`
- `setMaxAttackers`
- `setModulationColor`
- `setPosition`
- `setRotation`
- `setSectorIndex`
- `setWalkableObject`
- `setWeapon`
- `sleep`
- `startDamageOverTime`
- `startPersistentInput`
- `startPersistentTimedInput`
- `startWeaponCollision`
- `stopAllPersistentInputs`
- `stopAllWeaponCollision`
- `stopAllWeaponCollisionPending`
- `stopAllWeaponTrails`
- `stopAllWeaponTrailsPending`
- `stopDamageOverTime`
- `stopPersistentInput`
- `stopWeaponCollision`
- `struckAudio`
- `tickAction`
- `tickActionMachine`
- `tickBuild`
- `tickCollision`
- `tickInitial`
- `tickWeaponCollision`
- `updatePersistentInputs`
- `useRestoreLifeItem`

## ClPlayerObj (63 members)

- `__ct`
- `__vt`
- `addHeldProjectile`
- `addToIgnoreTargets`
- `addToRangedTargets`
- `addUpgrade`
- `applyInstantaneousItem`
- `callForHelp`
- `canDoTeamSuper`
- `canTargetThisObj`
- `clearInputs`
- `clearRangedTargets`
- `controlChar`
- `death`
- `die`
- `disableTargetingIcon`
- `enableTargetingIcon`
- `fellOutOfWorld`
- `fillRangedTargetList`
- `findNearestScreenTarget`
- `getArmorValue`
- `getAttackUpgrade`
- `getDamageOverTimeAmount`
- `getDamageOverTimeAttackMask`
- `getDamageOverTimeCount`
- `getDamageOverTimeVictimPfxID`
- `getDamageOverTimeWeaponPfxID`
- `getDeflectProjectilesValue`
- `getHealthRegenRate`
- `getJumpDamageModifier`
- `getListenerPosition`
- `getNextTarget`
- `getProjectileSource`
- `getProjectileUpgrade`
- `getRangedDamageModifier`
- `getRestoreLifeItem`
- `getReverseDamageShieldValue`
- `getShieldLevel`
- `getSpellUpgrade`
- `getStealthAbility`
- `getStealthStrikeTimeModifier`
- `getStealthTimeModifier`
- `getSuperMeterRate`
- `getSuperMeterRecord`
- `getTargettingUpdateBaseTime`
- `getTargettingUpdateTimeVariance`
- `getWeaponDamageModifier`
- `giveItem`
- `giveSkill`
- `handleMessage`
- `holdProjectiles`
- `initialize`
- `isCollisionFound`
- `isDefending`
- `lockOntoNearestTarget`
- `msRTTI`
- `possess`
- `sauIgnoreCurrentTarget`
- `setWeapon`
- `tickAction`
- `tickActionMachine`
- `updatePlayerState`
- `useRestoreLifeItem`

## ClPropObj (42 members)

- `__ct`
- `__vt`
- `activate`
- `changeHitPoints`
- `deactivate`
- `dispossess`
- `fadeOut`
- `getProjectileTarget`
- `handleDestroyedProp`
- `handleExplosion`
- `handleMessage`
- `handleStruck`
- `handleStruckAndDestroyedProp`
- `handleStruckByDevice`
- `handleStruckByProjectile`
- `handleStruckByShoulderCharge`
- `handleStruckBySpell`
- `handleStruckBySplashDamage`
- `handleStruckByWeapon`
- `heal`
- `initialize`
- `initializeAttributes`
- `msRTTI`
- `possess`
- `removeAllAttributesAndServices`
- `reset`
- `sauDisableCollision`
- `sauFade`
- `sauManuallyDestroy`
- `sauSetCrashable`
- `sauSetPlayerOnlyStrikable`
- `sauSetPropStats`
- `setIlluminationTargets`
- `setMatrix`
- `setModifiers`
- `setPosition`
- `setRotation`
- `tickAction`
- `tickBuild`
- `tickCollision`
- `tickFinal`
- `updateModulationColor`

## ClNoamSkeleton (37 members)

- `BeginSkeletonComputation`
- `BlendAnimation`
- `BlendBardAnimation`
- `CalculateRootBoneTranslation`
- `CalculateRootBoneTranslationSecondaryAnim`
- `ComputeSkeletalHierarchy`
- `ComputeSkeletalHierarchyProcessBoneUpdates`
- `ComputeSkeletalHierarchyProcessHeadTracking`
- `ComputeSkeletalHierarchyProcessSimulations`
- `EndSkeletonComputation`
- `GetSkeletalHierarchyLOD0`
- `GetSkeletalHierarchyLOD0NoXfer`
- `GetSkeletalHierarchyLOD1`
- `SetAnimTimeFactor`
- `StartAnimation`
- `SwapPrimaryAndSecondaryMixerInputs`
- `Update`
- `UpdateBlending`
- `UpdateTime`
- `UpdateTriggers`
- `__ct`
- `addSimulation`
- `calculateOrientedBBoxes`
- `canDoAttackRotation`
- `canDoBackRecoil`
- `getAnimBBox`
- `getEndTime`
- `getOBBInfo`
- `isCustomAnimPlaying`
- `resetIK`
- `setIKBlend`
- `setSpineRotation`
- `updateAnimationEventTriggers`
- `updateFootTriggers`
- `updateLinkTriggers`
- `updateNoteTriggers`
- `updateSoundTriggers`

## ClShell (78 members)

- `dispatchEvent`
- `drawText`
- `getSafeX`
- `getSafeY`
- `getSubtitleAsset`
- `getTextureAsset`
- `initShellText`
- `initialize`
- `isTransitInDone`
- `isTransitOutDone`
- `keyOnAmbient`
- `load`
- `modeDraw2d`
- `modeDraw3d`
- `modeEnter`
- `modeExit`
- `modeIsIdle`
- `modeTick`
- `preTick`
- `registerScriptWrappers`
- `sauShellRegisterBackground`
- `sauShellRegisterDispatch`
- `sauShellRegisterForgroundGroup`
- `sauShellRegisterInfo`
- `sauShellRegisterMenu`
- `setDefaultGraphicsState`
- `setDrawProperties`
- `setMode`
- `smBlack`
- `smBrightUnderlayLeft`
- `smBrightUnderlayRight`
- `smCharacter`
- `smClearColor`
- `smColorSet`
- `smCursorCycleRate`
- `smCursorCycleRatio`
- `smDarkRed`
- `smDisabledTextColor`
- `smDropColor`
- `smDropX`
- `smDropY`
- `smFadeTime`
- `smFontType`
- `smGreen`
- `smGroup`
- `smHalfRed`
- `smMenuHeight`
- `smMenuWidth`
- `smPlacardUnderlayLeft`
- `smPlacardUnderlayRight`
- `smPrimaryFocusColor`
- `smPrimaryTextColor`
- `smRed`
- `smRingTransitTime`
- `smSafeH`
- `smSafeHalfH`
- `smSafeHalfW`
- `smSafeW`
- `smSafeX`
- `smSafeY`
- `smSunBlue`
- `smSunDirection`
- `smSunGreen`
- `smSunRed`
- `smTimer`
- `smTitleFontType`
- `smUnderlayLeft`
- `smUnderlayRight`
- `smWhite`
- `smYellow`
- `smaEmptyString`
- `smaTypeH`
- `smpGameCamera`
- `startAmbient`
- `stopAmbient`
- `transitBackward`
- `transitForward`
- `unload`

## ClLevel (25 members)

- `adjustForDifficulty`
- `beginDraw3d`
- `disableLoadConsole`
- `draw2d`
- `draw3d`
- `drawView`
- `enableLoadConsole`
- `endDraw3d`
- `getClearScreenRGB`
- `getLevelReset`
- `getTextureAsset`
- `initialize`
- `load`
- `postLoad`
- `postLoadStable`
- `preLoad`
- `registerScriptWrappers`
- `reset`
- `resetForRespawn`
- `setClearColor`
- `setLevelReset`
- `setMachineConfig`
- `stabilize`
- `tick`
- `unload`

## ClGameState (24 members)

- `beginLevel`
- `devDisplayStats`
- `devInitialize`
- `devInitializePlayer`
- `devInitializePlayers`
- `devInitializeStockPlayer`
- `devInitializeUnlocked`
- `devSetInitialize`
- `endLevel`
- `getLevel`
- `getLevelState`
- `getPlayerState`
- `getUnlockedState`
- `hasPlayerSetDifficulty`
- `initialize`
- `isFirstLevel`
- `newGame`
- `restoreState`
- `restoreStateRespawn`
- `setFirstLevel`
- `setLevel`
- `setPlayerSetDifficulty`
- `storeState`
- `storeStateRespawn`

## ClTexEnv (37 members)

- `AllocTexture_2BlockLerp`
- `BeginFrame`
- `CopyMipmapChain`
- `CopyPalette`
- `CopyVideoMipmapChain`
- `CreateMipmapChainWithGS`
- `EndFrame`
- `FreePermanentTexture`
- `FreePermanentTexture_2BlockLerp`
- `FreePermanentTexture_Default`
- `FreeTexture`
- `FreeTexture_2BlockLerp`
- `FreeTexture_Default`
- `GetTextureRegs`
- `InitializeTexEnv`
- `PopTexEnv`
- `PushTexEnv`
- `SetPath3Mask`
- `SetTCC`
- `SetTexEnv`
- `SetTexture`
- `SetTextureFunction`
- `SetTextureLK`
- `SetTexture_2BlockLerp`
- `SetTexture_Default`
- `isUsePath3`
- `mCurrTexCount`
- `mDbuffNum`
- `mDmaAmount`
- `mPath3State`
- `mPermTexDepth`
- `mTexCount`
- `mTexDepth`
- `mTexType`
- `mpLastTag`
- `mpLastTex`
- `totalDmaUsedQW`

## ClDrawAttrib (15 members)

- `__ct`
- `enableShadow`
- `findContainingNodeRecursive`
- `findContainingSectorIndex`
- `fullyContained`
- `init`
- `isVisible`
- `registerObject`
- `release`
- `setModulationColor`
- `setVisibilityAabb`
- `setVisibilityMatrix`
- `setVisibilitySphere`
- `unregisterObject`
- `updateRegistration`

## ClCollisionAttrib (25 members)

- `__ct`
- `findContainingNodeRecursive`
- `findContainingSectorIndex`
- `fullyContained`
- `init`
- `isEllipsoidPenetrating`
- `isInCylinder`
- `isInSphere`
- `isInView`
- `isOBBPenetrating`
- `isPointCollision`
- `isSphereIntersection`
- `pointVelocity`
- `process`
- `registerObject`
- `release`
- `setCylinder`
- `setEllipsoid`
- `setMesh`
- `setObb`
- `setSphere`
- `triviallyReject`
- `unregisterObject`
- `updateData`
- `updateRegistration`

## ClPfxPattern (17 members)

- `__ct`
- `draw`
- `getRandomFireSegments`
- `hardKill`
- `initialize`
- `initializeBasicParticle`
- `initializeBillboard`
- `initializeFireSamples`
- `initializeGeometryParticle`
- `initializeTrailHead`
- `release`
- `setPattern`
- `setTargetPosition`
- `setWorldPosition`
- `softKill`
- `startPattern`
- `tick`

## ClBillboardParticleRenderer (5 members)

- `BeginPacket`
- `BeginRendering`
- `EndPacket`
- `EndRendering`
- `GetMaxParticlesPerPacket`

## ClPropRenderer (28 members)

- `getNewPropInstanceList`
- `getNewPropShaderList`
- `initialize`
- `mCurrentTransformID`
- `mFrameInstanceCount`
- `mFramePropInstanceListCount`
- `mFramePropShaderListCount`
- `mTeleportalItemsQueued`
- `maInstancePool`
- `maPhaseList`
- `maPropInstanceList`
- `maPropShaderList`
- `mpCurrentCamera`
- `mpCurrentPropPhase`
- `mpLastCameraList`
- `mpLastPropInstanceList`
- `mpLastPropShaderList`
- `postPropAlphaPhase`
- `prePropAlphaPhase`
- `render`
- `renderAlpha`
- `renderReflections`
- `renderShadowCastPhases`
- `renderShadowRecievingPhases`
- `reset`
- `resetUcodeState`
- `setUcodeCameraState`
- `updateCurrentPhase`

## ClRain (19 members)

- `drawDrops`
- `drawSnowDrops`
- `drawSplashes`
- `initialize`
- `render`
- `renderRainEffect`
- `renderSnowEffect`
- `returnDropToFreeList`
- `returnFlakeToFreeList`
- `returnSplashToFreeList`
- `setColor`
- `setDropAlphaRange`
- `setEnable`
- `setSplashAlphaRange`
- `smData`
- `spawnRainParticle`
- `spawnSnowflake`
- `spawnSplash`
- `tick`

## ClWind (4 members)

- `getBaseDirection`
- `getMagnitude`
- `getWindVector`
- `smData`

## ClCloud (6 members)

- `CB`
- `correctPointers`
- `draw`
- `postPhase`
- `prePhase`
- `setCloudsOn`

## ClSkyBox (13 members)

- `RenderSkyboxCB`
- `RenderSkyboxRefCB`
- `correctPointers`
- `draw`
- `facesReflected`
- `postOpFn`
- `postPhase`
- `postRefOpFn`
- `postRefPhase`
- `preOpFn`
- `prePhase`
- `preRefOpFn`
- `preRefPhase`

## All Classes (5+ members)

### ClAI (6 members)

- `areEnemies`
- `areFriends`
- `getFactionID`
- `getInputList`
- `initialize`
- `normalizeAngle`

### ClAIObj (12 members)

- `__ct`
- `clearInputs`
- `frameInit`
- `getNextObjective`
- `reset`
- `setObjective`
- `setTetherObj`
- `setup`
- `switchActionStateMachines`
- `tick`
- `tickCondition`
- `tickDecision`

### ClActionAttack (7 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`
- `updateDirection`

### ClActionBlockReact (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionCastSpell (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionCliff (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionControl (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionDead (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionDying (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionFaceMithril (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionFaceObjective (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionFaceTarget (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionFall (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionFallOffLadder (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionHoldDragon (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionJump (8 members)

- `__vt`
- `computeTrajectory`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`
- `updateLeftStickJumping`

### ClActionJumpAttack (7 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`
- `updateDirection`

### ClActionJumpOntoDragon (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionKillmove (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionLand (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionLink (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavHealth (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavMithril (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavObjective (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavShadow (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavTarget (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNavTether (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionNone (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionPlayAnim (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionRogueSuper (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionShoot (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionSneakAttack (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionStateCode (9 members)

- `__vt`
- `calcHeading`
- `clampHeading`
- `clrAllFlags`
- `clrFlag`
- `enter`
- `isFlagSet`
- `setFlag`
- `tick`

### ClActionStateMachine (7 members)

- `__vt`
- `forceStateChange`
- `handleStateEnter`
- `handleStateExit`
- `initialize`
- `tick`
- `tickCollision`

### ClActionStopSpell (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionTakeHit (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionTeamAttack (6 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`

### ClActionUserLoco (8 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `tick`
- `tickCollision`
- `updateDirection`
- `updateInputState`

### ClActionUtils (11 members)

- `calcHeading`
- `clampHeading`
- `collideCharacter`
- `collideCharacterPlatform`
- `dampenLateralMotion`
- `getDirectionalVelocity`
- `getZooAnimDirection`
- `parseAttackMask`
- `parseSpellMask`
- `updateDirection`
- `wasVerticalCollision`

### ClActionZoo (7 members)

- `__vt`
- `enter`
- `exit`
- `getName`
- `playNewAnim`
- `tick`
- `tickCollision`

### ClActor (18 members)

- `__vt`
- `createActor`
- `dispossess`
- `enableLegIK`
- `enableReflection`
- `enableShadow`
- `getType`
- `isLegIKEnabled`
- `isReflectionEnabled`
- `isShadowEnabled`
- `possess`
- `setHeading`
- `setLastPosition`
- `setLocation`
- `setMatrix`
- `setOwner`
- `setPosition`
- `setSurfaceType`

### ClAlphaSortRenderer (24 members)

- `isDataQueued`
- `renderQueuedData`
- `reset`
- `setCamera`
- `smLastBlendType`
- `smNumCameras`
- `smNumElems_DB`
- `smNumQueuedTextures`
- `smPropViewMat`
- `smTotalNumElems`
- `smViewMat`
- `smZMin`
- `smZMult`
- `smaBaseArray`
- `smaSortArray_A`
- `smaSortArray_B`
- `smaSortQueues`
- `smpCamera`
- `smpCurQueue`
- `smpLastPropSubobjectMatrix`
- `smpLastTexture`
- `smpQueuedTextures`
- `smpSort_A`
- `smpSort_B`

### ClAnimBin (23 members)

- `animExistsForModel`
- `getAnimBoneHeader`
- `getAnimSetHeader`
- `getAttackInfo`
- `getBoneIndex`
- `getBoneList`
- `getCharacterSimulationDataCount`
- `getDataForNthSimulation`
- `getEndTime`
- `getHeadTrackingInfo`
- `getIKInfo`
- `getLODInfo`
- `getLinkPfxBoneArray`
- `getNumBones`
- `getNumLevelsOfDetail`
- `getNumLinkPfxBones`
- `getNumSegments`
- `getOrientedBBoxArray`
- `getParentList`
- `getSegmentInfo`
- `getSkeletonDataHeader`
- `getSoundTrigHeader`
- `verifyData`

### ClAnimPropObj (23 members)

- `__ct`
- `__vt`
- `activate`
- `draw`
- `getBoneIndexByUpdateIndex`
- `getNumBoneUpdates`
- `handleBoneUpdate`
- `handleMessage`
- `handleNoamMsg`
- `handleStruckAndDestroyedProp`
- `initialize`
- `msRTTI`
- `registerScriptMethods`
- `reset`
- `sauAnimPropInit`
- `sauFinishAnim`
- `sauIsPlayingAnim`
- `sauSetAnim`
- `setAnim`
- `setAssetContainer`
- `setIlluminationTargets`
- `tickAction`
- `tickBuild`

### ClArmorPieceObj (6 members)

- `__ct`
- `__vt`
- `draw`
- `drop`
- `msRTTI`
- `tick`

### ClAssetMap (5 members)

- `__ct`
- `getContainer`
- `numContainers`
- `reset`
- `setData`

### ClAssetRepository (5 members)

- `getAssetById`
- `getContainer`
- `initialize`
- `reset`
- `setAssetMap`

### ClAttributeManager (6 members)

- `__vt`
- `addAttribute`
- `processQueues`
- `removeAll`
- `removeAttribute`
- `reset`

### ClAttributeObj (23 members)

- `__ct`
- `__vt`
- `addAttribute`
- `addService`
- `findAttribute`
- `getDirection`
- `getOwner`
- `getSectorIndex`
- `handleMessage`
- `hasAttribute`
- `hasServiceOfType`
- `initializeAttributes`
- `msRTTI`
- `notifyReflectionStateChange`
- `removeAllAttributesAndServices`
- `removeAttribute`
- `removeService`
- `setDirection`
- `setMatrix`
- `setOwner`
- `setPosition`
- `setRotation`
- `setSectorIndex`

### ClAudioHookDB (7 members)

- `getAudioHookRecord`
- `installMenuEventCallback`
- `load`
- `menuEventCallback`
- `play`
- `smpAudioHookRecords`
- `smpHeader`

### ClBSpline (6 members)

- `clear`
- `draw`
- `getNearestSplinePos`
- `getPointAlongPath`
- `initialize`
- `setSpline`

### ClBard (32 members)

- `allocateStreamingBuffer`
- `canPlayScriptedEvent`
- `drawSubtitles`
- `drawUI`
- `getCameraDirection`
- `getCameraFov`
- `getCameraPosition`
- `getCameraTilt`
- `getCinematicTimeWithOverrideName`
- `getNumOpenSlots`
- `getTotalCinematicTimeWithOverrideName`
- `initialize`
- `initializeDisabled`
- `isLetterBoxing`
- `isPlaying`
- `pendingSlowMotionRestore`
- `playerCanTrigger`
- `preloadCinematic`
- `preloadCinematicAndWait`
- `releaseStreamingBuffer`
- `setInitialSector`
- `smAudioSegmentFilename`
- `smAudioSegmentHandle`
- `smStreamingDataBufferUsed`
- `smpData`
- `smpStreamingDataBufferOwner`
- `start`
- `stop`
- `stopCinematicWithOverrideName`
- `stopSpecificCinematic`
- `tick`
- `updateSectorIndex`

### ClBardCubicCurve (5 members)

- `__ct`
- `clear`
- `getPointAtTime`
- `setCurve`
- `spline`

### ClBardInterfaceProject (34 members)

- `__vt`
- `activateBardCamera`
- `addCharacterToScene`
- `addPropToScene`
- `addSimulationToScene`
- `deactivateBardCamera`
- `destroyParticle`
- `doBardCameraShake`
- `doPropAnimation`
- `getCharacterByAC`
- `getCharacterByName`
- `getHeroCharacter`
- `getNoamActor`
- `getParticleObj`
- `getPropByAC`
- `getPropByName`
- `getPropNumSubobjs`
- `getPropSubobjMatrix`
- `getSimulationByAC`
- `getSimulationByName`
- `getSimulationId`
- `initialize`
- `killAllParticles`
- `notifyCameraOfCut`
- `processCommand`
- `removeCharacterFromScene`
- `removePropFromScene`
- `removeSimulationFromScene`
- `setBardCameraSectorIndex`
- `smInterface`
- `startCinematic`
- `stopCinematic`
- `turnOffLetterBox`
- `turnOnLetterBox`

### ClBardModule (7 members)

- `__ct`
- `__vt`
- `cutTo`
- `draw`
- `getName`
- `getSectorIndex`
- `solveConstraints`

### ClBarrierObj (11 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `debugDraw`
- `initializeAttributes`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `sauSetExtents`
- `sauSetOptions`

### ClBehaviorStackMachine (9 members)

- `__vt`
- `evaluate`
- `handleStateEnter`
- `handleStateExit`
- `initialize`
- `popState`
- `pushState`
- `reset`
- `tick`

### ClBoatObj (16 members)

- `__ct`
- `__vt`
- `activate`
- `msRTTI`
- `registerScriptMethods`
- `reset`
- `setDirection`
- `setMatrix`
- `setObjective`
- `setPosition`
- `setRotation`
- `tickAction`
- `tickCollision`
- `tickFinal`
- `updatePhysics`
- `updateSteering`

### ClBodyPartObj (22 members)

- `__ct`
- `__vt`
- `activate`
- `applyDamage`
- `deactivate`
- `debugDrawHealthAndDamage`
- `disable`
- `handleMessage`
- `handleStruck`
- `handleStruckByDevice`
- `handleStruckByProjectile`
- `handleStruckByShoulderCharge`
- `handleStruckBySpell`
- `handleStruckBySplashDamage`
- `handleStruckByWeapon`
- `initialize`
- `isCharacterSeparationEnabled`
- `isTargetable`
- `msRTTI`
- `setMatrix`
- `setPosition`
- `setRotation`

### ClBoneAttachmentConstraint (5 members)

- `__ct`
- `__vt`
- `process`
- `setBoneAttachmentParams`
- `teleport`

### ClBossModule (18 members)

- `__ct`
- `__vt`
- `cutTo`
- `draw`
- `getBoss`
- `getBossHeightOffset`
- `getDesiredHeight`
- `getDesiredPitch`
- `getFollowJump`
- `getFov`
- `getLookAtPlayer`
- `getMaxFollowDistance`
- `getName`
- `getPitchRange`
- `getSectorIndex`
- `getSubjectOverride`
- `getViewTargetSLerpSpeed`
- `solveConstraints`

### ClBrxActorControl (9 members)

- `computeRotation`
- `doAnimation`
- `doMouthAnimation`
- `setActor`
- `setPosition`
- `setRotation`
- `setTargetPosition`
- `setTargetRotation`
- `tick`

### ClBrxInterpolator (14 members)

- `allocate`
- `getKeyValue1d`
- `getKeyValue3d`
- `getKeyValueQuaternion`
- `initialize`
- `initializeQuaternion`
- `interpolateTime`
- `set1d`
- `set3d`
- `set4d`
- `tick1d`
- `tick3d`
- `tick3dCubicCurve`
- `tickQuaternion`

### ClBugbearChieftainObj (5 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `msRTTI`
- `registerScriptMethods`

### ClCamera (23 members)

- `__as`
- `__ct`
- `clipToFrustum`
- `getCamPosition`
- `getFrustumCopy`
- `getFrustumDeltas`
- `getFrustumLocalPoints`
- `getZBufferValue`
- `init`
- `initViewport`
- `lookAt`
- `multMatrix`
- `projection`
- `projectionWithFrustumDir`
- `recomputeMatrices`
- `roll`
- `setDrawContext`
- `setFarPlane`
- `setNearPlaneDistance`
- `setZBufferBias`
- `smAxisFlipMatrix`
- `smTransformToClipMatrix`
- `tick`

### ClCameraEffects (5 members)

- `getEffectMemory`
- `initialize`
- `releaseEffect`
- `reset`
- `smaEffectsPool`

### ClCameraList (8 members)

- `getCameraCount`
- `getCameraListForSector`
- `getCameraSectorMask`
- `getCameraToAdd`
- `initialize`
- `preDrawObjects`
- `reset`
- `smData`

### ClCameraMgr (9 members)

- `addCamera`
- `getGameCamera`
- `getNumCameras`
- `initialize`
- `reset`
- `setFarPlane`
- `smNumCameras`
- `smaCameras`
- `tick`

### ClCameraObj (16 members)

- `__ct`
- `__vt`
- `msRTTI`
- `registerScriptMethods`
- `sauActivate`
- `sauInitBossCam`
- `sauInitDonutCam`
- `sauInitDoubleTreadCam`
- `sauInitFollowCam`
- `sauInitLookAtCam`
- `sauInitPathCam`
- `sauInitPlaneBossCam`
- `sauInitPlaneCam`
- `sauInitPrisonCam`
- `sauInitReverseTreadCam`
- `sauInitTreadCam`

### ClCameraPath (8 members)

- `addPathPoint`
- `clearPath`
- `draw`
- `drawCubicBSplinePath`
- `drawPath`
- `getPathPoint`
- `getPointAlongPath`
- `projectPointToBSpline`

### ClCedarFightGithyankiGeneralObj (8 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `isDeflecting`
- `msRTTI`
- `registerScriptMethods`
- `sauSetPhase`
- `tickAction`

### ClCedarFightSlaadLordObj (9 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `isDeflecting`
- `msRTTI`
- `registerScriptMethods`
- `sauSetPhase`
- `sauTeleport`
- `tickAction`

### ClCharacterManager (37 members)

- `addToActiveList`
- `createCharacter`
- `createCharacterBegin`
- `createCharacterEnd`
- `getFrontEndCharacter`
- `initialize`
- `isValidCharacter`
- `registerScriptMethods`
- `releaseCharacter`
- `releaseFrontEndCharacter`
- `removeFromActiveList`
- `reset`
- `sauCreateCharacter`
- `sauEnableWeaponDamageOverTime`
- `sauFreeCharacter`
- `sauShellRegisterCharacter`
- `sauShellUnregisterCharacter`
- `sbWeaponDamageOverTimeEnabled`
- `smCharacterSlotHint`
- `smCreationState`
- `smCurCharacterHandle`
- `smCurPoolSize`
- `smCurSlot`
- `smMaxCharacterSize`
- `smMaxCharactersAllocated`
- `smNumCharacters`
- `smNumFreeCharacters`
- `smNumPooledCharacters`
- `smPooledCharacterSize`
- `smapFrontEndCharacters`
- `smpActiveCharacterRoot`
- `smpCharacterMemory`
- `smpCharacters`
- `smpCurCharacter`
- `smpPoolMemory`
- `smpRedDragon`
- `tick`

### ClCharacterSimulation (10 members)

- `__ct`
- `__vt`
- `cut`
- `deactivate`
- `draw`
- `getStripRootByIndex`
- `initialize`
- `postTick`
- `setAttachmentActor`
- `tick`

### ClCharacterStats (18 members)

- `__ct`
- `__vt`
- `canDoSuperAttack`
- `canDoTeamAttack`
- `finishedSuperAttack`
- `finishedTeamAttack`
- `getMinTeamAttackValue`
- `getNormalizedSuperLevel`
- `getSuperLevel`
- `increaseSuperMeter`
- `isImmuneToSpell`
- `m_fDecrementModifier`
- `setAccumulating`
- `setDifficultyModifier`
- `setSpellImmunities`
- `setSuperLevel`
- `startedSuperAttack`
- `tick`

### ClChargedMagicMissileSpell (6 members)

- `__ct`
- `__vt`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClCinematicObj (20 members)

- `__ct`
- `__vt`
- `cinematicDoneLoading`
- `cinematicPlay`
- `cinematicPreload`
- `cinematicStartupInit`
- `cinematicStartupPlay`
- `cinematicStop`
- `handleMessage`
- `msRTTI`
- `registerScriptMethods`
- `sauCinematicDoneLoading`
- `sauCinematicInit`
- `sauCinematicPlay`
- `sauCinematicPreload`
- `sauCinematicStartupInit`
- `sauCinematicStartupPlay`
- `sauCinematicStop`
- `sauDumpPreloadedCinematic`
- `setAssetContainer`

### ClClock (30 members)

- `devSlow`
- `devUnslow`
- `freeze`
- `initialize`
- `reset`
- `setSlowTimeMultiplier`
- `slow`
- `smDeltaMilli`
- `smDeltaSec`
- `smDevFrozen`
- `smDevSlow`
- `smDevSlowDeltaMilli`
- `smFrozen`
- `smMissionDeltaMilli`
- `smMissionDeltaSec`
- `smMissionFrozen`
- `smMissionTimeMilli`
- `smMissionTimeSec`
- `smPhysicalDeltaMilli`
- `smPhysicalDeltaSec`
- `smPhysicalTimeMilli`
- `smPhysicalTimeSec`
- `smSlow`
- `smSlowTimeMultiplier`
- `smTimeMilli`
- `smTimeSec`
- `tick`
- `tickClocks`
- `unfreeze`
- `unslow`

### ClClothSimObj (17 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `draw`
- `handleMessage`
- `initializeAttributes`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `sauFree`
- `sauInit`
- `sauSetRippleParams`
- `setMatrix`
- `setPosition`
- `setRotation`
- `tickFinal`

### ClConfigDB (8 members)

- `getConfigRecord`
- `initialize`
- `load`
- `setCurrentLevel`
- `smIsDefault`
- `smpCurRecord`
- `smpHeader`
- `smpRecords`

### ClConfiguration (18 members)

- `addSelectableLanguage`
- `getCurAudioDir`
- `getCurFmvDir`
- `getHardwareDateNotation`
- `getHardwareTimeNotation`
- `getLanguageLevel`
- `getLanguageTypeByLevel`
- `getPrimaryLanguage`
- `getSelectableLanguage`
- `getSelectableLanguageCount`
- `getSelectableLanguageGameNameLine1`
- `getSelectableLanguageGameNameLine2`
- `initialize`
- `isLanguageLevels`
- `isSecondaryLanguage`
- `isTertiaryLanguage`
- `setLanguageLevel`
- `setLanguageLevels`

### ClConfigurationData (7 members)

- `__vt`
- `getCharacterStatus`
- `getNextCharacter`
- `getVariable`
- `parse`
- `parseVariable`
- `ungetCharacter`

### ClConsole (5 members)

- `disable`
- `displayDebugConsole`
- `enable`
- `initialize`
- `setUserDrawCallback`

### ClConstraintFunctions (9 members)

- `solveBardCamera`
- `solveDebugCamera`
- `solveDontFollowJump`
- `solvePreventGimbalLock`
- `solveStayBack`
- `solveStayClose`
- `solveTargetFrameHeight`
- `solveViewPitchLock`
- `solveViewTarget`

### ClConstraintInstance (9 members)

- `__ct`
- `__vt`
- `affectsSimulationSubObject`
- `postTick`
- `setOpenParameterValueFloat`
- `setOpenParameterValueInteger`
- `setOpenParameterValueVector`
- `setPoint`
- `teleport`

### ClConstraintListPool (6 members)

- `__ct`
- `addInstance`
- `initialize`
- `removeInstance`
- `sMaxConstraintType`
- `sMaxNumConstraintLists`

### ClConstraintManager (22 members)

- `getConstraintById`
- `getConstraintUsedRecord`
- `getNewBoneAttachmentConstraint`
- `getNewCollisionConstraint`
- `getNewSegmentLengthConstraint`
- `getNewStaticAttachmentConstraint`
- `initialize`
- `releaseConstraint`
- `simulationTeleport`
- `smaBoneAttachmentConstraintPool`
- `smaCollisionConstraintPool`
- `smaConstraintLists`
- `smaConstraintUsedRecordPool`
- `smaConstraintsInUseCount`
- `smaControlPointAttachmentConstraintPool`
- `smaMaxConstraintsUsedCount`
- `smaParallelSegmentConstraintPool`
- `smaSegmentLengthConstraintPool`
- `smaStaticAttachmentConstraintPool`
- `smapFreeConstraintRoot`
- `smpFreeConstraintUsedRecordRoot`
- `tick`

### ClConstraintSphere (7 members)

- `__ct`
- `__vt`
- `add`
- `initialize`
- `isEquivalent`
- `msRTTI`
- `release`

### ClControl (5 members)

- `__ct`
- `calculateUV`
- `draw`
- `offset`
- `pulseColor`

### ClControlPoint (5 members)

- `addConstraint`
- `initialize`
- `isConstrainedToOtherPoints`
- `removeConstraint`
- `tick`

### ClControlPointPool (7 members)

- `freeControlPoint`
- `getControlPoint`
- `initialize`
- `mFreePointsCount`
- `mFreeRoot`
- `mFreeTail`
- `maPool`

### ClDB (6 members)

- `getEntrySwitch`
- `getNumRecords`
- `getRecord`
- `getRecordByIndex`
- `maDBData`
- `setEntryData`

### ClDebugCallStack (7 members)

- `popCall`
- `pushCall`
- `smAvailableList`
- `smCallList`
- `smCollecting`
- `smaStackElements`
- `transmit`

### ClDebugModule (6 members)

- `__vt`
- `cutTo`
- `draw`
- `getName`
- `getSectorIndex`
- `solveConstraints`

### ClDecal (9 members)

- `CB`
- `addDecal`
- `initialize`
- `postOpFn`
- `postPhase`
- `preOpFn`
- `prePhase`
- `smNumActiveDecals`
- `tick`

### ClDevConsole (15 members)

- `clear`
- `draw`
- `drawBackground`
- `drawProgress`
- `drawProgressBar`
- `drawText`
- `initialize`
- `initializeDisplay`
- `isVisible`
- `miniDraw`
- `printf`
- `setProgress`
- `setProgressDraw`
- `setVisible`
- `tick`

### ClDevFont (16 members)

- `beginDraw`
- `draw`
- `endDraw`
- `getColor`
- `getDisplayHeight`
- `getDisplayWidth`
- `getHeight`
- `getLastCharacterX`
- `getLastCharacterY`
- `getWidth`
- `initialize`
- `loadType`
- `printf`
- `purge`
- `setType`
- `tick`

### ClDeviceMgrPS2 (33 members)

- `__ct`
- `__dt`
- `__vt`
- `clearPrimaryController`
- `detectControllerLoss`
- `displayLostControllerMsg`
- `getDevice`
- `getDeviceHandle`
- `getDevicePort`
- `getDeviceSlot`
- `getFirstAvailableDevice`
- `getFirstAvailableNotInUse`
- `getGamePad`
- `getNumSupportedDevices`
- `getPrimaryController`
- `getPrimaryPort`
- `handleState`
- `havePrimaryController`
- `initGamePads`
- `initPadSettings`
- `initialize`
- `isAnyAttached`
- `isControllerLost`
- `isInitialized`
- `isValidDeviceIndex`
- `setPrimaryDevice`
- `setPrimaryToFirstActive`
- `setPrimaryToFirstAvailable`
- `stopAllMotors`
- `terminate`
- `updateControllerLoss`
- `updateDevices`
- `updateGamePads`

### ClDevicePs2GamePad (37 members)

- `__ct`
- `__dt`
- `__vt`
- `close`
- `debounceAll`
- `getButtonDeadZone`
- `getHandle`
- `getMaximumButtonValue`
- `getMaximumRumbleValue`
- `getMaximumStickValue`
- `getMinimumButtonValue`
- `getMinimumStickValue`
- `getNormalizedXStickValue`
- `getNormalizedYStickValue`
- `getPort`
- `getSlot`
- `getState`
- `getStickDeadZone`
- `getXStickValue`
- `getYStickValue`
- `isAnyActive`
- `isAnyButtonActive`
- `isConnected`
- `isInitialized`
- `isRumbleEnabled`
- `isValidPortNumber`
- `m_PadData`
- `open`
- `poll`
- `pollState`
- `setAnalogMode`
- `setButtonDeadZone`
- `setIsInitialized`
- `setPort`
- `setRumble`
- `setSlot`
- `setStickDeadZone`

### ClDifficultyDB (6 members)

- `getDifficultyRecord`
- `load`
- `setDifficultyRecord`
- `smpCurrDifficultyRecord`
- `smpDifficultyRecords`
- `smpHeader`

### ClDmaBuffer (7 members)

- `__vt`
- `dmaChannel`
- `initialize`
- `reallocateBuffers`
- `reallocateBuffersFmv`
- `reallocateBuffersMaximal`
- `reallocateBuffersMinimal`

### ClDonutModule (19 members)

- `__ct`
- `__vt`
- `cutTo`
- `draw`
- `getAngFromTangent`
- `getDesiredPitch`
- `getDesiredTargetLead`
- `getFollowJump`
- `getFov`
- `getHeightOffset`
- `getName`
- `getPitchRange`
- `getPosition`
- `getRadius`
- `getRotation`
- `getSectorIndex`
- `getViewTargetLerpSpeed`
- `getYawLimit`
- `solveConstraints`

### ClDoubleTreadModule (11 members)

- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getDuration`
- `getFov`
- `getIsTimed`
- `getName`
- `getSectorFromParameter`
- `getSectorIndex`
- `solveConstraints`

### ClDraw2D (26 members)

- `beginFan`
- `beginStrip`
- `beginTexturedFan`
- `beginTexturedSpriteChain`
- `beginTexturedStrip`
- `box`
- `boxLine`
- `boxNoSafe`
- `endFan`
- `endStrip`
- `endTexturedFan`
- `endTexturedSpriteChain`
- `endTexturedStrip`
- `fanVertex`
- `gradientBox`
- `gradientBoxLeftRight`
- `initialize`
- `line`
- `setDefaultScissor`
- `setScissor`
- `stripVertex`
- `texturedFanVertex`
- `texturedQuad`
- `texturedSprite`
- `texturedSpriteChain`
- `texturedStripVertex`

### ClDrawManager (11 members)

- `__ct`
- `__vt`
- `addAttribute`
- `allocateFromPool`
- `initializePool`
- `process`
- `releaseToPool`
- `removeAttribute`
- `reset`
- `smManager`
- `smpCurCamera`

### ClDrawPrim (7 members)

- `createBuffer`
- `drawPrim`
- `initialize`
- `setDrawMatrix`
- `setStaticData`
- `setStqMatrix`
- `uploadMicrocode`

### ClDrizztObj (19 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `fellOutOfWorld`
- `getIdleAnim`
- `getPlayerID`
- `getProjectileSource`
- `holdProjectiles`
- `initialize`
- `msRTTI`
- `notifyReflectionStateChange`
- `registerScriptMethods`
- `sauInitializeHairSim`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setWeapon`
- `tickAction`

### ClDynamicLightRendererPS2 (6 members)

- `Set16BitMode`
- `getDynamicLightTexture`
- `initialize`
- `queueData`
- `renderQueuedData`
- `setCamera`

### ClEnchantSpell (7 members)

- `__ct`
- `__vt`
- `draw`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClEncounterData (70 members)

- `boss`
- `clearEncounterTargets`
- `clearTrainFlag`
- `gatherBossData`
- `gatherCurrentPlayerEnemyCount`
- `gatherHealth`
- `gatherIsInCombat`
- `gatherKillCount`
- `gatherRelativeHealth`
- `getNearbyEnemyCount`
- `getNextPlayerIndex`
- `givePlayerProjectile`
- `helpCurrentPlayer`
- `initText`
- `initTrain`
- `killRunningMonitors`
- `meleeHelpCurrentPlayer`
- `monitor`
- `monitorBlock`
- `monitorSuper`
- `reEnableTrain`
- `registerScriptWrappers`
- `reset`
- `rogue`
- `rogueSeekShadow`
- `sauEncounterBlock`
- `sauEncounterBossInputResponse`
- `sauEncounterCoupDeGrace`
- `sauEncounterKnockdown`
- `sauEncounterRangedChargedFire`
- `sauEncounterRangedFire`
- `sauEncounterRogueSeekShadow`
- `sauEncounterSpecialRogue`
- `sauEncounterSpecialSorcererDetonate`
- `sauEncounterSpecialSorcererDrop`
- `sauEncounterSpecialWarrior`
- `sauEncounterSuperAttack`
- `sauEncounterTeamSuperAttack`
- `sauEncounterTrainOff`
- `sauEncounterTrainOn`
- `sauMonitorSituations`
- `seekHealth`
- `setFreeze`
- `setTrainFlag`
- `sorcerer`
- `sorcererCharged`
- `sorcererHelpCurrentPlayer`
- `sorcererProtect`
- `sorcererSleep`
- `tick`
- `train`
- `trainBlock`
- `trainCdg`
- `trainHeroMeter`
- `trainRanged`
- `trainRangedCharged`
- `trainReset`
- `trainSotf`
- `trainSpecialRogue`
- `trainSpecialSorcerer`
- `trainSpecialWarrior`
- `trainStop`
- `trainSuper`
- `trainTeamHelp`
- `trainTeamSuper`
- `trainText`
- `updateBossDamageHistory`
- `useKnockback`
- `warrior`
- `warriorProximity`

### ClEncounterManager (6 members)

- `__ct`
- `__vt`
- `forceEncounterUpdate`
- `isInvolved`
- `process`
- `smManager`

### ClEndOverProjectile (5 members)

- `__ct`
- `__vt`
- `deflect`
- `deflectTail`
- `orientMissileBody`

### ClEnemyDB (5 members)

- `getEnemyRecord`
- `load`
- `postLoadUpdate`
- `smpEnemyRecords`
- `smpHeader`

### ClExplodeAttribManager (8 members)

- `__ct`
- `__vt`
- `getFirstAttribute`
- `initialize`
- `removeAll`
- `removeAttribute`
- `reset`
- `smManager`

### ClExplosionManager (11 members)

- `addToFreePool`
- `destroyExplosion`
- `initialize`
- `releaseExplosion`
- `requestExplosion`
- `reset`
- `smElapsedTime`
- `smExplosionList`
- `smExplosionPool`
- `smNumExplosions`
- `tick`

### ClFMVDeux (42 members)

- `alignPointer`
- `allocate`
- `checkAbort`
- `draw`
- `fillMPEGDataBuffer`
- `initialize`
- `playModal`
- `queueForPlayModal`
- `scmpCaptionText`
- `setCaption`
- `setup`
- `shutdown`
- `smAbortPlayback`
- `smAudioSegmentHandle`
- `smCaptionFlashAlpha`
- `smCaptionFlashCycle`
- `smCaptionFontType`
- `smElapsedTimeInSec`
- `smFMVMemorySize`
- `smIsPlaying`
- `smIsSetup`
- `smLastElapsedTime`
- `smMPEGBufferSize`
- `smPlaybackType`
- `smQueuedClearScreenAfter`
- `smQueuedSkipType`
- `smRGBBlocks`
- `smVBlankRequests`
- `smpAlignedChunkBuffer`
- `smpBuffer`
- `smpFMVMemory`
- `smpFMVTexture`
- `smpMPEGDataBuffer`
- `smpQueuedFilename`
- `smpQueuedSubtitleAsset`
- `smpReserveBuffer`
- `startPlayback`
- `tempCloseStream`
- `tempOpenStream`
- `tempUpdateStream`
- `tick`
- `tickFlashCycle`

### ClFMVDeuxDecode (9 members)

- `backgroundCallback`
- `errorCallback`
- `isMPEGEnd`
- `noDataCallback`
- `setup`
- `shutdown`
- `smMPEG`
- `smWasBufferUnderrun`
- `tick`

### ClFMVDeuxGraphics (10 members)

- `blitMpegToGSBackBuffer`
- `draw`
- `drawFullscreenFMV`
- `drawTextureFMV`
- `fast_memmove`
- `restoreState`
- `setup`
- `setupPackets`
- `shutdown`
- `smOldIssueMode`

### ClFMVDeuxMPEGBuffer (13 members)

- `addBlock`
- `canAddBlock`
- `canGetBlock`
- `findNextChunkStart`
- `getBlock`
- `getContiguousDataSize`
- `getContiguousFreeSize`
- `getNextAddr`
- `getNextFrameSize`
- `initialize`
- `reset`
- `setMPEGBuffer`
- `validate`

### ClFader (6 members)

- `__ct`
- `draw`
- `getFactor`
- `isFadingOut`
- `setColor`
- `tick`

### ClFile (36 members)

- `abortLoad`
- `beginGetStream`
- `close`
- `closeStream`
- `devDrawLeds`
- `devInitialize`
- `enableLoadThrottle`
- `endGetStream`
- `getFlags`
- `getHostRootPrefix`
- `getQueueLoadFilename`
- `getQueueLoadProgress`
- `getSize`
- `getStatus`
- `getStream`
- `getStreamBufferCount`
- `getStreamStatus`
- `initialize`
- `load`
- `loadEeSpuPs2`
- `open`
- `openStream`
- `read`
- `reload`
- `reset`
- `resetHardware`
- `setLoadThrottle`
- `setRoot`
- `smDiscIsDVD`
- `smUsingATHostIO`
- `smUsingDisc`
- `smUsingT10000`
- `stopLoad`
- `sync`
- `tick`
- `unread`

### ClFileData (6 members)

- `allocateQueueNode`
- `allocateStreamNode`
- `freeQueueNode`
- `freeStreamNode`
- `getIopVersion`
- `initializeIop`

### ClFog (14 members)

- `computeTable`
- `getColor`
- `initialize`
- `render`
- `setColor`
- `setDensity`
- `setEnable`
- `setEnd`
- `setFunction`
- `setStart`
- `setState`
- `tick`
- `update`
- `updateParams`

### ClFollowModule (7 members)

- `__ct`
- `__vt`
- `cutTo`
- `draw`
- `getName`
- `getSectorIndex`
- `solveConstraints`

### ClFont (12 members)

- `addText`
- `clearText`
- `draw`
- `getLineWidth`
- `getTypeHeight`
- `initialize`
- `initializeType`
- `loadTexture`
- `reset`
- `setType`
- `smData`
- `unloadTexture`

### ClFontType (6 members)

- `getCharacterDescription`
- `getSection`
- `initialize`
- `loadTexture`
- `setTexture`
- `unloadTexture`

### ClForceManager (17 members)

- `addFrameForceApplier`
- `clearPerFrameForces`
- `getForceForControlPoint`
- `initialize`
- `removeForcesOnPoint`
- `smaFrameForcePool`
- `smaRigidityForcePool`
- `smaRootForcePool`
- `smpActiveFrameForceRoot`
- `smpActiveFrameForceTail`
- `smpActiveRigidityForceRoot`
- `smpActiveRigidityForceTail`
- `smpActiveRootForceRoot`
- `smpActiveRootForceTail`
- `smpInactiveFrameForceRoot`
- `smpInactiveRigidityForceRoot`
- `smpInactiveRootForceRoot`

### ClFrustum (9 members)

- `calculateOrthoViews`
- `calculatePlanes`
- `clip`
- `clipEdge`
- `initialize`
- `intersection`
- `isBoundingBoxVisible`
- `isSphereVisible`
- `tick`

### ClFullScreenShimmer (7 members)

- `enable`
- `initialize`
- `postPhase`
- `prePhase`
- `setAmplitude`
- `setDelay`
- `tick`

### ClGame (5 members)

- `__dt`
- `getModeData`
- `initialize`
- `mExecutableName`
- `tick`

### ClGameCamera (29 members)

- `__ct`
- `activateCamera`
- `activateForBard`
- `addEffect`
- `applyEffects`
- `debugDraw`
- `getFov`
- `getPosition`
- `hide`
- `initViewport`
- `initialize`
- `isShowing`
- `pushModule`
- `removeAllEffects`
- `removeEffect`
- `resumeFromBard`
- `saveCurrentCamera`
- `setFarPlane`
- `setFogState`
- `setInputPad`
- `setSubject`
- `setupProjection`
- `show`
- `tick`
- `tickDebug`
- `tickModule`
- `tickTransition`
- `updateSectorIndex`
- `xformGlobalToScreen`

### ClGameConfigProject (45 members)

- `__vt`
- `getControllerPort`
- `getDateFormat`
- `getDifficulty`
- `getGameState`
- `getGameType`
- `getIsIngame`
- `getLanguage`
- `getLanguageLevel`
- `getMasterVolume`
- `getMaxNumberOfPlayers`
- `getMusicVolume`
- `getNumPlayers`
- `getNumPlayersPerPad`
- `getNumSavedVillagers`
- `getRespawnId`
- `getSoundEffectsVolume`
- `getSpeakerMode`
- `getSubtitles`
- `getTimeFormat`
- `getVibration`
- `getVoiceVolume`
- `initialize`
- `registerScriptMethods`
- `setCheatsMask`
- `setControllerPort`
- `setDateFormat`
- `setGameType`
- `setIsInGame`
- `setLanguage`
- `setLanguageLevel`
- `setMasterVolume`
- `setMusicVolume`
- `setNumPlayers`
- `setNumPlayersPerPad`
- `setNumSavedVillagers`
- `setRespawnId`
- `setSoundEffectsVolume`
- `setSpeakerMode`
- `setSubtitles`
- `setTimeFormat`
- `setVibration`
- `setVoiceVolume`
- `smGameConfig`
- `smInterface`

### ClGameEffects (6 members)

- `forceEnd`
- `initialize`
- `silverSwordDeath`
- `teamAttackEnd`
- `teamAttackStart`
- `tick`

### ClGameModeBoot (22 members)

- `__dt`
- `__vt`
- `createMemcardMessage`
- `drawLegal`
- `drawMemoryCardCheck`
- `drawTextBlock`
- `drawTextureAsset`
- `enter`
- `exit`
- `initialize`
- `languageLevelSelectStart`
- `languageSelectStart`
- `loadWad`
- `memoryCardCheckStart`
- `resetMemcardMenu`
- `tick`
- `tickLanguageLevelSelect`
- `tickLanguageSelect`
- `tickLegal`
- `tickMemoryCardCheck`
- `validateMemCard`
- `validateSlot`

### ClGameModeInitialize (6 members)

- `__dt`
- `__vt`
- `enter`
- `exit`
- `initialize`
- `tick`

### ClGameModePlay (34 members)

- `__dt`
- `__vt`
- `drawControllerLossMenu`
- `drawDeadMenu`
- `drawOptionsDialogBox`
- `drawPauseMenu`
- `drawSkillList`
- `enter`
- `exit`
- `initialize`
- `isPaused`
- `loadInit`
- `loadWad`
- `pause`
- `pauseInGameAudio`
- `postLoadInit`
- `preLoadInit`
- `setupAskMenu`
- `setupControllerLossState`
- `setupDeadMenu`
- `setupInputRecorder`
- `setupSkillList`
- `setupUI`
- `tick`
- `tickCommon`
- `tickControllerLossMenu`
- `tickDeadMenu`
- `tickExit`
- `tickInputRecorder`
- `tickOptionsDialogBox`
- `tickPauseMenu`
- `tickPlaying`
- `tickSkillList`
- `unload`

### ClGameModeShell (12 members)

- `__dt`
- `__vt`
- `drawShellMode`
- `enter`
- `exit`
- `initialize`
- `reset`
- `setup`
- `tick`
- `tickActive`
- `tickDemo`
- `tickShellMode`

### ClGameRta (21 members)

- `callbackActionPlayerPlayCuePhoenix`
- `callbackAliveInputHealth`
- `callbackAliveInputQuestFlag`
- `callbackAlivePlayerHealthPhoenix`
- `callbackResetInputHealth`
- `callbackResetInputQuestFlag`
- `callbackResetIsPlayerPhoenix`
- `callbackResetPlayerHealthPhoenix`
- `callbackTestCombatStatus`
- `callbackTestIdealPlayer`
- `callbackTestInputHealth`
- `callbackTestInputQuestFlag`
- `callbackTestIsPlayerPhoenix`
- `callbackTestPlayerHealthPhoenix`
- `initialize`
- `load`
- `testCombatStatus`
- `testInputHealth`
- `testInputQuestFlag`
- `testIsPlayerPhoenix`
- `testPlayerHealthPhoenix`

### ClGameUI (43 members)

- `calculateSafeCoords`
- `drawFader`
- `drawHud`
- `drawLetterBox`
- `drawScriptFader`
- `drawTrainingFreeze`
- `initialize`
- `msDrawHUD`
- `msDrawPlayerHUD`
- `msInGameFader`
- `mscLetterBoxMoveTime`
- `registerScriptWrappers`
- `sauCreateCircleMeterControl`
- `sauCreateMeterControl`
- `sauCreateRingMeterControl`
- `sauCreateTextControl`
- `sauCreateTextureControl`
- `sauDrawNumber`
- `sauDrawNumberOutOfNumber`
- `sauEnableControl`
- `sauFreeControl`
- `sauGetControlPosition`
- `sauMessageBoxAllocate`
- `sauMessageBoxFree`
- `sauMessageBoxOff`
- `sauMessageBoxOn`
- `sauMessageBoxRelease`
- `sauOffsetControlPosition`
- `sauPulseColor`
- `sauPulseControl`
- `sauSetControlColor`
- `sauSetDrawPlayerHUD`
- `sauSetMeterValue`
- `sauSetPulseSettings`
- `sauSetRoundMeterValue`
- `setScreenEnable`
- `setTrainingFreeze`
- `smNumControls`
- `smScriptFader`
- `smaControls`
- `tick`
- `turnOffLetterBox`
- `turnOnLetterBox`

### ClGenericSimulation (7 members)

- `__ct`
- `__vt`
- `cut`
- `draw`
- `initialize`
- `postTick`
- `tick`

### ClGrass (12 members)

- `CB`
- `geomCB`
- `geomPostOpFn`
- `geomPostPhase`
- `geomPreOpFn`
- `geomPrePhase`
- `initialize`
- `postOpFn`
- `postPhase`
- `preOpFn`
- `prePhase`
- `tick`

### ClHeatHaze (8 members)

- `addEffect`
- `cycle`
- `draw`
- `drawEffect`
- `initialize`
- `postPhase`
- `prePhase`
- `tick`

### ClHeldProjectileObj (8 members)

- `__ct`
- `__vt`
- `draw`
- `hide`
- `hold`
- `initialize`
- `msRTTI`
- `setRelativeMatrix`

### ClInputRecorder (13 members)

- `close`
- `getCurrentDelta`
- `incrementFrame`
- `initialize`
- `loadFrame`
- `mode`
- `open`
- `pause`
- `resume`
- `saveFrame`
- `setCurrentDelta`
- `smPaused`
- `smRecordMode`

### ClInputs (5 members)

- `clearInputs`
- `getInputNameByIndex`
- `setInput`
- `setup`
- `testInput`

### ClInstancedCharacterManager (9 members)

- `activateInstance`
- `addInstance`
- `initialize`
- `setInstanceSector`
- `smInstanceCount`
- `smSkeletonRecordCount`
- `smaInstanceRecords`
- `smaSkeletonRecords`
- `tick`

### ClInstancedCharacterObj (12 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `draw`
- `getFigure`
- `initializeAttributes`
- `msRTTI`
- `removeAllAttributesAndServices`
- `reset`
- `setAssetContainer`
- `setSkeleton`

### ClIronGolemObj (7 members)

- `__ct`
- `__vt`
- `activate`
- `handleAnimTrigger`
- `initialize`
- `msRTTI`
- `registerScriptMethods`

### ClLava (6 members)

- `initialize`
- `lavaCB`
- `lavaPostOpFn`
- `lavaPreOpFn`
- `postLavaPhase`
- `preLavaPhase`

### ClLevelData (10 members)

- `beginDraw3d`
- `disableLoadConsole`
- `enableLoadConsole`
- `endDraw3d`
- `loadCostumeWad`
- `loadMissileWad`
- `loadWad`
- `loadWeaponWad`
- `stabilize`
- `verifyMemoryMap`

### ClLevelState (34 members)

- `addExperience`
- `addGold`
- `addItem`
- `getAdjustedExperience`
- `getAdjustedGold`
- `getBaseFilename`
- `getExperience`
- `getFilename`
- `getFinished`
- `getGold`
- `getKillCount`
- `getNameStringID`
- `getNextLevel`
- `getPlayed`
- `getPreviousExperience`
- `getPreviousGold`
- `incrementKillCount`
- `initialize`
- `isPlayable`
- `popItem`
- `setBaseFilename`
- `setEnemySpawnCount`
- `setExperience`
- `setFinished`
- `setGold`
- `setGrade`
- `setKillCount`
- `setNameStringID`
- `setNextLevel`
- `setPlayTime`
- `setPlayable`
- `setPlayed`
- `setPreviousExperience`
- `setPreviousGold`

### ClLightning (7 members)

- `enable`
- `initialize`
- `postPhase`
- `setColor`
- `setDuration`
- `setIntensity`
- `setType`

### ClLightningSpell (6 members)

- `__ct`
- `__vt`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClLinkedAnimDB (9 members)

- `buildLookupTable`
- `getLinkedAnimRecord`
- `load`
- `parseArray`
- `smEnemyDBIDTable`
- `smNumEnemyDBIDs`
- `smpHeader`
- `smpLinkedAnimRecords`
- `smpLookupTable`

### ClLinkedList (8 members)

- `addAtHead`
- `addAtTail`
- `addBefore`
- `countElements`
- `findElement`
- `removeElement`
- `removeFirstElement`
- `removeLastElement`

### ClLockPickGameObj (18 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `disrupt`
- `draw`
- `initialize`
- `initializeAttributes`
- `isSolved`
- `mKeys`
- `msRTTI`
- `randRange`
- `registerScriptMethods`
- `sauLockPickInit`
- `solve`
- `stopRumble`
- `tick`
- `tickInput`

### ClLookAtModule (9 members)

- `__vt`
- `cutTo`
- `draw`
- `getFov`
- `getName`
- `getPosition`
- `getSectorIndex`
- `getTarget`
- `solveConstraints`

### ClMagicMissileSpell (6 members)

- `__ct`
- `__vt`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClMagicalAttackTrail (8 members)

- `CB`
- `draw`
- `initialize`
- `postOp`
- `postPhase`
- `preOp`
- `prePhase`
- `tick`

### ClMathUtil (9 members)

- `angFromHereToThere`
- `computeHeading`
- `findOrbitPoint`
- `interpolateTowards`
- `rand`
- `randf`
- `srand`
- `srandf`
- `youInFrontOfMe`

### ClMatrix (29 members)

- `__ct`
- `__ml`
- `__pl`
- `fastInverse`
- `fastRotate`
- `getEulerAngles`
- `getEulerAnglesFast`
- `inverse`
- `loadIdentity`
- `lookAtRH`
- `multMatrix`
- `multMatrixLocal`
- `orthonormalize`
- `perspectiveFovLH`
- `rotate`
- `rotateAxis`
- `rotateAxisLocal`
- `rotateLocal`
- `rotateX`
- `rotateY`
- `rotateZ`
- `rotateZLocal`
- `scale`
- `scaleLocal`
- `setAxes`
- `transformCoord`
- `translate`
- `translateLocal`
- `transpose`

### ClMegaSpiderCaveObj (7 members)

- `__ct`
- `__vt`
- `getDirection`
- `msRTTI`
- `registerScriptMethods`
- `setDirection`
- `tickCollision`

### ClMemory (13 members)

- `allocate`
- `changeHeapMemory`
- `getFreeSize`
- `initialize`
- `lock`
- `permanentAllocate`
- `permanentLock`
- `permanentRestore`
- `permanentSave`
- `permanentUnlock`
- `reset`
- `setTempAllocator`
- `unlock`

### ClMerrshaulkObj (11 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `isTargetable`
- `msRTTI`
- `registerScriptMethods`
- `sauSetEatObject`
- `sauSetHunger`
- `sauSetShootChance`
- `tickCollision`

### ClMeshSimulation (13 members)

- `__ct`
- `__vt`
- `cut`
- `deactivate`
- `draw`
- `getNthControlPoint`
- `initialize`
- `initializeShader`
- `postTick`
- `renderBaseCB`
- `renderSpecCB`
- `setRippleAxis`
- `tick`

### ClMessageBox (8 members)

- `allocate`
- `draw`
- `free`
- `initialize`
- `off`
- `on`
- `release`
- `tick`

### ClMeteorShowerSpell (7 members)

- `__ct`
- `__vt`
- `draw`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClMineObj (9 members)

- `__ct`
- `__vt`
- `arm`
- `detonate`
- `initialize`
- `initializeAttributes`
- `isArmed`
- `msRTTI`
- `tick`

### ClMiniGameManager (7 members)

- `disrupt`
- `initialize`
- `m_eType`
- `m_pLockPickGame`
- `registerScriptMethods`
- `tick`
- `updateInput`

### ClMithrilFlameObj (13 members)

- `__ct`
- `__vt`
- `activate`
- `addToActiveMithrilFlameObjList`
- `deactivate`
- `getClosestActiveMithrilFlameObj`
- `getRadius`
- `msRTTI`
- `registerScriptMethods`
- `removeFromActiveMithrilFlameObjList`
- `smpActiveMithrilFlameObjRoot`
- `staticInitialize`
- `staticReset`

### ClMixer (6 members)

- `ComputeMatrices`
- `ConfigureMixerJumpTable`
- `PostComputeMatrices`
- `SetLevelOfDetail`
- `__ct`
- `tick`

### ClMixerInputHeadTrack (9 members)

- `GetBoneJumpTableEntry`
- `IsValid`
- `StartAnimation`
- `UpdateBlending`
- `UpdateTime`
- `__ct`
- `__vt`
- `canDoHeadTracking`
- `updateHeadPosition`

### ClMixerInputKeyframe (11 members)

- `AnimationCompletedThisFrame`
- `CalculateRootBoneTranslation`
- `GetBoneJumpTableEntry`
- `SampleRootBoneTranslation`
- `SetAnimationTime`
- `StartAnimation`
- `StartBlending`
- `StartReverseBlending`
- `UpdateBlending`
- `UpdateTime`
- `__vt`

### ClMixerInputLipLock (5 members)

- `GetBoneJumpTableEntry`
- `IsValid`
- `UpdateBlending`
- `UpdateTime`
- `__vt`

### ClMorpher (12 members)

- `blendAnimation`
- `blendBardAnimation`
- `getMorphMeshCache`
- `getMorphTargetData`
- `isCustomAnimPlaying`
- `resetRawTargets`
- `setRawTarget`
- `startAnimation`
- `tick`
- `update`
- `updateBlending`
- `updateTime`

### ClMultiLightningSpell (6 members)

- `__ct`
- `__vt`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClNavManager (7 members)

- `getMetrics`
- `getNavHeading`
- `getNavMeshFromID`
- `initialize`
- `isLoaded`
- `meshesAreAdjacent`
- `setup`

### ClNavMesh (9 members)

- `encloses`
- `getHeadingToTri`
- `getNavHeading`
- `getTriCenter`
- `getTriToTriHeading`
- `inTriangle`
- `initialize`
- `isOnMesh`
- `setup`

### ClNoamFigure (9 members)

- `__ct`
- `__vt`
- `getAnimTime`
- `getCurAnimId`
- `getPrimaryAnim`
- `getSecondaryAnim`
- `init`
- `setModulationColor`
- `update`

### ClNoamFigurePs2 (25 members)

- `__vt`
- `activateHighResHead`
- `getLevelOfDetail`
- `initialize`
- `isGating`
- `isNoamCharacterVisible`
- `renderAdditiveTranslucentShaderCB`
- `renderDamageShaderCB`
- `renderDeferredPasses`
- `renderDiffuse`
- `renderDiffuseInstanced`
- `renderDiffuseShaderCB`
- `renderDisintegrating`
- `renderEnvmapShaderCB`
- `renderSelfIllumShaderCB`
- `renderShadowShaderCB`
- `renderSpecularShaderCB`
- `resetDeferredPassQueue`
- `setAlphaReferenceValue`
- `setClipAndLOD`
- `setClipAndLOD_Shadow`
- `setLevelOfDetail`
- `smDeltaTime`
- `smTime`
- `tick`

### ClNoamPropObj (18 members)

- `__ct`
- `__vt`
- `activate`
- `draw`
- `handleAnimTrigger`
- `handleMessage`
- `handleStruckAndDestroyedProp`
- `msRTTI`
- `registerScriptMethods`
- `reset`
- `sauFinishAnim`
- `sauIsPlayingAnim`
- `sauNoamPropInit`
- `sauSetAnim`
- `setAnim`
- `setAssetContainer`
- `tickAction`
- `tickBuild`

### ClNoamPs2UcodeInterface (20 members)

- `computeMatrices`
- `end`
- `initialize`
- `renderShadowVolume`
- `resetPerModelState`
- `setAlphaReference`
- `setAmbientLight`
- `setBoneMatrices`
- `setClipFlagsAndLOD`
- `setDualPassGsAndTexState`
- `setGsAndTexStates`
- `setGsAndTexStatesEnvmap`
- `setMatrices`
- `setSelfIllumCol`
- `setShadowLight`
- `setShadowVolumeMatrices`
- `setSneakCol`
- `setState`
- `setViewMatrix`
- `tick`

### ClNodeObjectList (5 members)

- `getNodeByID`
- `initialize`
- `mObjectPool`
- `mObjectsInUse`
- `mpFreeObjectRoot`

### ClObjectiveObj (23 members)

- `__ct`
- `__vt`
- `addNextObjective`
- `getNextObjective`
- `msRTTI`
- `registerScriptMethods`
- `reset`
- `sauAddNext`
- `sauAttach`
- `sauInitCrouch`
- `sauInitEvadeDragon`
- `sauInitJumpA`
- `sauInitJumpB`
- `sauInitJumpTo`
- `sauInitRingBell`
- `sauInitRunTo`
- `sauInitShoot`
- `sauInitSidestep`
- `sauInitTaunt`
- `sauInitTeleportTo`
- `sauInitWait`
- `sauInitWalkTo`
- `sauSetChance`

### ClOptionsDialogBox (5 members)

- `draw`
- `getFadeAlpha`
- `initialize`
- `tick`
- `turnOn`

### ClOrcKingObj (6 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `msRTTI`
- `registerScriptMethods`
- `sleep`

### ClParser (7 members)

- `__ct`
- `__dt`
- `__vt`
- `initialize`
- `matchReservedWord`
- `parseNextToken`
- `setErrorNumber`

### ClParticleObj (19 members)

- `__ct`
- `__vt`
- `createParticleSystem`
- `destroyParticleSystem`
- `draw`
- `hardKill`
- `initializeAttributes`
- `isActive`
- `isSystemDead`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `setMatrix`
- `setPosFollowsSpawn`
- `setPosition`
- `setTarget`
- `setTargetObj`
- `softKill`
- `tick`

### ClParticlePlacementObj (12 members)

- `__ct`
- `__vt`
- `msRTTI`
- `registerScriptMethods`
- `sauCreateFixedSystem`
- `sauCreateSystem`
- `sauHardKill`
- `sauSoftKill`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setSectorIndex`

### ClPathModule (19 members)

- `__ct`
- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getDesiredPitch`
- `getDesiredTargetLead`
- `getFollowJump`
- `getFov`
- `getMaxFollowDistance`
- `getMinFollowDistance`
- `getName`
- `getPitchRange`
- `getSectorIndex`
- `getStayBackLerpSpeed`
- `getStayCloseLerpSpeed`
- `getUseCombatFraming`
- `getViewTargetLerpSpeed`
- `solveConstraints`

### ClPbi (23 members)

- `blit`
- `clear`
- `copy`
- `copyByPage`
- `createInertHeader`
- `createPaletteHeader`
- `getLinearSample24`
- `getLinearSample32`
- `getLinearSample4`
- `getLinearSample8`
- `getPalette`
- `getSwizzledXy`
- `initialize`
- `lerpBlit`
- `modulateColorAndDoSrcAlphaTest`
- `modulateColorByAlpha`
- `move_A_to_BGR`
- `move_G_to_A`
- `reverse_BGR`
- `setAlphaFrom24BitTexture`
- `splitPaletteBlit`
- `tick`
- `validate`

### ClPerceptions (5 members)

- `__ct`
- `initialize`
- `setEnemyDetectionInputs`
- `setTargetRangeInputs`
- `tick`

### ClPfxMachine (19 members)

- `createAsbestos`
- `destroyAsbestos`
- `elementsFree`
- `emitElement`
- `emitGeometryElement`
- `initialize`
- `initializeSystem`
- `killElement`
- `patternTicked`
- `processAsbestos`
- `queuePattern`
- `renderQueuedParticles`
- `resetAsbestos`
- `setAsbestosCylinder`
- `setAsbestosPlane`
- `setAsbestosSphere`
- `systemDrawn`
- `systemTicked`
- `tick`

### ClPhysicsAttrib (6 members)

- `__ct`
- `init`
- `release`
- `setRigidBody`
- `setRigidBodyInertiaTensor`
- `setRigidBodyMass`

### ClPhysicsManager (14 members)

- `__ct`
- `__vt`
- `addAttribute`
- `allocRigidBody`
- `allocateFromPool`
- `freeRigidBody`
- `initialize`
- `initializePool`
- `process`
- `releaseToPool`
- `removeAll`
- `removeAttribute`
- `reset`
- `smManager`

### ClPickupManager (12 members)

- `addToFreePool`
- `createPickup`
- `destroyPickup`
- `evaluateRule`
- `initialize`
- `requestPickup`
- `reset`
- `smElapsedTime`
- `smNumPickups`
- `smPickupList`
- `smPickupPool`
- `tick`

### ClPickupObj (20 members)

- `__ct`
- `__vt`
- `applyPickup`
- `draw`
- `fadeOut`
- `getNavFailureForChar`
- `handleMessage`
- `initializeAttributes`
- `msRTTI`
- `release`
- `removeAllAttributesAndServices`
- `setMatrix`
- `setNavFailureForChar`
- `setNotificationObject`
- `setOverrideTime`
- `setPosition`
- `setRotation`
- `setup`
- `tickCollision`
- `tickFinal`

### ClPlaneBossModule (17 members)

- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getBoss`
- `getBossHeightOffset`
- `getDesiredHeight`
- `getDesiredPitch`
- `getFollowJump`
- `getFov`
- `getLookAtPlayer`
- `getMaxFollowDistance`
- `getName`
- `getPitchRange`
- `getSectorIndex`
- `getViewTargetSLerpSpeed`
- `solveConstraints`

### ClPlaneModule (22 members)

- `__ct`
- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getDesiredPitch`
- `getDesiredTargetLead`
- `getFollowJump`
- `getFov`
- `getIsDirectional`
- `getMaxFollowDistance`
- `getMinFollowDistance`
- `getName`
- `getPitchRange`
- `getSectorIndex`
- `getStayBackLerpSpeed`
- `getStayCloseLerpSpeed`
- `getUseCombatFraming`
- `getViewDirectionX`
- `getViewDirectionZ`
- `getViewTargetLerpSpeed`
- `solveConstraints`

### ClPlayerHUD (14 members)

- `draw`
- `drawAmmo`
- `drawHeroMeter`
- `flashHeroMeter`
- `flashValue`
- `initialize`
- `mFlashHeroMeter`
- `mMeterHeight`
- `mMeterPosX`
- `mMeterPosY`
- `mMeterValue`
- `mMeterWidth`
- `mVerticalBar`
- `queueAwardPoints`

### ClPlayerState (38 members)

- `addDefaultItems`
- `addDefaultSkills`
- `addExperience`
- `addGold`
- `addItem`
- `addSkill`
- `addUnspentExperience`
- `clearItems`
- `getExperience`
- `getGold`
- `getItem`
- `getItemCount`
- `getLevel`
- `getNextLevelExperience`
- `getProjectileCount`
- `getReplacedItem`
- `getSkill`
- `getSkillCount`
- `getTopArmor`
- `getTopWeapon`
- `getTotalGold`
- `getUnspentExperience`
- `getWeaponParticle`
- `hasDesignatedItem`
- `hasItem`
- `hasItemUpgrade`
- `hasSkill`
- `hasSkillUpgrade`
- `initialize`
- `removeItem`
- `setExperience`
- `setGold`
- `setLevel`
- `setProjectileCount`
- `setTotalGold`
- `setUnspentExperience`
- `subtractCurrentGold`
- `subtractUnspentExperience`

### ClPlayers (43 members)

- `addPlayer`
- `assignCurrentPlayers`
- `clearTeamHelpCalled`
- `configPadsAndPlayers`
- `getCurPlayer`
- `getCurPlayerID`
- `getCurPlayerObj`
- `getIsSwitchAllowed`
- `getNearestCurPlayer`
- `getNearestPlayer`
- `getNumPads`
- `getNumPlayersPerPad`
- `getPadNum`
- `getPlayer`
- `getPlayerDied`
- `getPlayerDying`
- `getPlayerID`
- `getPlayerObj`
- `getPlayerState`
- `getPlayerStats`
- `getPlayerViewport`
- `giveExperience`
- `giveGold`
- `initialize`
- `isCurPlayer`
- `isCurPlayerIdeal`
- `isPlayer`
- `postSuperMeterUpdate`
- `setAllowPlayerSwitching`
- `setAllowPlayerSwitchingTraining`
- `setIdealPlayer`
- `setPlayerDied`
- `setPlayerDying`
- `setSwitchToPlayerPermission`
- `setSwitchToPlayerPermissionTraining`
- `showPlayerCameras`
- `stopWatchingForPlayerSwitch`
- `substitutePlayer`
- `switchToPlayer`
- `tick`
- `updatePlayerStats`
- `wasTeamHelpCalled`
- `watchForPlayerSwitch`

### ClPointProjectile (10 members)

- `__ct`
- `__vt`
- `calculateTrajectory`
- `checkCollision`
- `deflect`
- `destroy`
- `getVelocity`
- `handleCollision`
- `strike`
- `updatePosition`

### ClPortalDrawManager (9 members)

- `addPortal`
- `getPortalDrawParams`
- `initialize`
- `mCurrentParamCount`
- `mTotalParamCount`
- `mpParamList`
- `setGoalRotationRate`
- `setGoalScaling`
- `tick`

### ClPortalRipple (9 members)

- `CB`
- `addRipple`
- `initialize`
- `postOpFn`
- `postPhase`
- `preOpFn`
- `prePhase`
- `setParams`
- `tick`

### ClPositionService (5 members)

- `__vt`
- `getSplinePos`
- `interpolate`
- `process`
- `updateSectorIndex`

### ClPrisonModule (13 members)

- `__vt`
- `cutTo`
- `draw`
- `getDesiredPitch`
- `getFollowJump`
- `getFov`
- `getName`
- `getOrientation`
- `getPitchRange`
- `getPosition`
- `getSectorIndex`
- `initialize`
- `solveConstraints`

### ClProcTexture (9 members)

- `addDroplet`
- `allocateAndReadHeightMap`
- `allocateHeightMap`
- `allocateHeightMapPSMT8H`
- `drawAllDroplets`
- `freeHeightMap`
- `initialize`
- `tick`
- `tickDroplets`

### ClProjectileElement (6 members)

- `getCreationTime`
- `getProjectileMemory`
- `getProjectileObject`
- `setCreationTime`
- `setProjectileMemory`
- `setProjectileObject`

### ClProjectileManager (10 members)

- `addToFreePool`
- `initialize`
- `releaseProjectile`
- `requestProjectile`
- `reset`
- `smActiveProjectiles`
- `smFreeProjectiles`
- `smNumFreeProjectiles`
- `smNumProjectiles`
- `tick`

### ClProjectileObj (26 members)

- `__ct`
- `__vt`
- `blowUp`
- `clearTargetObj`
- `deflect`
- `destroy`
- `detach`
- `draw`
- `getFirer`
- `getInaccuracy`
- `getLength`
- `goToPieces`
- `handleMessage`
- `initializeAttributes`
- `isSticky`
- `msRTTI`
- `orientMissileBody`
- `removeAllAttributesAndServices`
- `setMatrix`
- `setMissileAsset`
- `setOrientationFromVelocity`
- `setPosition`
- `setRotation`
- `setTimeLeft`
- `strike`
- `tick`

### ClPropDrawData (8 members)

- `GetPassPostOp`
- `GetPassPreOp`
- `RenderPropShadowCb`
- `correctPointers`
- `initialize`
- `smDeltaTime`
- `smTime`
- `tick`

### ClPropPieceManager (5 members)

- `__ct`
- `allocatePropPiece`
- `deallocatePropPiece`
- `initialize`
- `smManager`

### ClProtectSpell (7 members)

- `__ct`
- `__vt`
- `draw`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClRedDragonBarrierObj (5 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `setSectorIndex`

### ClRedDragonFireFieldObj (7 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `lower`
- `setSectorIndex`
- `tickCollision`

### ClRedDragonObj (39 members)

- `__ct`
- `__vt`
- `activate`
- `calculateChannel`
- `deactivate`
- `dispossess`
- `getBodyPart`
- `getGravity`
- `getHeadTargetPos`
- `getNumBodyParts`
- `getTarget`
- `handleMessage`
- `initialize`
- `isCharacterSeparationEnabled`
- `isCharacterWorldCollisionEnabled`
- `isTargetable`
- `makeTargetable`
- `msRTTI`
- `possess`
- `registerScriptMethods`
- `sauDisableFireField`
- `sauDisableHeadCharacterSeparation`
- `sauDisableWings`
- `sauEat`
- `sauEnableFireField`
- `sauEnableHeadCharacterSeparation`
- `sauGateIn`
- `sauGateOutEnd`
- `sauGateOutStart`
- `sauGetLinkedByRogue`
- `sauLowerFireField`
- `sauSetBossPhase`
- `sauSetEasySpawner`
- `sauSetHardSpawner`
- `sauTryToEat`
- `testFlameCollisions`
- `tickCollision`
- `tickCrashCollision`
- `tickFlameCollision`

### ClReverseTreadModule (13 members)

- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getDesiredHeight`
- `getFollowJump`
- `getFov`
- `getLookAtPlayer`
- `getMaxFollowDistance`
- `getName`
- `getSectorFromParameter`
- `getSectorIndex`
- `solveConstraints`

### ClRigidBody (21 members)

- `addForce`
- `addStaticContact`
- `applyImpulse`
- `clampForces`
- `clampMotion`
- `clearForces`
- `computeAuxiliaryQuantities`
- `getMatrix`
- `getPosition`
- `init`
- `pointVelocity`
- `setAngularDampingFactor`
- `setAngularVelocity`
- `setLinearDampingFactor`
- `setMatrix`
- `setPosition`
- `setVelocity`
- `simulate`
- `updateResting`
- `wallCollis`
- `wallCollisImpulse`

### ClRogueObj (33 members)

- `__ct`
- `__vt`
- `activate`
- `applyDamage`
- `deactivate`
- `dispossess`
- `fellOutOfWorld`
- `getIdleAnim`
- `getLinkedMoveType`
- `getPlayerID`
- `getProjectileSource`
- `getTargettingUpdateBaseTime`
- `getTargettingUpdateTimeVariance`
- `getWalkAnim`
- `handleMessage`
- `hasJumpTarget`
- `initialize`
- `isDisabled`
- `isTargetable`
- `msRTTI`
- `notifyReflectionStateChange`
- `possess`
- `registerScriptMethods`
- `sauBlockEvadeSuccess`
- `sauInitializeHairSim`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setSectorIndex`
- `setWeapon`
- `stopAllWeaponCollision`
- `stopAllWeaponTrails`
- `tickAction`

### ClRogueShadowObj (10 members)

- `__ct`
- `__vt`
- `activate`
- `addToActiveRogueShadowObjList`
- `getClosestActiveRogueShadowObj`
- `msRTTI`
- `registerScriptMethods`
- `smpActiveRogueShadowObjRoot`
- `staticInitialize`
- `staticReset`

### ClRta (8 members)

- `allocateSequence`
- `freeSequence`
- `getMaximumRtxCount`
- `initialize`
- `registerRtx`
- `registerRtxOpCallback`
- `reset`
- `tick`

### ClRtaRtxOpCallback (14 members)

- `actionDoNothing`
- `actionInputPlayCue`
- `actionOutputPlayCue`
- `actionTrigOutput`
- `aliveNoDie`
- `aliveRunOnce`
- `getCallback`
- `initialize`
- `reset`
- `resetAlwaysOn`
- `resetNeverReset`
- `resetTimer`
- `testAlwaysFalse`
- `testAlwaysTrue`

### ClRtaSequence (6 members)

- `initialize`
- `setNextTime`
- `stop`
- `tick`
- `tickReset`
- `tickRun`

### ClRumbleManager (6 members)

- `enable`
- `initialize`
- `reset`
- `stop`
- `tick`
- `vibrate`

### ClSaveDataProject (12 members)

- `getBuffer`
- `getCompletedLevel`
- `getDifficulty`
- `getManufacturerRequiredSaveSize`
- `getNumSaveSlots`
- `getSaveGameDataSize`
- `getSaveGameName`
- `getSaveTime`
- `getTotalSaveSize`
- `prepSaveData`
- `restoreData`
- `verifyLoadedData`

### ClSaveDevice (19 members)

- `dir`
- `doesIconExist`
- `doesIconSysExist`
- `fileExists`
- `format`
- `getFree`
- `getLastError`
- `getSizeOnDevice`
- `getStatus`
- `getType`
- `initialize`
- `isIdle`
- `openFile`
- `readFile`
- `scan`
- `setGameName`
- `setIconData`
- `tick`
- `writeFile`

### ClSaveLoad (5 members)

- `gameExists`
- `initialize`
- `isGameLoaded`
- `loadGame`
- `saveGame`

### ClScreenShot (6 members)

- `initialize`
- `msTakingVideo`
- `msVidCapEnabled`
- `msVidCapRenderRate`
- `startVideoCapture`
- `stopVideoCapture`

### ClScriptLink (8 members)

- `__ct`
- `getDelayTime`
- `getEventName`
- `getOneShotState`
- `getRefObject`
- `sendEvent`
- `setOneShotState`
- `setScriptData`

### ClScriptObj (15 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `handleMessage`
- `isActive`
- `msRTTI`
- `registerScriptMethods`
- `reset`
- `sauGetPosition`
- `sauGetRotation`
- `sauGetSector`
- `sauSetPosition`
- `sauSetRotation`
- `sauSetSector`

### ClSegmentLengthConstraint (5 members)

- `__vt`
- `affectsSimulationSubObject`
- `process`
- `setOpenParameterValueFloat`
- `setSegmentLengthParams`

### ClServiceManager (9 members)

- `addService`
- `allocateServiceMemory`
- `hasServiceOfType`
- `initialize`
- `removeMyServices`
- `removeService`
- `selfObjTickEnd`
- `selfObjTickStart`
- `tick`

### ClShaderConfigPS2 (24 members)

- `EnableSelfShadowing`
- `Initialize`
- `RegisterShader`
- `SetDoubleTexturePostOp`
- `SetDoubleTexturePreOp`
- `SetKValues`
- `SetPerPixelPlanarDot3TexturePreOp`
- `SetSingleTextureDecalPreOp`
- `SetSingleTextureHighlight2PreOp`
- `SetSingleTextureModulatePreOp`
- `SetSingleTexturePostOp`
- `SetSingleTexturePreOp`
- `SetTripleTextureModulatePreOp`
- `SetTripleTexturePostOp`
- `isLowResShadows`
- `isSelfShadowingEnabled`
- `mCharacterModulateFadeOut`
- `mCharacterModulateTimeLeft`
- `mCharacterModulateTimeTotal`
- `mCharacterModulateValue`
- `mNumTextures`
- `mTextureKBias`
- `maTextureK`
- `mpTextures`

### ClShaderTextureManager (13 members)

- `GetTexture`
- `RegisterTexture`
- `SetTexturePool`
- `UnRegisterTexture`
- `mLevelTextureCount`
- `mMaxConcurrentStreamingTextureCount`
- `mNonStreamingTextureCount`
- `mRegisteredTextureCount`
- `mpLookupTable`
- `mpTextureSectorMask`
- `mpTextureState`
- `mppTextureList`
- `tick`

### ClShadowVolume (5 members)

- `__ct`
- `calcFaceDirections`
- `renderShadowCaps`
- `renderShadowEdges`
- `skinVertices`

### ClShaftProjectile (14 members)

- `__ct`
- `__vt`
- `calculateTrajectory`
- `checkCollision`
- `deflect`
- `deflectTail`
- `destroy`
- `getVelocity`
- `handleCollision`
- `handleTailCollision`
- `orientMissileBody`
- `strike`
- `tick`
- `updatePosition`

### ClShellBackgroundCloud (10 members)

- `__ct`
- `fillPropInfo`
- `isTransitInDone`
- `isTransitOutDone`
- `nextValue`
- `randBetween`
- `reset`
- `tick`
- `transitBackward`
- `transitForward`

### ClShellForgroundGroup (10 members)

- `__ct`
- `hide`
- `mscAll`
- `mscNone`
- `pfx`
- `reset`
- `resetItems`
- `setupItems`
- `show`
- `tick`

### ClShellModeAutoBuy (32 members)

- `__ct`
- `__dt`
- `__vt`
- `buyItem`
- `buySkill`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `getAdjustedItemCost`
- `getItemStatus`
- `getSkillStatus`
- `initialize`
- `isIdle`
- `preTick`
- `reset`
- `saveState`
- `setScreenItemsAlpha`
- `setScreenPos`
- `setup`
- `setupCurser`
- `setupListing`
- `setupPopup`
- `setupScreenItems`
- `setupSelectionParts`
- `tick`
- `tickArrows`
- `tickBackground`
- `tickBuyPopup`
- `tickCharacter`
- `tickListing`
- `tickPopup`

### ClShellModeController (13 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`
- `tickAlpha`

### ClShellModeCredits (16 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `getAlphaByY`
- `getNextCredit`
- `initialize`
- `isIdle`
- `preTick`
- `reset`
- `setup`
- `tick`
- `tickNames`

### ClShellModeHUD (13 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`
- `tickAlpha`

### ClShellModeLevelEnd (17 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `drawMenu`
- `drawPortraits`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `setupAskMenu`
- `setupAskReplayMenu`
- `tick`
- `tickMenu`

### ClShellModeLevelEquipment (35 members)

- `__ct`
- `__dt`
- `__vt`
- `buyItem`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `getAdjustedItemCost`
- `getItemColor`
- `getItemStatus`
- `initialize`
- `isIdle`
- `preTick`
- `reset`
- `setScreenItemsAlpha`
- `setScreenPos`
- `setScreenShowAlpha`
- `setScreenUnifiedAlpha`
- `setup`
- `setupCurser`
- `setupListing`
- `setupNotice`
- `setupPopup`
- `setupScreenItems`
- `setupSelectionParts`
- `setupShow`
- `tick`
- `tickArrows`
- `tickBackground`
- `tickCharacter`
- `tickItemPopup`
- `tickListing`
- `tickPopup`
- `tickShow`

### ClShellModeLevelSelect (17 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isAudioByMenuPlaying`
- `isIdle`
- `playAudioByMenu`
- `preTick`
- `reset`
- `setup`
- `setupUnlockablePopup`
- `tick`
- `tickUnlockablePopup`

### ClShellModeLevelUp (36 members)

- `__ct`
- `__dt`
- `__vt`
- `buySkill`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `getSkillColor`
- `getSkillStatus`
- `initialize`
- `isIdle`
- `preTick`
- `reset`
- `scmaLevelList`
- `setScreenItemsAlpha`
- `setScreenPos`
- `setScreenShowAlpha`
- `setScreenUnifiedAlpha`
- `setup`
- `setupButtons`
- `setupCurser`
- `setupListing`
- `setupNotice`
- `setupPopup`
- `setupScreenItems`
- `setupSelectionParts`
- `setupShow`
- `tick`
- `tickArrows`
- `tickBackground`
- `tickCharacter`
- `tickListing`
- `tickPopup`
- `tickShow`
- `tickSkillPopup`

### ClShellModeLoadGame (19 members)

- `__ct`
- `__dt`
- `__vt`
- `dialogTransition`
- `draw2d`
- `draw3d`
- `drawMenu`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `prepareExit`
- `reset`
- `setup`
- `setupDialogMenu`
- `switchToGameSelect`
- `tick`
- `tickState`
- `updateDialog`

### ClShellModeMainMenu (13 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`
- `tickDev`

### ClShellModeNewGame (12 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`

### ClShellModeOptions (13 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`
- `tickRing`

### ClShellModeSaveGame (19 members)

- `__ct`
- `__dt`
- `__vt`
- `dialogTransition`
- `draw2d`
- `draw3d`
- `drawMenu`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `prepareExit`
- `reset`
- `setup`
- `setupDialogMenu`
- `switchToGameSelect`
- `tick`
- `tickState`
- `updateDialog`

### ClShellModeShow (12 members)

- `__ct`
- `__dt`
- `__vt`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `initialize`
- `isIdle`
- `reset`
- `setup`
- `tick`

### ClShellModeUpgrade (34 members)

- `__ct`
- `__dt`
- `__vt`
- `clearInfo`
- `devTick`
- `draw2d`
- `draw3d`
- `enter`
- `exit`
- `fillBoxStatusBase`
- `fillBoxStatusItem`
- `fillBoxStatusSkill`
- `initialize`
- `isIdle`
- `preTick`
- `reset`
- `setColors`
- `setScreenItemsAlpha`
- `setScreenPos`
- `setup`
- `setupCharacter`
- `setupMenu`
- `setupPopup`
- `setupScreenItems`
- `setupStatus`
- `tick`
- `tickBackground`
- `tickCharacter`
- `tickListing`
- `tickMenu`
- `tickPopup`
- `tickSavePopup`
- `tickScreenItems`
- `tickStatus`

### ClShieldSpell (7 members)

- `__ct`
- `__vt`
- `draw`
- `getType`
- `kill`
- `stopAffectingObject`
- `tick`

### ClSilverSwordEffect (5 members)

- `addDeath`
- `forceEnd`
- `initialize`
- `isActive`
- `tick`

### ClSimMeshObj (20 members)

- `__ct`
- `__vt`
- `activate`
- `createSimCollisionSpheres`
- `deactivate`
- `draw`
- `initializeAttributes`
- `msRTTI`
- `registerScriptMethods`
- `releaseSimCollisionSpheres`
- `removeAllAttributesAndServices`
- `sauSimMeshInit`
- `setAssetContainer`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setSneakRenderMode`
- `teleport`
- `tickAction`
- `tickFinal`

### ClSimulationBase (13 members)

- `__ct`
- `__vt`
- `addControlPoint`
- `constraintInitialize`
- `controlPointInitialize`
- `deactivate`
- `freeSubSimulation`
- `getControlPointByInitializationId`
- `getNthControlPoint`
- `getSegmentCount`
- `isInitialized`
- `releaseControlPoint`
- `setMatrix`

### ClSimulationManager (16 members)

- `getSimulationById`
- `initialize`
- `removeSimulation`
- `removeSubSimulation`
- `setFloatOpenParameterValue`
- `setIntegerOpenParameterValue`
- `setVectorOpenParameterValue`
- `smaCharacterSimulationPool`
- `smaFlagSimulationPool`
- `smaGenericSimulationPool`
- `smaSimulationCountByType`
- `smaTapestrySimulationPool`
- `smapActiveSimulationRootByType`
- `smapFreeSimulationRootByType`
- `teleportSimulation`
- `tick`

### ClSimulationObj (32 members)

- `__ct`
- `__vt`
- `activate`
- `allocateSimulationResources`
- `cutSegment`
- `deactivate`
- `doCharacterSeparation`
- `doCylinderSeparation`
- `doEllipsoidSeparation`
- `draw`
- `handleExplosion`
- `handleMessage`
- `handleStruckBySplashDamage`
- `handleStruckByWeapon`
- `initializeAttributes`
- `msRTTI`
- `registerScriptMethods`
- `releaseSimulationResources`
- `removeAllAttributesAndServices`
- `sauSetCharCollisionProperties`
- `sauSetStats`
- `sauSimulationInit`
- `setAssetContainer`
- `setFloatParam`
- `setIntParam`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setVectorParam`
- `struckByNonWeapon`
- `tickCollision`
- `tickFinal`

### ClSimulationRenderer (30 members)

- `freeSimulation`
- `freeSimulationSubObject`
- `getStringPointEntry`
- `initialize`
- `queueSimulation`
- `render`
- `reset`
- `setDynamicLightState`
- `setSubObjAlpha`
- `setTextureAsset`
- `setUcodeCameraState`
- `setUcodeState`
- `smDrawCamerasUsedCount`
- `smDrawListByTextureUsedCount`
- `smDrawListEntriesUsedCount`
- `smPointsInUseCount`
- `smSimulationHeadersInUseCount`
- `smStringsInUseCount`
- `smaCameraDrawLists`
- `smaDrawListByTextureEntryPool`
- `smaDrawListEntryPool`
- `smaDrawStringHeaderPool`
- `smaStringPointEntryPool`
- `smaStringPool`
- `smapTextureAssetsByIndex`
- `smbTeleportalItemsQueued`
- `smpActiveDrawStringHeaderRoot`
- `smpFreeDrawStringHeaderRoot`
- `smpFreeStringPointEntryRoot`
- `smpFreeStringRoot`

### ClSlaadLordObj (12 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `initialize`
- `isDeflecting`
- `msRTTI`
- `registerScriptMethods`
- `sauRegenerate`
- `sauShoot`
- `sauSleep`
- `sauTeleport`
- `tickAction`

### ClSorcererObj (23 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `fellOutOfWorld`
- `getIdleAnim`
- `getPlayerID`
- `getProjectileSource`
- `getWalkAnim`
- `handleAnimTrigger`
- `handleMessage`
- `initialize`
- `isDeflecting`
- `isDisabled`
- `msRTTI`
- `possess`
- `registerScriptMethods`
- `sauBlockEvadeSuccess`
- `sauInitializeHairSim`
- `setMatrix`
- `setPosition`
- `setRotation`
- `tickAction`

### ClSpawnerObj (11 members)

- `__ct`
- `__vt`
- `initializeAttributes`
- `msRTTI`
- `particleAttachToBone`
- `registerScriptMethods`
- `sauAttachToObject`
- `sauCanSpawn`
- `sauObjDied`
- `sauSpawnObj`
- `sauUpdatePosition`

### ClSpellElement (5 members)

- `__ct`
- `getCreationTime`
- `getSpellObject`
- `setCreationTime`
- `setSpellType`

### ClSpellManager (15 members)

- `addToFreePool`
- `destroySpell`
- `draw`
- `initialize`
- `playSpellSound`
- `releaseSpell`
- `requestSpell`
- `reset`
- `smElapsedTime`
- `smNumSpells`
- `smSpellList`
- `smSpellPool`
- `stopAffectingObject`
- `stopSpell`
- `tick`

### ClSpellObj (6 members)

- `__ct`
- `__vt`
- `draw`
- `getSpellClassFromType`
- `kill`
- `tick`

### ClSplineProjectile (6 members)

- `__ct`
- `__vt`
- `calculateTrajectory`
- `handleCollision`
- `setupSpline`
- `updatePosition`

### ClStatCapture (23 members)

- `addEventToBuffer`
- `convertEventToString`
- `flush`
- `fprintf`
- `initialize`
- `killedCliff`
- `killedDamage`
- `killedFall`
- `killedKillmove`
- `killedRemove`
- `mFilename`
- `mUsedBufferSize`
- `makeObjID`
- `mbEnabled`
- `mbNewSession`
- `mbTrace`
- `mfTime`
- `mpBuffer`
- `outputGameState`
- `start`
- `switchPlayer`
- `tick`
- `writeObj`

### ClStateMachine (9 members)

- `__ct`
- `__vt`
- `computeNewState`
- `evaluate`
- `handleStateEnter`
- `handleStateExit`
- `initialize`
- `reset`
- `tick`

### ClStateMachineData (6 members)

- `__ct`
- `__vt`
- `fixup`
- `initialize`
- `reset`
- `setup`

### ClStaticPropObj (28 members)

- `__ct`
- `__vt`
- `activate`
- `allocatePieces`
- `deactivate`
- `draw`
- `generateExplosionImpulse`
- `goToPieces`
- `handleExplosion`
- `handleMessage`
- `handleStruckAndDestroyedProp`
- `initialize`
- `msRTTI`
- `reconstruct`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `reset`
- `sauEnableCollision`
- `sauReconstruct`
- `sauStaticPropInit`
- `setAssetContainer`
- `setBreakParams`
- `setIlluminationTargets`
- `setMatrix`
- `setPosition`
- `setRotation`
- `tickAction`
- `tickCollision`

### ClSteering (10 members)

- `avoidCharacters`
- `calculatePitch`
- `calculateRoll`
- `keepDistance`
- `recalculateForces`
- `reset`
- `steerToAvoidCharacter`
- `tick`
- `tickFlying`
- `tickWalking`

### ClStrikableScriptObj (11 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `handleMessage`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `sauInitCylinder`
- `sauInitObb`
- `sauInitSphere`

### ClStrings (6 members)

- `getString`
- `getStringByLabelNoError`
- `getStringByLanguageLevel`
- `getStringNoError`
- `initialize`
- `initializeDatabase`

### ClStruckByHistory (5 members)

- `__ct`
- `calculateHandle`
- `canBeStruckBy`
- `isStruckBy`
- `reset`

### ClSubtitleAsset (6 members)

- `__vt`
- `displayCurrentVOSubtitle`
- `displaySubtitles`
- `getCurHeader`
- `msDisplaySubtitles`
- `mspMissionVoiceOver`

### ClTargetMeList (6 members)

- `addToTargetMeList`
- `clear`
- `initialize`
- `insert`
- `removeFromTargetMeList`
- `sort`

### ClTargetObj (11 members)

- `__ct`
- `__vt`
- `activate`
- `addToTargetMeList`
- `deactivate`
- `handleMessage`
- `isInView`
- `msRTTI`
- `registerScriptMethods`
- `removeFromTargetMeList`
- `sauInit`

### ClTargetting (26 members)

- `addToActiveTargetObjList`
- `canSeeTarget`
- `canTargetAndAssist`
- `facingTarget`
- `findBestTarget`
- `findTargets`
- `findTargetsActivePlayer`
- `findTargetsClosestInFrontEnemy`
- `findTargetsNearestEnemy`
- `getCurTargetPos`
- `getHeadTargetPos`
- `getHeadingToTarget`
- `getNearestPossibleThreat`
- `getNumAttackers`
- `initialize`
- `isValidTarget`
- `mAssistEachOther`
- `mEnemiesOnEnemies`
- `overrideTarget`
- `prepForDestroy`
- `removeFromActiveTargetObjList`
- `setBestTarget`
- `smpActiveTargetObjRoot`
- `staticInitialize`
- `staticReset`
- `tick`

### ClTeamAttackEffect (6 members)

- `end`
- `forceEnd`
- `initialize`
- `isActive`
- `start`
- `tick`

### ClTeleportTargetObj (14 members)

- `__ct`
- `__vt`
- `activate`
- `addToActiveTeleportTargetObjList`
- `deactivate`
- `getTeleportTargetObj`
- `msRTTI`
- `registerScriptMethods`
- `removeFromActiveTeleportTargetObjList`
- `sauInitialize`
- `sauSetFilter`
- `smpActiveTeleportTargetObjRoot`
- `staticInitialize`
- `staticReset`

### ClText (6 members)

- `__ct`
- `__vt`
- `draw`
- `postDraw`
- `preDraw`
- `reset`

### ClTexture (5 members)

- `allocate`
- `free`
- `getHeight`
- `getWidth`
- `set`

### ClTickManager (13 members)

- `__ct`
- `__vt`
- `addAttribute`
- `addToTickPhaseList`
- `allocateFromPool`
- `initializePool`
- `process`
- `releaseToPool`
- `removeAll`
- `removeAttribute`
- `removeFromTickPhaseList`
- `reset`
- `smManager`

### ClTimer1IntHandler (6 members)

- `install`
- `setTimerInterruptFrequency`
- `smActualHertz`
- `smDesiredHertz`
- `smTimer1IntHandlerID`
- `timer1IntHandler`

### ClTrailParticleRenderer (7 members)

- `beginPacket`
- `beginRendering`
- `canTrailFitInPacket`
- `decrementPacketSize`
- `endPacket`
- `endRendering`
- `setConstants`

### ClTrainingHUD (9 members)

- `draw`
- `getAssets`
- `highlightButton`
- `off`
- `on`
- `reset`
- `setText`
- `tick`
- `unhighlightButtons`

### ClTreadModule (16 members)

- `__ct`
- `__vt`
- `calcSectorIndex`
- `cutTo`
- `draw`
- `getDesiredPitch`
- `getDesiredTargetLead`
- `getFollowJump`
- `getFov`
- `getName`
- `getPitchRange`
- `getSectorFromParameter`
- `getSectorIndex`
- `getUseCombatFraming`
- `getViewTargetLerpSpeed`
- `solveConstraints`

### ClTriggerAttrib (11 members)

- `__ct`
- `addDetect`
- `canDetect`
- `getBoxData`
- `getPlaneData`
- `getWedgeData`
- `initBox`
- `initPlane`
- `initWedge`
- `sendMessage`
- `setPosition`

### ClTrollKingObj (6 members)

- `__ct`
- `__vt`
- `canTargetThisObj`
- `getLinkedMoveType`
- `msRTTI`
- `registerScriptMethods`

### ClTrollObj (9 members)

- `__ct`
- `__vt`
- `applyDamage`
- `die`
- `fadeOut`
- `giveHealth`
- `msRTTI`
- `registerScriptMethods`
- `tickAction`

### ClUIButtonText (9 members)

- `__ct`
- `__vt`
- `draw`
- `reset`
- `set`
- `setButton`
- `setButtonInGame`
- `setPosition`
- `setText`

### ClUICharacterObj (19 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `draw`
- `getShieldLevel`
- `giveItem`
- `giveSkill`
- `initializeForUI`
- `msRTTI`
- `prepForDestroy`
- `registerScriptMethods`
- `sauInitializeHairSim`
- `sauUICharacterInit`
- `setMatrix`
- `setPosition`
- `setRotation`
- `setSneakTimer`
- `tickAction`

### ClUIListing (14 members)

- `__ct`
- `__vt`
- `calculatePositions`
- `draw`
- `drawByBottom`
- `drawByMiddle`
- `drawByTop`
- `reset`
- `setCurrent`
- `setFont`
- `setList`
- `setPosition`
- `setSize`
- `setupFont`

### ClUISkillList (13 members)

- `__ct`
- `draw`
- `fillBox`
- `getFadeAlpha`
- `reset`
- `setAlpha`
- `setup`
- `setupBox`
- `setupUIInfo`
- `setupUIPosition`
- `tick`
- `turnOff`
- `turnOn`

### ClUIToggleItem (8 members)

- `__ct`
- `__vt`
- `draw`
- `reset`
- `setArrows`
- `setPosition`
- `setText`
- `tick`

### ClUnicode (5 members)

- `intcat`
- `itoa`
- `spacecat`
- `strcat`
- `strcpy`

### ClUserInput (10 members)

- `clearInputs`
- `enableAllInputs`
- `enableStickInput`
- `getPlayerCharacter`
- `getStickInput`
- `initialize`
- `load`
- `setup`
- `tick`
- `tickStickInput`

### ClVBlankIntHandler (10 members)

- `capTo30FPS`
- `getNumVBlanksSinceStart`
- `install`
- `queueDmaChain`
- `smCapTo30FPS`
- `smNumQueuedEntries`
- `smNumVBlanksSinceLastKick`
- `smNumVBlanksSinceStart`
- `smVBlankIntHandlerID`
- `vBlankIntHandler`

### ClVersion (7 members)

- `initialize`
- `scmaBuildDate`
- `scmaBuildMode`
- `smaDisplayMode`
- `smaFileMedia`
- `smaLanguage`
- `smaVersionNumber`

### ClVif0DmaBuffer (24 members)

- `AddCall`
- `AddRef`
- `Allocate`
- `BeginCall`
- `BeginChain`
- `BeginCont`
- `Commit`
- `EndCall`
- `EndChain`
- `EndCont`
- `Free`
- `GenerateInterrupt`
- `GetIssueMode`
- `GetPacketBuildingMode`
- `Reserve`
- `SetIssueMode`
- `SetPacketBuildingMode`
- `Sync`
- `UploadUCode`
- `UseBuffer`
- `__vt`
- `allocateVif0Buffer`
- `freeVif0Buffer`
- `initialize`

### ClVramManager (8 members)

- `AllocChunk`
- `AllocPermanentTexture`
- `AllocTexture`
- `CalculateNumBytesInVRAM`
- `FreeChunk`
- `FreePermanentTexture`
- `FreeTexture`
- `__ct`

### ClWad (6 members)

- `getFileData`
- `getFileSize`
- `getFilename`
- `getSize`
- `loadAndWait`
- `reset`

### ClWarriorObj (21 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `fellOutOfWorld`
- `getLinkedMoveType`
- `getPlayerID`
- `getProjectileSource`
- `holdProjectiles`
- `initialize`
- `isDefending`
- `isDisabled`
- `msRTTI`
- `notifyReflectionStateChange`
- `registerScriptMethods`
- `sauBlockEvadeSuccess`
- `sauInitializeHairSim`
- `setMatrix`
- `setPosition`
- `setRotation`
- `tickAction`

### ClWeaponManager (11 members)

- `createWeapon`
- `initialize`
- `registerScriptMethods`
- `releaseWeapon`
- `reset`
- `sauCreateWeapon`
- `sauFreeWeapon`
- `smNumFreeWeapons`
- `smNumWeapons`
- `smapWeapons`
- `smpWeaponMemory`

### ClWeaponObj (31 members)

- `__ct`
- `__vt`
- `activate`
- `checkRigidBodyCollisions`
- `deactivate`
- `draw`
- `drop`
- `hold`
- `initForUI`
- `initialize`
- `initializeAttributes`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `sauIgniteMithril`
- `sauSetWeaponDBName`
- `sauWeaponInit`
- `setAssetContainer`
- `setBloodParticleIdOverride`
- `setMatrix`
- `setWeaponMode`
- `setWeaponTrailID`
- `startWeaponCollision`
- `startWeaponTrail`
- `stopWeaponCollision`
- `stopWeaponCollisionPending`
- `stopWeaponTrail`
- `stopWeaponTrailPending`
- `tickAction`
- `tickWeaponCollision`
- `tickWeaponTrail`

### ClWeaponTrail (7 members)

- `CB`
- `addSamplePoint`
- `endTrail`
- `initialize`
- `postPhase`
- `prePhase`
- `tick`

### ClWickObj (11 members)

- `__ct`
- `__vt`
- `activate`
- `deactivate`
- `handleMessage`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `sauInitCylinderWick`
- `sauInitObbWick`
- `sauInitSphereWick`

### ClWindManager (14 members)

- `getCurrentWindParameters`
- `getWindBallValues`
- `initialize`
- `mBaseDirection`
- `mCurrentDirection`
- `mMagnitude`
- `mPeriod`
- `mPeriodCurrentTime`
- `mTargetDirection`
- `mVariation`
- `mWindActive`
- `setWindParameters`
- `setWindVariation`
- `tick`

### ClWizardShield (17 members)

- `CB`
- `draw`
- `initialize`
- `move`
- `postOp`
- `postPhase`
- `preOp`
- `prePhase`
- `setAlpha`
- `setAmp`
- `setFreq`
- `setRadius`
- `setTexScale`
- `setTexture`
- `start`
- `stop`
- `tick`

### ClWorldBillboard (6 members)

- `CB`
- `initialize`
- `postOpFn`
- `postPhase`
- `preOpFn`
- `prePhase`

### ClWorldCollisionNode (12 members)

- `beginCollision`
- `correctPointersRecursive`
- `endCollision`
- `getLastEllipsoidCollisionNode`
- `initialize`
- `isEllipsoidPenetratingRecursive`
- `isLineInside`
- `isOBBPenetratingRecursive`
- `isPointCollisionRecursive`
- `registerObject`
- `setLastEllipsoidCollisionNode`
- `unregisterObject`

### ClWorldPlant (6 members)

- `CB`
- `initialize`
- `postPhase`
- `prePhase`
- `setWindDirection`
- `tick`

### ClWorldPropObj (35 members)

- `__ct`
- `__vt`
- `activate`
- `allocatePieces`
- `deactivate`
- `draw`
- `generateExplosionImpulse`
- `getBoneIndexByUpdateIndex`
- `getNumBoneUpdates`
- `getNumSubObjects`
- `goToPieces`
- `handleBoneUpdate`
- `handleExplosion`
- `handleMessage`
- `handleNoamMsg`
- `handleStruckAndDestroyedProp`
- `initialize`
- `msRTTI`
- `registerScriptMethods`
- `removeAllAttributesAndServices`
- `reset`
- `sauFinishAnim`
- `sauIsPlayingAnim`
- `sauSetAnim`
- `sauWorldPropInit`
- `sauWorldPropWithAnimInit`
- `setAnim`
- `setAssetContainer`
- `setBreakParams`
- `setMatrix`
- `setPosition`
- `setRotation`
- `tickAction`
- `tickBuild`
- `tickCollision`

