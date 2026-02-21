# Auto-generated from engine-map.json
# Total: 6447 functions across 660 classes
# Address range: 0x00100258 - 0x01358b70

FUNCTIONS = [
    (0x00100258, "item::picFind"),  # size=364, subsystem=Game Entities
    (0x001003c8, "item::picInit"),  # size=224, subsystem=Game Entities
    (0x001004a8, "item::picKickOneOut"),  # size=256, subsystem=Game Entities
    (0x001005a8, "item::picProcess"),  # size=928, subsystem=Game Entities
    (0x00100948, "item::picAdd"),  # size=220, subsystem=Game Entities
    (0x00100a28, "item::dropGold"),  # size=632, subsystem=Game Entities
    (0x00100ca0, "item::dropItem"),  # size=384, subsystem=Game Entities
    (0x00100e20, "item::dropTreasure"),  # size=2484, subsystem=Game Entities
    (0x001017d8, "item::findAndStripGender"),  # size=556, subsystem=Game Entities
    (0x00101a08, "item::getAttributeName"),  # size=548, subsystem=Game Entities
    (0x00101c30, "item::getName"),  # size=1348, subsystem=Game Entities
    (0x00102178, "item::getValue"),  # size=6048, subsystem=Game Entities
    (0x00103918, "item::getArmorBonus"),  # size=212, subsystem=Game Entities
    (0x001039f0, "item::getAttackBonus"),  # size=212, subsystem=Game Entities
    (0x00103ac8, "item::getDamageRangeAll"),  # size=1116, subsystem=Game Entities
    (0x00103f28, "item::createNamedRandom"),  # size=1304, subsystem=Game Entities
    (0x00104440, "item::createRandom"),  # size=4220, subsystem=Game Entities
    (0x001054c0, "item::createRandomByDropLevel"),  # size=1508, subsystem=Game Entities
    (0x00105aa8, "item::createRandomCombineableItem"),  # size=1204, subsystem=Game Entities
    (0x00105f60, "item::create"),  # size=5428, subsystem=Game Entities
    (0x00107498, "item::createUniqueRandom"),  # size=344, subsystem=Game Entities
    (0x001075f0, "item::getPicName"),  # size=1164, subsystem=Game Entities
    (0x00107a80, "item::getPic"),  # size=228, subsystem=Game Entities
    (0x00107b68, "item::init"),  # size=384, subsystem=Game Entities
    (0x00107ce8, "item::makeRandomPotion"),  # size=632, subsystem=Game Entities
    (0x00107f60, "item::createNamedList"),  # size=244, subsystem=Game Entities
    (0x00108058, "item::getnthPipeString"),  # size=124, subsystem=Game Entities
    (0x001080d8, "item::getWeight"),  # size=160, subsystem=Game Entities
    (0x00108178, "item::getDamageRange"),  # size=180, subsystem=Game Entities
    (0x00108230, "item::getDamageMultiplier"),  # size=16, subsystem=Game Entities
    (0x00108240, "item::getEnchantmentValue"),  # size=28, subsystem=Game Entities
    (0x00108260, "item::getWeaponType"),  # size=68, subsystem=Game Entities
    (0x001082a8, "item::getArmorType"),  # size=92, subsystem=Game Entities
    (0x00108308, "item::setupHalo"),  # size=220, subsystem=Game Entities
    (0x001083e8, "item::pack"),  # size=28, subsystem=Game Entities
    (0x00108408, "item::unpack"),  # size=28, subsystem=Game Entities
    (0x00108428, "item::getPicSize"),  # size=112, subsystem=Game Entities
    (0x00108498, "item::getProxyMeshId"),  # size=68, subsystem=Game Entities
    (0x001084e0, "item::description::compareToItem"),  # size=68, subsystem=Other
    (0x00108528, "creature::numInRegion"),  # size=240, subsystem=Game Entities
    (0x00108e58, "Creature::constructor"),  # size=852, subsystem=Game Entities
    (0x001091b0, "Creature::finishConstruction"),  # size=316, subsystem=Game Entities
    (0x001092f0, "Creature::setParameters"),  # size=632, subsystem=Game Entities
    (0x00109710, "Creature::runStandardGlow"),  # size=244, subsystem=Game Entities
    (0x00109808, "Creature::draw"),  # size=2716, subsystem=Game Entities
    (0x0010a2a8, "Creature::turnToFace"),  # size=380, subsystem=Game Entities
    (0x0010a428, "Creature::objectActivationCheck"),  # size=228, subsystem=Game Entities
    (0x0010a510, "Creature::pointInZone"),  # size=456, subsystem=Game Entities
    (0x0010a6d8, "Creature::objectInZone"),  # size=412, subsystem=Game Entities
    (0x0010a878, "Creature::enemyInZone2"),  # size=584, subsystem=Game Entities
    (0x0010aac0, "Creature::alternateEnemyInZone"),  # size=1268, subsystem=Game Entities
    (0x0010afb8, "Creature::objectIsCrowded"),  # size=524, subsystem=Game Entities
    (0x0010b4a8, "Creature::isEnemy"),  # size=176, subsystem=Game Entities
    (0x0010b558, "Creature::updateEnemy"),  # size=1212, subsystem=Game Entities
    (0x0010ba18, "Creature::pathIsClearForRadius"),  # size=892, subsystem=Game Entities
    (0x0010bd98, "Creature::findClearPath"),  # size=1068, subsystem=Game Entities
    (0x0010c1c8, "Creature::ISeeDeadPeople"),  # size=364, subsystem=Game Entities
    (0x0010c338, "Creature::dropTreasure"),  # size=3864, subsystem=Game Entities
    (0x0010d250, "Creature::getSmartRandomDestination"),  # size=468, subsystem=Game Entities
    (0x0010d428, "Creature::newDamageHandler"),  # size=5872, subsystem=Game Entities
    (0x0010ebf8, "Creature::everyFrame"),  # size=4136, subsystem=Game Entities
    (0x0010fc20, "Creature::move2"),  # size=1688, subsystem=Game Entities
    (0x001102b8, "Creature::steerAndRouteToPosition"),  # size=1572, subsystem=Game Entities
    (0x001108e0, "Creature::steerToPosition"),  # size=744, subsystem=Game Entities
    (0x00110bc8, "Creature::persue2"),  # size=1216, subsystem=Game Entities
    (0x00111088, "Creature::flee2"),  # size=1032, subsystem=Game Entities
    (0x00111490, "Creature::slideBack"),  # size=924, subsystem=Game Entities
    (0x00111830, "Creature::creatureAdvanceAnimation"),  # size=420, subsystem=Game Entities
    (0x001119d8, "Creature::msg_save"),  # size=436, subsystem=Game Entities
    (0x00111b90, "Creature::msg_load"),  # size=608, subsystem=Game Entities
    (0x00111df0, "Creature::msg_poke"),  # size=372, subsystem=Game Entities
    (0x00111f68, "Creature::msg_getPokeName"),  # size=980, subsystem=Game Entities
    (0x00112340, "Creature::~destructor"),  # size=244, subsystem=Game Entities
    (0x00112438, "Creature::creatureSlamEffect"),  # size=884, subsystem=Game Entities
    (0x001128a8, "Creature::setAnimEventFlags"),  # size=88, subsystem=Game Entities
    (0x00112900, "Creature::setAnimEventFlagsResMap"),  # size=60, subsystem=Game Entities
    (0x00112940, "Creature::initMiniboss"),  # size=12, subsystem=Game Entities
    (0x00112950, "Creature::getMinibossName"),  # size=12, subsystem=Game Entities
    (0x001129f0, "Creature::setStateProcessing"),  # size=108, subsystem=Game Entities
    (0x00112a60, "Creature::move"),  # size=56, subsystem=Game Entities
    (0x00112a98, "Creature::turnToFaceEnemy"),  # size=96, subsystem=Game Entities
    (0x00112af8, "Creature::death"),  # size=168, subsystem=Game Entities
    (0x00112ba0, "Creature::charm"),  # size=64, subsystem=Game Entities
    (0x00112be0, "Creature::stun"),  # size=80, subsystem=Game Entities
    (0x00112c30, "Creature::confuse"),  # size=52, subsystem=Game Entities
    (0x00112c68, "Creature::enemyInZone"),  # size=64, subsystem=Game Entities
    (0x00112ca8, "Creature::pathIsClear"),  # size=256, subsystem=Game Entities
    (0x00112da8, "Creature::bFarFromHome"),  # size=96, subsystem=Game Entities
    (0x00112e08, "Creature::bExitStatePersueIdle"),  # size=12, subsystem=Game Entities
    (0x00112e18, "Creature::produceMeleeDamage"),  # size=360, subsystem=Game Entities
    (0x00112f80, "Creature::produceGeneralDamage"),  # size=308, subsystem=Game Entities
    (0x001130b8, "Creature::steerAndRouteToEnemy"),  # size=112, subsystem=Game Entities
    (0x00113128, "Creature::smartWander"),  # size=212, subsystem=Game Entities
    (0x00113200, "Creature::getCurrentRoutePoint"),  # size=112, subsystem=Game Entities
    (0x00113270, "Creature::getNextRoutePoint"),  # size=216, subsystem=Game Entities
    (0x00113348, "Creature::plotRoute"),  # size=280, subsystem=Game Entities
    (0x00113460, "Creature::resetRouting"),  # size=40, subsystem=Game Entities
    (0x00113488, "Creature::msg_route"),  # size=44, subsystem=Game Entities
    (0x001134b8, "Creature::msg_alert"),  # size=36, subsystem=Game Entities
    (0x00113618, "Creature::msg_hurt"),  # size=240, subsystem=Game Entities
    (0x00113708, "Creature::msg_collisionWorld"),  # size=36, subsystem=Game Entities
    (0x00113730, "Creature::msg_collision"),  # size=8, subsystem=Game Entities
    (0x00113738, "Creature::msg_moveCollision"),  # size=52, subsystem=Game Entities
    (0x00113770, "creature::sleepMonsters"),  # size=32, subsystem=Game Entities
    (0x00113790, "creature::wakeMonsters"),  # size=32, subsystem=Game Entities
    (0x001137b0, "Creature::msg_trigger"),  # size=116, subsystem=Game Entities
    (0x00113828, "Creature::setActiveChunks"),  # size=104, subsystem=Game Entities
    (0x00113890, "Creature::terminateSpell"),  # size=64, subsystem=Game Entities
    (0x001138d0, "Creature::checkIfSpellIsRunning"),  # size=120, subsystem=Game Entities
    (0x00113948, "Creature::addSpell"),  # size=48, subsystem=Game Entities
    (0x00113978, "Creature::runSpells"),  # size=180, subsystem=Game Entities
    (0x00113a30, "Creature::creatureFindLeadYaw"),  # size=272, subsystem=Game Entities
    (0x00113b40, "Creature::findEnemyLeadPosition"),  # size=208, subsystem=Game Entities
    (0x00113ce0, "GameObject::clone"),  # size=244, subsystem=Game Props
    (0x00113dd8, "Creature::clone"),  # size=1336, subsystem=Game Entities
    (0x00114310, "Projectile::clone"),  # size=276, subsystem=C++ Runtime
    (0x00114428, "Prop::clone"),  # size=604, subsystem=C++ Runtime
    (0x00114688, "ParticleProp::clone"),  # size=612, subsystem=Particles
    (0x001148f0, "ItemProp::clone"),  # size=680, subsystem=C++ Runtime
    (0x00114b98, "PhProp::clone"),  # size=980, subsystem=C++ Runtime
    (0x00114f70, "PhIce::clone"),  # size=1012, subsystem=Game Entities
    (0x00115368, "Gold::clone"),  # size=368, subsystem=Renderer
    (0x001154d8, "Container::clone"),  # size=368, subsystem=Game Props
    (0x00115648, "Ice::clone"),  # size=312, subsystem=Game Entities
    (0x00115780, "Chest::clone"),  # size=316, subsystem=Game Props
    (0x001158c0, "CosmeticPropAnim::clone"),  # size=340, subsystem=Game Props
    (0x00115a18, "CosmeticProp::clone"),  # size=296, subsystem=Game Props
    (0x00115b40, "UserParamProp::clone"),  # size=308, subsystem=Game Props
    (0x00115c78, "TriggerParams::clone"),  # size=264, subsystem=C++ Runtime
    (0x00115d80, "Trigger::clone"),  # size=336, subsystem=Game Props
    (0x00115ed0, "Blocker::clone"),  # size=256, subsystem=Game Entities
    (0x00115fd0, "VehicleBodySphere::clone"),  # size=272, subsystem=Physics
    (0x001160e0, "WaveMaker::clone"),  # size=420, subsystem=Audio
    (0x00116288, "PushTrigger::clone"),  # size=256, subsystem=Game Props
    (0x00116388, "Player::clone"),  # size=2280, subsystem=Game Entities
    (0x00116c70, "Ant::clone"),  # size=1404, subsystem=Game Entities
    (0x001171f0, "AntQueen::clone"),  # size=1412, subsystem=Game Entities
    (0x00117778, "AntWave::clone"),  # size=1376, subsystem=Audio
    (0x00117cd8, "Badger::clone"),  # size=1364, subsystem=C++ Runtime
    (0x00118230, "BlackWidow::clone"),  # size=1532, subsystem=Game Entities
    (0x00118830, "Critter::clone"),  # size=1604, subsystem=Game Entities
    (0x00118e78, "Cyclops::clone"),  # size=1356, subsystem=Game Entities
    (0x001193c8, "FemaleDarkElf::clone"),  # size=1572, subsystem=Game Entities
    (0x001199f0, "FireBeetle::clone"),  # size=1472, subsystem=Renderer
    (0x00119fb0, "FireFly::clone"),  # size=1648, subsystem=Game Entities
    (0x0011a620, "Froglock::clone"),  # size=1580, subsystem=Game Entities
    (0x0011ac50, "Generator::clone"),  # size=1408, subsystem=Game Props
    (0x0011b1d0, "Ghoul::clone"),  # size=1372, subsystem=Game Entities
    (0x0011b730, "Gnome::clone"),  # size=1384, subsystem=Renderer
    (0x0011bc98, "Goblin::clone"),  # size=1652, subsystem=Game Entities
    (0x0011c310, "LavaMonster::clone"),  # size=1460, subsystem=Game Entities
    (0x0011c8c8, "MaleDarkElf::clone"),  # size=1580, subsystem=Renderer
    (0x0011cef8, "Orc::clone"),  # size=1644, subsystem=Game Entities
    (0x0011d568, "Scorpion::clone"),  # size=1356, subsystem=Game Entities
    (0x0011dab8, "Skeleton::clone"),  # size=1612, subsystem=Game Entities
    (0x0011e108, "Skelight::clone"),  # size=1572, subsystem=Renderer
    (0x0011e730, "Spider::clone"),  # size=1356, subsystem=C++ Runtime
    (0x0011ec80, "SpiderQueen::clone"),  # size=1560, subsystem=Game Entities
    (0x0011f298, "SmallSpider::clone"),  # size=1348, subsystem=C++ Runtime
    (0x0011f7e0, "SuperOrc::clone"),  # size=1568, subsystem=Game Entities
    (0x0011fe00, "CdEyeball::clone"),  # size=1364, subsystem=C++ Runtime
    (0x00120358, "UndeadKnight::clone"),  # size=1588, subsystem=Game Entities
    (0x00120990, "Vampire::clone"),  # size=1348, subsystem=C++ Runtime
    (0x00120ed8, "VampireLord::clone"),  # size=1696, subsystem=Game Entities
    (0x00121578, "WoodElfSoldier::clone"),  # size=1420, subsystem=Game Entities
    (0x00121b08, "Wraith::clone"),  # size=1376, subsystem=Game Entities
    (0x00122068, "NPC::clone"),  # size=1588, subsystem=Game Entities
    (0x001226a0, "GutChunk::clone"),  # size=1052, subsystem=Renderer
    (0x00122ac0, "LooseIceChunk::clone"),  # size=996, subsystem=Game Entities
    (0x00122ea8, "Torch::clone"),  # size=440, subsystem=C++ Runtime
    (0x00123060, "Fire::clone"),  # size=264, subsystem=Game Props
    (0x00123168, "FlyingText::clone"),  # size=428, subsystem=Renderer
    (0x00123318, "Candle::clone"),  # size=448, subsystem=Renderer
    (0x001234d8, "Cat::clone"),  # size=1404, subsystem=Game Entities
    (0x00123a58, "Candle2::clone"),  # size=272, subsystem=Renderer
    (0x00123b68, "Lantern::clone"),  # size=456, subsystem=C++ Runtime
    (0x00123d30, "Lamp::clone"),  # size=432, subsystem=C++ Runtime
    (0x00123ee0, "FireEffect::clone"),  # size=292, subsystem=Game Entities
    (0x00124008, "RecallEffect::clone"),  # size=304, subsystem=Game Entities
    (0x00124138, "IceChunk::clone"),  # size=264, subsystem=Game Entities
    (0x00124240, "FrostStormSpell::clone"),  # size=492, subsystem=C++ Runtime
    (0x00124430, "FrostStormIceChunk::clone"),  # size=996, subsystem=Game Entities
    (0x00124818, "GlowingCylinder::clone"),  # size=304, subsystem=Game Entities
    (0x00124948, "GlowingShaft::clone"),  # size=296, subsystem=Renderer
    (0x00124a70, "MissileTrap::clone"),  # size=272, subsystem=Game Props
    (0x00124b80, "Shooter::clone"),  # size=332, subsystem=Game Entities
    (0x00124cd0, "WaterSpout::clone"),  # size=296, subsystem=Renderer
    (0x00124df8, "DummyDamager::clone"),  # size=360, subsystem=Renderer
    (0x00124f60, "Sparks::clone"),  # size=528, subsystem=Renderer
    (0x00125170, "HolyBolt::clone"),  # size=544, subsystem=Renderer
    (0x00125390, "OniBall::clone"),  # size=528, subsystem=Game Entities
    (0x001255a0, "LostSoul::clone"),  # size=512, subsystem=Game Entities
    (0x001257a0, "Root::clone"),  # size=544, subsystem=C++ Runtime
    (0x001259c0, "UnholyAura::clone"),  # size=468, subsystem=Game Entities
    (0x00125b98, "IceBall::clone"),  # size=504, subsystem=Projectiles
    (0x00125d90, "MissileWeapon::clone"),  # size=980, subsystem=Projectiles
    (0x00126168, "AnimatedMissile::clone"),  # size=356, subsystem=Renderer
    (0x001262d0, "playerProjectile::clone"),  # size=1020, subsystem=Renderer
    (0x001266d0, "beetleProjectile::clone"),  # size=1008, subsystem=Physics
    (0x00126ac0, "WebTrap::clone"),  # size=428, subsystem=Game Props
    (0x00126c70, "LooseFire::clone"),  # size=276, subsystem=Game Props
    (0x00126d88, "GroundPoundEffect::clone"),  # size=484, subsystem=Game Entities
    (0x00126f70, "LightEffect::clone"),  # size=524, subsystem=Lighting
    (0x00127180, "Player1::clone"),  # size=256, subsystem=C++ Runtime
    (0x00127280, "charAmbient_Light::clone"),  # size=256, subsystem=Lighting
    (0x00127380, "charDirectional_Light::clone"),  # size=256, subsystem=Lighting
    (0x00127480, "charDirectional_LightD::clone"),  # size=256, subsystem=Lighting
    (0x00127580, "WorldPart::clone"),  # size=272, subsystem=C++ Runtime
    (0x00127690, "DoorSwing::clone"),  # size=296, subsystem=Game Props
    (0x001277b8, "RollDoor::clone"),  # size=304, subsystem=C++ Runtime
    (0x001278e8, "DoorSecret::clone"),  # size=304, subsystem=Game Props
    (0x00127a18, "Switch::clone"),  # size=272, subsystem=C++ Runtime
    (0x00127b28, "FloorSwitch::clone"),  # size=288, subsystem=Game Props
    (0x00127c48, "FallPlatform::clone"),  # size=352, subsystem=C++ Runtime
    (0x00127da8, "FireTrail::clone"),  # size=308, subsystem=Game Entities
    (0x00127ee0, "FireTrailMaker::clone"),  # size=356, subsystem=Game Entities
    (0x00128048, "Savepoint::clone"),  # size=508, subsystem=Game Props
    (0x00128248, "JumpGate::clone"),  # size=660, subsystem=Game Props
    (0x001284e0, "FireBomb::clone"),  # size=304, subsystem=C++ Runtime
    (0x00128610, "FireBomblet::clone"),  # size=544, subsystem=C++ Runtime
    (0x00128830, "FireBombletJr::clone"),  # size=328, subsystem=C++ Runtime
    (0x00128978, "StaticFire::clone"),  # size=636, subsystem=C++ Runtime
    (0x00128bf8, "PokeReflector::clone"),  # size=256, subsystem=Game Entities
    (0x00128cf8, "Lever::clone"),  # size=280, subsystem=Game Props
    (0x00128e10, "Counter::clone"),  # size=264, subsystem=C++ Runtime
    (0x00128f18, "Timer::clone"),  # size=272, subsystem=Game Props
    (0x00129028, "ShopDaemon::clone"),  # size=264, subsystem=C++ Runtime
    (0x00129130, "WeaponRack::clone"),  # size=336, subsystem=Renderer
    (0x00129280, "Weather::clone"),  # size=288, subsystem=Game Entities
    (0x001293a0, "Teleporter::clone"),  # size=1348, subsystem=Renderer
    (0x001298e8, "poisonGasSpell::clone"),  # size=332, subsystem=C++ Runtime
    (0x00129a38, "dustCloud::clone"),  # size=320, subsystem=Projectiles
    (0x00129b78, "PointSourceSound::clone"),  # size=312, subsystem=Audio
    (0x00129cb0, "PushPhysicsProp::clone"),  # size=588, subsystem=Renderer
    (0x00133a90, "CCompress::analCompress"),  # size=1228, subsystem=File I/O
    (0x00133f60, "CDecompress::analDecompress"),  # size=1100, subsystem=File I/O
    (0x00134ec0, "ShockProjectile::clone"),  # size=8, subsystem=Projectiles
    (0x0013eac8, "Light::~destructor"),  # size=92, subsystem=Lighting
    (0x00140e10, "GameObject::removeTag"),  # size=332, subsystem=Game Props
    (0x00140f60, "GameObject::findTagInt"),  # size=316, subsystem=Game Props
    (0x001410a0, "GameObject::findTagFloat"),  # size=332, subsystem=Game Props
    (0x001411f0, "GameObject::constructor"),  # size=1124, subsystem=Game Props
    (0x00141658, "GameObject::~destructor"),  # size=680, subsystem=Game Props
    (0x00141b70, "GameObject::genericMove"),  # size=1512, subsystem=Game Props
    (0x00143a80, "GameObject::findTagString"),  # size=304, subsystem=Game Props
    (0x00143bb0, "GameObject::setResource"),  # size=136, subsystem=Game Props
    (0x00144cb8, "Projectile::move"),  # size=1072, subsystem=C++ Runtime
    (0x001450e8, "MissileWeapon::constructor"),  # size=1356, subsystem=Projectiles
    (0x00145638, "MissileWeapon::~destructor"),  # size=228, subsystem=Projectiles
    (0x00145720, "MissileWeapon::msg_run"),  # size=4452, subsystem=Projectiles
    (0x00146888, "MissileWeapon::msg_draw"),  # size=1228, subsystem=Projectiles
    (0x00146d58, "MissileWeapon::msg_collision"),  # size=1312, subsystem=Projectiles
    (0x00147278, "MissileWeapon::findClosestShadowBall"),  # size=556, subsystem=Projectiles
    (0x001474a8, "AnimatedMissile::msg_run"),  # size=528, subsystem=Renderer
    (0x001476b8, "Prop::constructor"),  # size=504, subsystem=C++ Runtime
    (0x001478b0, "Prop::constructor"),  # size=404, subsystem=C++ Runtime
    (0x00147a48, "Prop::init"),  # size=996, subsystem=C++ Runtime
    (0x00147e30, "Prop::msg_run"),  # size=780, subsystem=C++ Runtime
    (0x00148140, "ParticleProp::msg_run"),  # size=832, subsystem=Particles
    (0x00148738, "PhProp::initStuff"),  # size=644, subsystem=C++ Runtime
    (0x001489c0, "PhProp::constructor"),  # size=836, subsystem=C++ Runtime
    (0x00148d08, "PhProp::constructor"),  # size=864, subsystem=C++ Runtime
    (0x00149068, "PhProp::constructor"),  # size=488, subsystem=C++ Runtime
    (0x00149250, "PhProp::constructor"),  # size=488, subsystem=C++ Runtime
    (0x00149438, "PhProp::msg_run"),  # size=4140, subsystem=C++ Runtime
    (0x0014a468, "PhProp::msg_draw"),  # size=420, subsystem=C++ Runtime
    (0x0014a610, "UserParamProp::constructor"),  # size=768, subsystem=Game Props
    (0x0014a910, "UserParamProp::msg_draw"),  # size=296, subsystem=Game Props
    (0x0014aa38, "Gold::constructor"),  # size=768, subsystem=Renderer
    (0x0014ad38, "Gold::msg_draw"),  # size=1160, subsystem=Renderer
    (0x0014b1c0, "CosmeticPropAnim::msg_load"),  # size=356, subsystem=Game Props
    (0x0014b328, "CosmeticProp::msg_load"),  # size=216, subsystem=Game Props
    (0x0014b400, "Player1::constructor"),  # size=656, subsystem=C++ Runtime
    (0x0014b690, "Prop::msg_save"),  # size=372, subsystem=C++ Runtime
    (0x0014b808, "Prop::msg_load"),  # size=476, subsystem=C++ Runtime
    (0x0014b9e8, "ItemProp::constructor"),  # size=480, subsystem=C++ Runtime
    (0x0014bbc8, "ItemProp::constructor"),  # size=796, subsystem=C++ Runtime
    (0x0014bee8, "ItemProp::constructor"),  # size=772, subsystem=C++ Runtime
    (0x0014c1f0, "ItemProp::msg_draw"),  # size=544, subsystem=C++ Runtime
    (0x00150100, "PushPhysicsProp::msg_load"),  # size=384, subsystem=Renderer
    (0x00150280, "PushPhysicsProp::constructor"),  # size=360, subsystem=Renderer
    (0x001503e8, "PushPhysicsProp::msg_collision"),  # size=488, subsystem=Renderer
    (0x001505d0, "PushPhysicsProp::msg_run"),  # size=2732, subsystem=Renderer
    (0x00151080, "WaveMaker::constructor"),  # size=1496, subsystem=Audio
    (0x00151658, "WaveMaker::msg_run"),  # size=2960, subsystem=Audio
    (0x001521e8, "WaveMaker::doWavelet"),  # size=1872, subsystem=Audio
    (0x00152938, "WaveMaker::doWaveletReflection"),  # size=300, subsystem=Audio
    (0x00152a68, "WaveMaker::doWaveletCollision"),  # size=608, subsystem=Audio
    (0x00152e30, "ParticleMorphEffect::msg_run"),  # size=1952, subsystem=Particles
    (0x00153fa8, "GameObject::eRand"),  # size=40, subsystem=Game Props
    (0x00153fd0, "Projectile::constructor"),  # size=156, subsystem=C++ Runtime
    (0x00154070, "AnimatedMissile::constructor"),  # size=380, subsystem=Renderer
    (0x001541f0, "AnimatedMissile::draw"),  # size=192, subsystem=Renderer
    (0x001542b0, "AnimatedMissile::msg_collision"),  # size=280, subsystem=Renderer
    (0x001543c8, "Prop::constructor"),  # size=196, subsystem=C++ Runtime
    (0x00154490, "Prop::constructor"),  # size=456, subsystem=C++ Runtime
    (0x00154658, "Prop::constructor"),  # size=352, subsystem=C++ Runtime
    (0x001547b8, "Prop::constructor"),  # size=108, subsystem=C++ Runtime
    (0x00154828, "Prop::msg_draw"),  # size=308, subsystem=C++ Runtime
    (0x00154960, "ParticleProp::constructor"),  # size=172, subsystem=Particles
    (0x00154a10, "PhProp::msg_getPokeName"),  # size=168, subsystem=C++ Runtime
    (0x00154ab8, "PhProp::msg_poke"),  # size=240, subsystem=C++ Runtime
    (0x00154ba8, "PhProp::setOnFire"),  # size=8, subsystem=C++ Runtime
    (0x00154bb0, "UserParamProp::msg_run"),  # size=72, subsystem=Game Props
    (0x00154bf8, "UserParamProp::msg_getPokeName"),  # size=128, subsystem=Game Props
    (0x00154c78, "UserParamProp::msg_poke"),  # size=72, subsystem=Game Props
    (0x00154cc0, "Gold::constructor"),  # size=188, subsystem=Renderer
    (0x00154d80, "Gold::msg_save"),  # size=24, subsystem=Renderer
    (0x00154d98, "Gold::msg_load"),  # size=24, subsystem=Renderer
    (0x00154db0, "Gold::msg_collision"),  # size=184, subsystem=Renderer
    (0x00154e68, "Gold::msg_run"),  # size=152, subsystem=Renderer
    (0x00154f00, "CosmeticPropAnim::constructor"),  # size=124, subsystem=Game Props
    (0x00154f80, "CosmeticPropAnim::constructor"),  # size=396, subsystem=Game Props
    (0x00155110, "CosmeticPropAnim::msg_draw"),  # size=168, subsystem=Game Props
    (0x001551b8, "CosmeticPropAnim::msg_run"),  # size=68, subsystem=Game Props
    (0x00155200, "CosmeticPropAnim::msg_save"),  # size=200, subsystem=Game Props
    (0x001552c8, "CosmeticProp::constructor"),  # size=116, subsystem=Game Props
    (0x00155340, "CosmeticProp::constructor"),  # size=264, subsystem=Game Props
    (0x00155448, "CosmeticProp::msg_save"),  # size=160, subsystem=Game Props
    (0x001554e8, "CosmeticProp::msg_draw"),  # size=168, subsystem=Game Props
    (0x00155590, "charAmbient_Light::constructor"),  # size=160, subsystem=Lighting
    (0x00155630, "charDirectional_Light::constructor"),  # size=160, subsystem=Lighting
    (0x001556d0, "charDirectional_LightD::constructor"),  # size=128, subsystem=Lighting
    (0x00155750, "ItemProp::msg_save"),  # size=180, subsystem=C++ Runtime
    (0x00155808, "ItemProp::msg_load"),  # size=280, subsystem=C++ Runtime
    (0x00155920, "ItemProp::msg_getPokeName"),  # size=168, subsystem=C++ Runtime
    (0x001559c8, "ItemProp::msg_poke"),  # size=240, subsystem=C++ Runtime
    (0x00155bd0, "PushPhysicsProp::msg_save"),  # size=276, subsystem=Renderer
    (0x00155ce8, "PushPhysicsProp::constructor"),  # size=128, subsystem=Renderer
    (0x00155d68, "PushPhysicsProp::msg_draw"),  # size=220, subsystem=Renderer
    (0x00155e48, "WaveMaker::getWaveletMat"),  # size=192, subsystem=Audio
    (0x00155f08, "ParticleMorphEffect::constructor"),  # size=148, subsystem=Particles
    (0x0015c038, "map::readMap"),  # size=416, subsystem=UI
    (0x0015c1d8, "map::earlyInit"),  # size=324, subsystem=UI
    (0x0015c320, "map::addIcon"),  # size=772, subsystem=UI
    (0x0015c628, "map::draw"),  # size=5936, subsystem=UI
    (0x0015dd58, "map::revealMap"),  # size=684, subsystem=UI
    (0x0015e010, "map::writeMap"),  # size=88, subsystem=UI
    (0x0015e068, "map::init"),  # size=12, subsystem=UI
    (0x0015e078, "map::revealEntireMap"),  # size=120, subsystem=UI
    (0x0015e0f0, "map::worldToMap"),  # size=68, subsystem=UI
    (0x0015e138, "map::isRevealed"),  # size=8, subsystem=UI
    (0x0015e140, "map::willDraw"),  # size=84, subsystem=UI
    (0x0015e948, "Spell::eRand"),  # size=40, subsystem=Spells
    (0x0015e970, "SkillDiseaseWeapons::constructor"),  # size=44, subsystem=Skills
    (0x0015e9a0, "SkillDiseaseWeapons::initRamps"),  # size=32, subsystem=Skills
    (0x0015e9c0, "SkillPoisonWeapons::constructor"),  # size=44, subsystem=Skills
    (0x0015e9f0, "SkillPoisonWeapons::initRamps"),  # size=32, subsystem=Skills
    (0x0015ea10, "SkillHateBeam::constructor"),  # size=48, subsystem=Skills
    (0x0015ea40, "SkillHateBeam::initRamps"),  # size=32, subsystem=Skills
    (0x0015ea60, "SkillBallOfHate::constructor"),  # size=48, subsystem=Skills
    (0x0015ea90, "SkillBallOfHate::initRamps"),  # size=32, subsystem=Skills
    (0x0015eab0, "SkillDiseaseEffect::constructor"),  # size=48, subsystem=Skills
    (0x0015eae0, "SkillDiseaseEffect::initRamps"),  # size=44, subsystem=Skills
    (0x0015eb10, "SkillHateEffect::constructor"),  # size=48, subsystem=Skills
    (0x0015eb40, "SkillHateEffect::initRamps"),  # size=32, subsystem=Skills
    (0x00162bf0, "AnimationState::constructor"),  # size=460, subsystem=C++ Runtime
    (0x00162dc0, "AnimationState4::constructor"),  # size=588, subsystem=C++ Runtime
    (0x00163010, "AnimationState8::constructor"),  # size=588, subsystem=C++ Runtime
    (0x00164050, "AnimationState::~destructor"),  # size=128, subsystem=C++ Runtime
    (0x00166f30, "ResourceMap::constructor"),  # size=20, subsystem=C++ Runtime
    (0x00166f48, "ResourceMap::get"),  # size=76, subsystem=C++ Runtime
    (0x00180d08, "ParticleDef::constructor"),  # size=112, subsystem=Particles
    (0x00180d78, "ParticleDef::constructor"),  # size=36, subsystem=Particles
    (0x00186a70, "ParticleEmitterData::__eq"),  # size=232, subsystem=Particles
    (0x00194498, "ListHead::constructor"),  # size=8, subsystem=C++ Runtime
    (0x00194660, "ListSafeIterator::constructor"),  # size=160, subsystem=C++ Runtime
    (0x00194700, "ListSafeIterator::~destructor"),  # size=80, subsystem=C++ Runtime
    (0x00194750, "ListSafeIterator::next"),  # size=124, subsystem=C++ Runtime
    (0x001947d0, "Player::~destructor"),  # size=348, subsystem=Game Entities
    (0x00194930, "Player::constructor"),  # size=2208, subsystem=Game Entities
    (0x00195cb8, "Player::preCacheArmor"),  # size=1076, subsystem=Game Entities
    (0x001960f0, "Player::drawAttachments"),  # size=2224, subsystem=Game Entities
    (0x001969a0, "Player::runNewStyleSpells"),  # size=684, subsystem=Game Entities
    (0x00196c50, "Player::castNewStyle"),  # size=884, subsystem=Game Entities
    (0x00196fc8, "Player::msg_draw"),  # size=2220, subsystem=Game Entities
    (0x00197878, "Player::msg_run"),  # size=27496, subsystem=Game Entities
    (0x001a1e58, "Player::playerItemScan"),  # size=2280, subsystem=Game Entities
    (0x001a2740, "Player::playerDamageHandler"),  # size=2012, subsystem=Game Entities
    (0x001a2f20, "Player::playerRegenerateEnergy"),  # size=608, subsystem=Game Entities
    (0x001a3180, "Player::playerRegenerateHealth"),  # size=476, subsystem=Game Entities
    (0x001a3360, "Player::clipVelocityToFrustum"),  # size=648, subsystem=Game Entities
    (0x001a35e8, "Player::playerMove"),  # size=4288, subsystem=Game Entities
    (0x001a46a8, "Player::msg_hurt"),  # size=996, subsystem=Game Entities
    (0x001a4d50, "Player::setState"),  # size=296, subsystem=Game Entities
    (0x001a59c0, "Player::playerAttackEnemy"),  # size=1724, subsystem=Game Entities
    (0x001a6080, "Player::playerRecomputeDamage"),  # size=1756, subsystem=Game Entities
    (0x001a7698, "Player::resurectEffect"),  # size=1420, subsystem=Game Entities
    (0x001a7c28, "Player::playerAdvanceAnimation"),  # size=248, subsystem=Game Entities
    (0x001a7d20, "Player::playerBlockSparks"),  # size=1592, subsystem=Game Entities
    (0x001a8358, "Player::drinkPotion"),  # size=2088, subsystem=Game Entities
    (0x001a8b80, "playerProjectile::msg_draw"),  # size=384, subsystem=Renderer
    (0x001a8d00, "playerProjectile::msg_run"),  # size=2572, subsystem=Renderer
    (0x001a9710, "Player::playerFindTarget"),  # size=812, subsystem=Game Entities
    (0x001a9a40, "Player::playerNewQuickToggle"),  # size=740, subsystem=Game Entities
    (0x001a9d28, "Player::playerFindRandomAttackAnim"),  # size=936, subsystem=Game Entities
    (0x001aa0d0, "Player::maybeDrawMultiPlayerMarkers"),  # size=720, subsystem=Game Entities
    (0x001aa3a0, "Player::playerPlayRandomIdle"),  # size=632, subsystem=Game Entities
    (0x001aa618, "Player::playerProcessEffectTimers"),  # size=1212, subsystem=Game Entities
    (0x001aaad8, "Player::playerDrawWeaponEffects"),  # size=1200, subsystem=Game Entities
    (0x001aaf88, "Player::doSlamEffect"),  # size=608, subsystem=Game Entities
    (0x001ab800, "Player::consumeEnergy"),  # size=116, subsystem=Game Entities
    (0x001ab8e0, "Player::outsideFrustum"),  # size=164, subsystem=Game Entities
    (0x001ab988, "Player::msg_collision"),  # size=196, subsystem=Game Entities
    (0x001aba50, "Player::dismount"),  # size=64, subsystem=Game Entities
    (0x001aba90, "Player::isEnemy"),  # size=88, subsystem=Game Entities
    (0x001abce0, "Player::footFallSound"),  # size=132, subsystem=Game Entities
    (0x001abea0, "playerProjectile::constructor"),  # size=336, subsystem=Renderer
    (0x001abff0, "Player::playerNewQuickSpellToggle"),  # size=164, subsystem=Game Entities
    (0x001ac098, "Player::playerEvadeHandler"),  # size=200, subsystem=Game Entities
    (0x001ac160, "Player::playerIsAnimPlaying"),  # size=112, subsystem=Game Entities
    (0x001bc040, "ShopDaemon::constructor"),  # size=196, subsystem=C++ Runtime
    (0x001bc108, "ShopDaemon::msg_run"),  # size=52, subsystem=C++ Runtime
    (0x001d12d8, "PushTrigger::constructor"),  # size=404, subsystem=Game Props
    (0x001d1470, "Trigger::constructor"),  # size=256, subsystem=Game Props
    (0x001d1570, "Trigger::msg_run"),  # size=736, subsystem=Game Props
    (0x001d1850, "PushTrigger::msg_getPokeName"),  # size=268, subsystem=Game Props
    (0x001d1960, "PushTrigger::msg_poke"),  # size=148, subsystem=Game Props
    (0x001d19f8, "TriggerParams::constructor"),  # size=104, subsystem=C++ Runtime
    (0x001d1a60, "TriggerParams::msg_trigger"),  # size=44, subsystem=C++ Runtime
    (0x001d1a90, "Trigger::msg_load"),  # size=36, subsystem=Game Props
    (0x001d1ab8, "Trigger::msg_save"),  # size=36, subsystem=Game Props
    (0x001d1ae0, "Trigger::objectInside"),  # size=80, subsystem=Game Props
    (0x001d4088, "GutChunk::msg_run"),  # size=1304, subsystem=Renderer
    (0x001d45a0, "LightEffect::msg_run"),  # size=488, subsystem=Lighting
    (0x001d4788, "DummyDamager::msg_run"),  # size=1124, subsystem=Renderer
    (0x001d4bf0, "DummyDamager::msg_collision"),  # size=484, subsystem=Renderer
    (0x001d4dd8, "WaterSpout::msg_run"),  # size=2136, subsystem=Renderer
    (0x001d8c08, "GlowingCylinder::msg_draw"),  # size=840, subsystem=Game Entities
    (0x001d8f50, "GlowingCylinder::msg_run"),  # size=460, subsystem=Game Entities
    (0x001d9120, "Fire::msg_run"),  # size=832, subsystem=Game Props
    (0x001d9460, "FlyingText::msg_draw"),  # size=496, subsystem=Renderer
    (0x001d9650, "MissileTrap::msg_run"),  # size=616, subsystem=Game Props
    (0x001da5d0, "Shooter::msg_run"),  # size=1808, subsystem=Game Entities
    (0x001decf0, "IceChunk::msg_run"),  # size=264, subsystem=Game Entities
    (0x001df588, "PhIce::msg_run"),  # size=632, subsystem=Game Entities
    (0x001df800, "Ice::msg_run"),  # size=884, subsystem=Game Entities
    (0x001e0870, "LooseFire::msg_collision"),  # size=640, subsystem=Game Props
    (0x001e0af0, "FireEffect::msg_draw"),  # size=492, subsystem=Game Entities
    (0x001e0ce0, "poisonGasSpell::msg_run"),  # size=1196, subsystem=C++ Runtime
    (0x001e1190, "dustCloud::msg_run"),  # size=1052, subsystem=Projectiles
    (0x001e15b0, "GlowingShaft::msg_draw"),  # size=868, subsystem=Renderer
    (0x001e1918, "FrostStormIceShard::msg_draw"),  # size=292, subsystem=Game Entities
    (0x001e1a40, "FrostStormIceShard::msg_run"),  # size=1448, subsystem=Game Entities
    (0x001e1fe8, "FrostStormSpell::constructor"),  # size=1036, subsystem=C++ Runtime
    (0x001e23f8, "FrostStormSpell::msg_run"),  # size=3596, subsystem=C++ Runtime
    (0x001e3208, "RainOfFireSpell::constructor"),  # size=1060, subsystem=C++ Runtime
    (0x001e3630, "RainOfFireSpell::msg_run"),  # size=1596, subsystem=C++ Runtime
    (0x001e5048, "GutChunk::constructor"),  # size=188, subsystem=Renderer
    (0x001e5108, "GutChunk::constructor"),  # size=132, subsystem=Renderer
    (0x001e5190, "GutChunk::constructor"),  # size=160, subsystem=Renderer
    (0x001e5230, "GutChunk::msg_draw"),  # size=72, subsystem=Renderer
    (0x001e5278, "LightEffect::constructor"),  # size=648, subsystem=Lighting
    (0x001e5500, "RecallEffect::constructor"),  # size=188, subsystem=Game Entities
    (0x001e55c0, "RecallEffect::msg_run"),  # size=8, subsystem=Game Entities
    (0x001e55c8, "RecallEffect::msg_draw"),  # size=8, subsystem=Game Entities
    (0x001e55d0, "DummyDamager::constructor"),  # size=296, subsystem=Renderer
    (0x001e56f8, "DummyDamager::msg_draw"),  # size=8, subsystem=Renderer
    (0x001e5700, "WaterSpout::constructor"),  # size=232, subsystem=Renderer
    (0x001e57e8, "WaterSpout::msg_draw"),  # size=64, subsystem=Renderer
    (0x001e5828, "GlowingCylinder::constructor"),  # size=352, subsystem=Game Entities
    (0x001e5988, "Fire::constructor"),  # size=120, subsystem=Game Props
    (0x001e5a00, "FlyingText::constructor"),  # size=340, subsystem=Renderer
    (0x001e5b58, "FlyingText::msg_run"),  # size=112, subsystem=Renderer
    (0x001e5bc8, "MissileTrap::constructor"),  # size=172, subsystem=Game Props
    (0x001e5c78, "MissileTrap::msg_trigger"),  # size=44, subsystem=Game Props
    (0x001e5ca8, "Shooter::constructor"),  # size=216, subsystem=Game Entities
    (0x001e5d80, "Shooter::msg_save"),  # size=24, subsystem=Game Entities
    (0x001e5d98, "Shooter::msg_load"),  # size=24, subsystem=Game Entities
    (0x001e5db0, "FxCreatureState::~destructor"),  # size=44, subsystem=Game Entities
    (0x001e5de0, "IceChunk::constructor"),  # size=124, subsystem=Game Entities
    (0x001e5e60, "IceChunk::msg_draw"),  # size=68, subsystem=Game Entities
    (0x001e5ea8, "LooseIceChunk::constructor"),  # size=120, subsystem=Game Entities
    (0x001e5f20, "FrostStormIceChunk::constructor"),  # size=120, subsystem=Game Entities
    (0x001e6190, "PhIce::constructor"),  # size=96, subsystem=Game Entities
    (0x001e61f0, "Ice::constructor"),  # size=316, subsystem=Game Entities
    (0x001e6330, "Ice::msg_draw"),  # size=168, subsystem=Game Entities
    (0x001e6490, "LooseFire::constructor"),  # size=212, subsystem=Game Props
    (0x001e6568, "LooseFire::msg_run"),  # size=76, subsystem=Game Props
    (0x001e65b8, "FireEffect::constructor"),  # size=212, subsystem=Game Entities
    (0x001e6690, "FireEffect::msg_run"),  # size=108, subsystem=Game Entities
    (0x001e6700, "FireEffect::msg_collision"),  # size=8, subsystem=Game Entities
    (0x001e6708, "poisonGasSpell::constructor"),  # size=276, subsystem=C++ Runtime
    (0x001e6820, "poisonGasSpell::msg_draw"),  # size=8, subsystem=C++ Runtime
    (0x001e6828, "dustCloud::constructor"),  # size=228, subsystem=Projectiles
    (0x001e6910, "GlowingShaft::constructor"),  # size=180, subsystem=Renderer
    (0x001e69c8, "GlowingShaft::msg_run"),  # size=72, subsystem=Renderer
    (0x001e6a10, "FrostStormIceShard::constructor"),  # size=244, subsystem=Game Entities
    (0x001e6b08, "FrostStormSpell::msg_draw"),  # size=8, subsystem=C++ Runtime
    (0x001e6b30, "CloudGiant::constructor"),  # size=1404, subsystem=Game Entities
    (0x001e70b0, "CloudGiant::msg_run"),  # size=7304, subsystem=Game Entities
    (0x001e8d38, "CloudGiant::setState"),  # size=1448, subsystem=Game Entities
    (0x001e92e0, "BoltGoRound::constructor"),  # size=580, subsystem=Game Entities
    (0x001e9528, "BoltGoRound::msg_run"),  # size=1000, subsystem=Game Entities
    (0x001e9990, "CloudGiant::msg_draw"),  # size=112, subsystem=Game Entities
    (0x001e9a00, "CloudGiant::msg_save"),  # size=72, subsystem=Game Entities
    (0x001e9a48, "CloudGiant::msg_load"),  # size=88, subsystem=Game Entities
    (0x001e9aa0, "CloudGiant::msg_trigger"),  # size=192, subsystem=Game Entities
    (0x001e9b60, "CloudGiant::msg_hurt"),  # size=60, subsystem=Game Entities
    (0x001e9bc0, "Demon::constructor"),  # size=740, subsystem=Game Entities
    (0x001e9ea8, "Demon::initAttackVariant"),  # size=384, subsystem=Game Entities
    (0x001ea028, "Demon::msg_run"),  # size=3592, subsystem=Game Entities
    (0x001eae30, "Demon::setState"),  # size=1064, subsystem=Game Entities
    (0x001eb258, "Demon::dropWeapon"),  # size=236, subsystem=Game Entities
    (0x001eb348, "Demon::msg_draw"),  # size=108, subsystem=Game Entities
    (0x001eb3b8, "Demon::msg_save"),  # size=72, subsystem=Game Entities
    (0x001eb400, "Demon::msg_load"),  # size=88, subsystem=Game Entities
    (0x001eb458, "Demon::isEnemy"),  # size=132, subsystem=Game Entities
    (0x001eb4e0, "LavaMonster::constructor"),  # size=1340, subsystem=Game Entities
    (0x001eba20, "LavaMonster::msg_draw"),  # size=212, subsystem=Game Entities
    (0x001ebaf8, "LavaMonster::msg_run"),  # size=5540, subsystem=Game Entities
    (0x001ed0a0, "LavaMonster::msg_load"),  # size=348, subsystem=Game Entities
    (0x001ed200, "LavaMonster::setState"),  # size=992, subsystem=Game Entities
    (0x001ed5e0, "LavaBomb::msg_run"),  # size=2268, subsystem=Renderer
    (0x001edec0, "LavaBomb::msg_collision"),  # size=476, subsystem=Renderer
    (0x001ee1e8, "LavaMonster::msg_save"),  # size=144, subsystem=Game Entities
    (0x001ee278, "LavaMonster::loseBodyPart"),  # size=8, subsystem=Game Entities
    (0x001ee280, "LavaMonster::getModel"),  # size=32, subsystem=Game Entities
    (0x001ee2a0, "LavaMonster::getTexture"),  # size=32, subsystem=Game Entities
    (0x001ee2c0, "LavaBomb::msg_draw"),  # size=172, subsystem=Renderer
    (0x001ee390, "Cat::constructor"),  # size=404, subsystem=Game Entities
    (0x001ee528, "Cat::msg_run"),  # size=884, subsystem=Game Entities
    (0x001ee8a0, "Cat::setState"),  # size=460, subsystem=Game Entities
    (0x001eea70, "Cat::switchToWalk"),  # size=396, subsystem=Game Entities
    (0x001eec00, "Cat::switchToRun"),  # size=396, subsystem=Game Entities
    (0x001eed90, "Cat::msg_draw"),  # size=96, subsystem=Game Entities
    (0x001eedf0, "Cat::msg_collision"),  # size=120, subsystem=Game Entities
    (0x001eee68, "Cat::addTurnAnimation"),  # size=180, subsystem=Game Entities
    (0x001eef20, "Cat::subTurnAnimation"),  # size=16, subsystem=Game Entities
    (0x001eef30, "Cat::readyToSwitch"),  # size=16, subsystem=Game Entities
    (0x001eef40, "Badger::constructor"),  # size=924, subsystem=C++ Runtime
    (0x001ef2e0, "Badger::msg_run"),  # size=1988, subsystem=C++ Runtime
    (0x001efaa8, "Badger::setState"),  # size=920, subsystem=C++ Runtime
    (0x001efe40, "Badger::msg_draw"),  # size=100, subsystem=C++ Runtime
    (0x001efea8, "Badger::msg_moveCollision"),  # size=8, subsystem=C++ Runtime
    (0x001efeb0, "Critter::constructor"),  # size=1944, subsystem=Game Entities
    (0x001f0648, "Critter::msg_run"),  # size=2300, subsystem=Game Entities
    (0x001f0f48, "Critter::setState"),  # size=756, subsystem=Game Entities
    (0x001f1240, "Critter::specificInit"),  # size=1488, subsystem=Game Entities
    (0x001f1810, "Critter::msg_draw"),  # size=228, subsystem=Game Entities
    (0x001f18f8, "Critter::msg_load"),  # size=8, subsystem=Game Entities
    (0x001f1900, "Critter::msg_save"),  # size=8, subsystem=Game Entities
    (0x001f1908, "Critter::msg_hurt"),  # size=8, subsystem=Game Entities
    (0x001f1910, "Critter::msg_collision"),  # size=172, subsystem=Game Entities
    (0x001f19c0, "Generator::constructor"),  # size=400, subsystem=Game Props
    (0x001f1b50, "Generator::msg_run"),  # size=1180, subsystem=Game Props
    (0x001f1ff0, "Generator::msg_draw"),  # size=8, subsystem=Game Props
    (0x001f1ff8, "Generator::msg_trigger"),  # size=140, subsystem=Game Props
    (0x001f2088, "Generator::msg_save"),  # size=36, subsystem=Game Props
    (0x001f20b0, "Generator::msg_load"),  # size=36, subsystem=Game Props
    (0x001f20d8, "Generator::setState"),  # size=112, subsystem=Game Props
    (0x001f2148, "Scorpion::constructor"),  # size=720, subsystem=Game Entities
    (0x001f2418, "Scorpion::msg_run"),  # size=1456, subsystem=Game Entities
    (0x001f29c8, "Scorpion::setState"),  # size=1020, subsystem=Game Entities
    (0x001f2dc8, "Scorpion::msg_draw"),  # size=56, subsystem=Game Entities
    (0x001f2e00, "Scorpion::loseBodyPart"),  # size=260, subsystem=Game Entities
    (0x001f2f08, "Soul::constructor"),  # size=520, subsystem=Game Entities
    (0x001f3110, "Soul::msg_draw"),  # size=508, subsystem=Game Entities
    (0x001f3310, "Soul::msg_run"),  # size=4384, subsystem=Game Entities
    (0x001f4430, "Soul::msg_hurt"),  # size=664, subsystem=Game Entities
    (0x001f46c8, "Soul::setState"),  # size=1672, subsystem=Game Entities
    (0x001f4d50, "Soul::demonNear"),  # size=268, subsystem=Game Entities
    (0x001f4ee8, "Soul::msg_trigger"),  # size=84, subsystem=Game Entities
    (0x001f4f40, "Soul::msg_save"),  # size=104, subsystem=Game Entities
    (0x001f4fa8, "Soul::msg_load"),  # size=104, subsystem=Game Entities
    (0x001f5010, "Soul::getModel"),  # size=32, subsystem=Game Entities
    (0x001f5050, "Ulthork::constructor"),  # size=772, subsystem=C++ Runtime
    (0x001f5358, "Ulthork::msg_draw"),  # size=272, subsystem=C++ Runtime
    (0x001f5468, "Ulthork::msg_run"),  # size=2088, subsystem=C++ Runtime
    (0x001f5c90, "Ulthork::setState"),  # size=1368, subsystem=C++ Runtime
    (0x001f61e8, "Ulthork::msg_save"),  # size=84, subsystem=C++ Runtime
    (0x001f6240, "Ulthork::msg_load"),  # size=168, subsystem=C++ Runtime
    (0x001f62e8, "Ghoul::constructor"),  # size=852, subsystem=Game Entities
    (0x001f6640, "Ghoul::msg_run"),  # size=2012, subsystem=Game Entities
    (0x001f6e20, "Ghoul::setState"),  # size=1624, subsystem=Game Entities
    (0x001f7478, "Ghoul::loseBodyPart"),  # size=320, subsystem=Game Entities
    (0x001f75b8, "Ghoul::msg_draw"),  # size=40, subsystem=Game Entities
    (0x001f75e0, "Ghoul::msg_alert"),  # size=188, subsystem=Game Entities
    (0x001f76a0, "Nightmare::constructor"),  # size=280, subsystem=Game Entities
    (0x001f77b8, "Nightmare::msg_run"),  # size=356, subsystem=Game Entities
    (0x001f7920, "Nightmare::setState"),  # size=484, subsystem=Game Entities
    (0x001f7b08, "Nightmare::turnToFace"),  # size=300, subsystem=Game Entities
    (0x001f7c38, "Nightmare::msg_draw"),  # size=40, subsystem=Game Entities
    (0x001f7c60, "Mermaid::constructor"),  # size=284, subsystem=Game Entities
    (0x001f7d80, "Mermaid::msg_run"),  # size=392, subsystem=Game Entities
    (0x001f7f08, "Mermaid::setState"),  # size=344, subsystem=Game Entities
    (0x001f8060, "Mermaid::msg_draw"),  # size=40, subsystem=Game Entities
    (0x001f8088, "SeaMonster::constructor"),  # size=532, subsystem=Game Entities
    (0x001f82a0, "SeaMonster::msg_run"),  # size=1232, subsystem=Game Entities
    (0x001f8770, "SeaMonster::setState"),  # size=1008, subsystem=Game Entities
    (0x001f8b60, "SeaMonster::msg_draw"),  # size=40, subsystem=Game Entities
    (0x001f8b88, "SeaMonster::msg_moveCollision"),  # size=8, subsystem=Game Entities
    (0x001f8b90, "SeaMonster::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x001f8bc8, "SeaMonster::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x001f8c08, "Innoruuk::constructor"),  # size=1348, subsystem=Game Entities
    (0x001f9150, "Innoruuk::msg_run"),  # size=11684, subsystem=Game Entities
    (0x001fbef8, "Innoruuk::setState"),  # size=1724, subsystem=Game Entities
    (0x001fc5b8, "Innoruuk::updateEnemy"),  # size=772, subsystem=Game Entities
    (0x001fc8c0, "Innoruuk::deathEffect"),  # size=824, subsystem=Game Entities
    (0x001fcbf8, "HateBeam::constructor"),  # size=372, subsystem=Game Entities
    (0x001fcd70, "HateBeam::msg_run"),  # size=2668, subsystem=Game Entities
    (0x001fd7e0, "HateProjectile::constructor"),  # size=452, subsystem=Projectiles
    (0x001fd9a8, "HateProjectile::msg_run"),  # size=3268, subsystem=Projectiles
    (0x001fe670, "HateProjectile::msg_draw"),  # size=284, subsystem=Projectiles
    (0x001fe790, "HateProjectile::buildShockChainList"),  # size=320, subsystem=Projectiles
    (0x001fe8d0, "SpellHateEffect::run"),  # size=548, subsystem=Spells
    (0x001feaf8, "HateSoul::constructor"),  # size=508, subsystem=Game Entities
    (0x001fecf8, "HateSoul::msg_run"),  # size=980, subsystem=Game Entities
    (0x001ff458, "Innoruuk::msg_draw"),  # size=172, subsystem=Game Entities
    (0x001ff508, "Innoruuk::msg_trigger"),  # size=96, subsystem=Game Entities
    (0x001ff568, "Innoruuk::msg_hurt"),  # size=64, subsystem=Game Entities
    (0x001ff5a8, "HateBeam::~destructor"),  # size=124, subsystem=Game Entities
    (0x001ff628, "HateProjectile::~destructor"),  # size=140, subsystem=Projectiles
    (0x001ff6b8, "HateProjectile::alreadyChained"),  # size=64, subsystem=Projectiles
    (0x001ff6f8, "SpellHateEffect::constructor"),  # size=264, subsystem=Spells
    (0x001ff820, "Froglock::constructor"),  # size=880, subsystem=Game Entities
    (0x001ffb90, "Froglock::initAttackVariant"),  # size=636, subsystem=Game Entities
    (0x001ffe10, "Froglock::msg_draw"),  # size=228, subsystem=Game Entities
    (0x001ffef8, "Froglock::msg_run"),  # size=3040, subsystem=Game Entities
    (0x00200ad8, "Froglock::setState"),  # size=1552, subsystem=Game Entities
    (0x002010e8, "Froglock::msg_save"),  # size=84, subsystem=Game Entities
    (0x00201140, "Froglock::msg_load"),  # size=116, subsystem=Game Entities
    (0x002011b8, "Froglock::bCrossingWater"),  # size=60, subsystem=Game Entities
    (0x002011f8, "Gnome::constructor"),  # size=472, subsystem=Renderer
    (0x002013d0, "Gnome::msg_draw"),  # size=472, subsystem=Renderer
    (0x002015a8, "Gnome::msg_run"),  # size=1016, subsystem=Renderer
    (0x002019a0, "Gnome::setState"),  # size=764, subsystem=Renderer
    (0x00201ca0, "GnomeNavigator::constructor"),  # size=340, subsystem=Game Entities
    (0x00201df8, "GnomeNavigator::msg_draw"),  # size=472, subsystem=Game Entities
    (0x00201fd0, "GnomeNavigator::msg_run"),  # size=476, subsystem=Game Entities
    (0x002021b0, "GnomeNavigator::setState"),  # size=564, subsystem=Game Entities
    (0x002023e8, "Gnome::initType"),  # size=160, subsystem=Renderer
    (0x00202488, "Gnome::msg_collision"),  # size=256, subsystem=Renderer
    (0x00202588, "Gnome::msg_moveCollision"),  # size=236, subsystem=Renderer
    (0x00202678, "Cyclops::constructor"),  # size=912, subsystem=Game Entities
    (0x00202a08, "Cyclops::msg_run"),  # size=2520, subsystem=Game Entities
    (0x002033e0, "Cyclops::setState"),  # size=1052, subsystem=Game Entities
    (0x00203800, "Cyclops::dropItem"),  # size=236, subsystem=Game Entities
    (0x002038f0, "Cyclops::generateDust"),  # size=604, subsystem=Game Entities
    (0x00203bc8, "Cyclops::msg_draw"),  # size=68, subsystem=Game Entities
    (0x00203c10, "Cyclops::msg_load"),  # size=80, subsystem=Game Entities
    (0x00203c60, "Cyclops::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x00203c98, "Cyclops::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x00203cf8, "Wraith::constructor"),  # size=528, subsystem=Game Entities
    (0x00203f08, "Wraith::msg_run"),  # size=3400, subsystem=Game Entities
    (0x00204c50, "Wraith::setState"),  # size=932, subsystem=Game Entities
    (0x00204ff8, "Wraith::isEnemy"),  # size=432, subsystem=Game Entities
    (0x00205258, "Wraith::msg_draw"),  # size=84, subsystem=Game Entities
    (0x002052b0, "Wraith::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x002052e8, "Wraith::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x00205368, "Ant::constructor"),  # size=1556, subsystem=Game Entities
    (0x00205980, "Ant::msg_run"),  # size=3236, subsystem=Game Entities
    (0x00206628, "Ant::setState"),  # size=1100, subsystem=Game Entities
    (0x00206a78, "Ant::loseBodyPart"),  # size=400, subsystem=Game Entities
    (0x00206c08, "AntQueen::constructor"),  # size=672, subsystem=Game Entities
    (0x00206ea8, "AntQueen::msg_run"),  # size=2540, subsystem=Game Entities
    (0x00207898, "AntQueen::setState"),  # size=2068, subsystem=Game Entities
    (0x002080b0, "AntQueen::findEvadeDestination"),  # size=548, subsystem=Game Entities
    (0x002082d8, "AntQueen::addTurnAnimation"),  # size=424, subsystem=Game Entities
    (0x00208480, "AntWave::msg_draw"),  # size=360, subsystem=Audio
    (0x002085e8, "AntWave::msg_run"),  # size=332, subsystem=Audio
    (0x00208820, "Ant::msg_draw"),  # size=76, subsystem=Game Entities
    (0x00208870, "Ant::msg_save"),  # size=72, subsystem=Game Entities
    (0x002088b8, "Ant::msg_load"),  # size=124, subsystem=Game Entities
    (0x00208938, "AntQueen::msg_draw"),  # size=104, subsystem=Game Entities
    (0x002089a0, "AntQueen::msg_trigger"),  # size=136, subsystem=Game Entities
    (0x00208a28, "AntQueen::msg_hurt"),  # size=88, subsystem=Game Entities
    (0x00208a80, "AntQueen::loseBodyPart"),  # size=232, subsystem=Game Entities
    (0x00208b68, "AntQueen::subTurnAnimation"),  # size=128, subsystem=Game Entities
    (0x00208be8, "AntWave::constructor"),  # size=232, subsystem=Audio
    (0x00208cd0, "AntWave::~destructor"),  # size=144, subsystem=Audio
    (0x00208d80, "Spider::constructor"),  # size=544, subsystem=C++ Runtime
    (0x00208fa0, "Spider::msg_run"),  # size=1236, subsystem=C++ Runtime
    (0x00209478, "Spider::setState"),  # size=824, subsystem=C++ Runtime
    (0x002097b0, "SmallSpider::constructor"),  # size=324, subsystem=C++ Runtime
    (0x002098f8, "SmallSpider::msg_run"),  # size=280, subsystem=C++ Runtime
    (0x00209a10, "SmallSpider::setState"),  # size=524, subsystem=C++ Runtime
    (0x00209c20, "BlackWidow::constructor"),  # size=896, subsystem=Game Entities
    (0x00209fa0, "BlackWidow::msg_run"),  # size=3244, subsystem=Game Entities
    (0x0020ac50, "BlackWidow::setState"),  # size=1224, subsystem=Game Entities
    (0x0020b118, "BlackWidow::loseBodyPart"),  # size=468, subsystem=Game Entities
    (0x0020b2f0, "SpiderQueen::constructor"),  # size=1024, subsystem=Game Entities
    (0x0020b6f0, "SpiderQueen::msg_run"),  # size=5740, subsystem=Game Entities
    (0x0020cd60, "SpiderQueen::msg_hurt"),  # size=464, subsystem=Game Entities
    (0x0020cf30, "SpiderQueen::setState"),  # size=1516, subsystem=Game Entities
    (0x0020dc68, "Web::start"),  # size=380, subsystem=Renderer
    (0x0020dde8, "Web::draw"),  # size=588, subsystem=Renderer
    (0x0020e038, "Web::run"),  # size=1112, subsystem=Renderer
    (0x0020e490, "WebTrap::constructor"),  # size=708, subsystem=Game Props
    (0x0020e758, "WebTrap::constructor"),  # size=400, subsystem=Game Props
    (0x0020e8e8, "WebTrap::msg_draw"),  # size=744, subsystem=Game Props
    (0x0020ebd0, "WebTrap::msg_run"),  # size=1984, subsystem=Game Props
    (0x0020f390, "PoisonProjectile::msg_run"),  # size=908, subsystem=C++ Runtime
    (0x0020f808, "Spider::msg_draw"),  # size=164, subsystem=C++ Runtime
    (0x0020f8b0, "Spider::getRunSpeed"),  # size=16, subsystem=C++ Runtime
    (0x0020f8c0, "Spider::getWalkSpeed"),  # size=16, subsystem=C++ Runtime
    (0x0020f8d0, "SmallSpider::msg_draw"),  # size=72, subsystem=C++ Runtime
    (0x0020f918, "SmallSpider::msg_collision"),  # size=120, subsystem=C++ Runtime
    (0x0020f990, "BlackWidow::msg_draw"),  # size=40, subsystem=Game Entities
    (0x0020f9b8, "SpiderQueen::msg_trigger"),  # size=112, subsystem=Game Entities
    (0x0020fa28, "SpiderQueen::msg_draw"),  # size=76, subsystem=Game Entities
    (0x0020fa78, "SpiderQueen::canGrab"),  # size=80, subsystem=Game Entities
    (0x0020fac8, "Web::constructor"),  # size=24, subsystem=Renderer
    (0x0020fae0, "Web::reset"),  # size=12, subsystem=Renderer
    (0x0020faf0, "Web::start"),  # size=148, subsystem=Renderer
    (0x0020fb88, "Web::breakWeb"),  # size=52, subsystem=Renderer
    (0x0020fbc0, "Web::bDrawing"),  # size=12, subsystem=Renderer
    (0x0020fbd0, "Web::bActive"),  # size=12, subsystem=Renderer
    (0x0020fbe0, "PoisonProjectile::constructor"),  # size=356, subsystem=C++ Runtime
    (0x0020fd48, "PoisonProjectile::msg_draw"),  # size=200, subsystem=C++ Runtime
    (0x0020fe10, "PoisonProjectile::msg_collision"),  # size=280, subsystem=C++ Runtime
    (0x0020ff48, "FireBeetle::constructor"),  # size=1008, subsystem=Renderer
    (0x00210338, "FireBeetle::msg_draw"),  # size=744, subsystem=Renderer
    (0x00210620, "FireBeetle::msg_run"),  # size=2668, subsystem=Renderer
    (0x00211090, "FireBeetle::setState"),  # size=1416, subsystem=Renderer
    (0x00211618, "FireBeetle::msg_moveCollision"),  # size=372, subsystem=Renderer
    (0x00211790, "FireBeetle::loseBodyPart"),  # size=340, subsystem=Renderer
    (0x002118e8, "FireFly::constructor"),  # size=484, subsystem=Game Entities
    (0x00211ad0, "FireFly::msg_draw"),  # size=564, subsystem=Game Entities
    (0x00211d08, "FireFly::msg_run"),  # size=612, subsystem=Game Entities
    (0x00211f70, "beetleProjectile::msg_run"),  # size=1204, subsystem=Physics
    (0x00212518, "FireFly::setState"),  # size=8, subsystem=Game Entities
    (0x00212520, "beetleProjectile::constructor"),  # size=244, subsystem=Physics
    (0x00212618, "beetleProjectile::msg_draw"),  # size=8, subsystem=Physics
    (0x00212620, "beetleProjectile::msg_collision"),  # size=128, subsystem=Physics
    (0x002126c0, "Switch::constructor"),  # size=304, subsystem=C++ Runtime
    (0x002127f0, "DoorSwing::constructor"),  # size=352, subsystem=Game Props
    (0x00212950, "DoorSwing::msg_poke"),  # size=952, subsystem=Game Props
    (0x00212d08, "DoorSwing::msg_load"),  # size=216, subsystem=Game Props
    (0x00212de0, "DoorSwing::msg_run"),  # size=292, subsystem=Game Props
    (0x00212f08, "DoorSecret::constructor"),  # size=332, subsystem=Game Props
    (0x00213058, "DoorSecret::msg_poke"),  # size=260, subsystem=Game Props
    (0x00213160, "DoorSecret::msg_run"),  # size=348, subsystem=Game Props
    (0x002132c0, "FloorSwitch::constructor"),  # size=296, subsystem=Game Props
    (0x002133e8, "FloorSwitch::msg_run"),  # size=796, subsystem=Game Props
    (0x00213708, "FallPlatform::constructor"),  # size=348, subsystem=C++ Runtime
    (0x00213868, "FallPlatform::findPath"),  # size=436, subsystem=C++ Runtime
    (0x00213a20, "FallPlatform::msg_run"),  # size=1456, subsystem=C++ Runtime
    (0x00213fd0, "FireTrail::msg_collision"),  # size=384, subsystem=Game Entities
    (0x00214150, "FireTrail::msg_run"),  # size=680, subsystem=Game Entities
    (0x002143f8, "FireTrailMaker::constructor"),  # size=752, subsystem=Game Entities
    (0x002146e8, "FireTrailMaker::msg_run"),  # size=860, subsystem=Game Entities
    (0x00214a48, "Savepoint::constructor"),  # size=428, subsystem=Game Props
    (0x00214bf8, "Savepoint::msg_run"),  # size=2424, subsystem=Game Props
    (0x00215570, "Savepoint::updatePlayersReady"),  # size=392, subsystem=Game Props
    (0x002156f8, "Savepoint::msg_draw"),  # size=536, subsystem=Game Props
    (0x00215910, "Savepoint::msg_getPokeName"),  # size=356, subsystem=Game Props
    (0x00215a78, "RollDoor::constructor"),  # size=368, subsystem=C++ Runtime
    (0x00215be8, "RollDoor::msg_run"),  # size=236, subsystem=C++ Runtime
    (0x00215cd8, "Lever::msg_getPokeName"),  # size=336, subsystem=Game Props
    (0x00215e28, "Lever::msg_run"),  # size=300, subsystem=Game Props
    (0x00215f58, "WeaponRack::constructor"),  # size=448, subsystem=Renderer
    (0x00216118, "WeaponRack::msg_draw"),  # size=392, subsystem=Renderer
    (0x002162a0, "Counter::msg_trigger"),  # size=224, subsystem=C++ Runtime
    (0x00216380, "Teleporter::msg_run"),  # size=636, subsystem=Renderer
    (0x00216600, "Blocker::constructor"),  # size=336, subsystem=Game Entities
    (0x00216750, "PointSourceSound::msg_run"),  # size=296, subsystem=Audio
    (0x00216878, "CdEyeball::msg_draw"),  # size=244, subsystem=C++ Runtime
    (0x00216970, "Sparks::msg_run"),  # size=1716, subsystem=Renderer
    (0x00217028, "Sparks::msg_collision"),  # size=544, subsystem=Renderer
    (0x00217248, "IceBall::constructor"),  # size=396, subsystem=Projectiles
    (0x002173d8, "IceBall::msg_run"),  # size=1160, subsystem=Projectiles
    (0x00217860, "Container::msg_load"),  # size=252, subsystem=Game Props
    (0x00217960, "Container::msg_collision"),  # size=212, subsystem=Game Props
    (0x00217a38, "Container::msg_run"),  # size=3416, subsystem=Game Props
    (0x00218790, "Chest::constructor"),  # size=596, subsystem=Game Props
    (0x002189e8, "Chest::msg_run"),  # size=1228, subsystem=Game Props
    (0x00218eb8, "Chest::msg_poke"),  # size=1916, subsystem=Game Props
    (0x00219638, "LostSoul::constructor"),  # size=540, subsystem=Game Entities
    (0x00219858, "LostSoul::msg_run"),  # size=744, subsystem=Game Entities
    (0x00219b40, "Root::constructor"),  # size=992, subsystem=C++ Runtime
    (0x00219f20, "Root::msg_run"),  # size=1280, subsystem=C++ Runtime
    (0x0021a420, "OniBall::constructor"),  # size=444, subsystem=Game Entities
    (0x0021a5e0, "OniBall::msg_run"),  # size=1292, subsystem=Game Entities
    (0x0021aaf0, "OniBall::msg_collision"),  # size=364, subsystem=Game Entities
    (0x0021ac60, "UnholyAura::msg_run"),  # size=1588, subsystem=Game Entities
    (0x0021b298, "Trap::msg_run"),  # size=408, subsystem=Game Props
    (0x0021bcc0, "WorldPart::constructor"),  # size=240, subsystem=C++ Runtime
    (0x0021bdb0, "WorldPart::~destructor"),  # size=140, subsystem=C++ Runtime
    (0x0021be40, "Switch::msg_getPokeName"),  # size=60, subsystem=C++ Runtime
    (0x0021be80, "Switch::msg_poke"),  # size=108, subsystem=C++ Runtime
    (0x0021bef0, "DoorSwing::msg_getPokeName"),  # size=96, subsystem=Game Props
    (0x0021bf50, "DoorSwing::msg_trigger"),  # size=52, subsystem=Game Props
    (0x0021bf88, "DoorSwing::msg_presave"),  # size=8, subsystem=Game Props
    (0x0021bf90, "DoorSwing::msg_save"),  # size=56, subsystem=Game Props
    (0x0021bfc8, "DoorSecret::msg_getPokeName"),  # size=60, subsystem=Game Props
    (0x0021c008, "DoorSecret::msg_trigger"),  # size=68, subsystem=Game Props
    (0x0021c050, "DoorSecret::msg_save"),  # size=24, subsystem=Game Props
    (0x0021c068, "DoorSecret::msg_load"),  # size=160, subsystem=Game Props
    (0x0021c108, "FloorSwitch::msg_save"),  # size=24, subsystem=Game Props
    (0x0021c120, "FloorSwitch::msg_load"),  # size=24, subsystem=Game Props
    (0x0021c138, "FallPlatform::msg_trigger"),  # size=80, subsystem=C++ Runtime
    (0x0021c188, "FallPlatform::msg_save"),  # size=24, subsystem=C++ Runtime
    (0x0021c1a0, "FallPlatform::msg_load"),  # size=24, subsystem=C++ Runtime
    (0x0021c1b8, "FireTrail::constructor"),  # size=352, subsystem=Game Entities
    (0x0021c318, "Savepoint::saveActivate"),  # size=12, subsystem=Game Props
    (0x0021c328, "Savepoint::msg_poke"),  # size=108, subsystem=Game Props
    (0x0021c398, "Savepoint::msg_save"),  # size=56, subsystem=Game Props
    (0x0021c3d0, "Savepoint::msg_load"),  # size=204, subsystem=Game Props
    (0x0021c4a0, "RollDoor::msg_getPokeName"),  # size=60, subsystem=C++ Runtime
    (0x0021c4e0, "RollDoor::msg_poke"),  # size=116, subsystem=C++ Runtime
    (0x0021c558, "RollDoor::msg_presave"),  # size=8, subsystem=C++ Runtime
    (0x0021c560, "RollDoor::msg_save"),  # size=60, subsystem=C++ Runtime
    (0x0021c5a0, "RollDoor::msg_load"),  # size=180, subsystem=C++ Runtime
    (0x0021c658, "RollDoor::msg_trigger"),  # size=52, subsystem=C++ Runtime
    (0x0021c690, "RollDoor::msg_draw"),  # size=212, subsystem=C++ Runtime
    (0x0021c768, "PokeReflector::constructor"),  # size=104, subsystem=Game Entities
    (0x0021c7d0, "PokeReflector::msg_getPokeName"),  # size=160, subsystem=Game Entities
    (0x0021c870, "PokeReflector::msg_poke"),  # size=172, subsystem=Game Entities
    (0x0021c920, "Lever::constructor"),  # size=128, subsystem=Game Props
    (0x0021c9a0, "Lever::msg_save"),  # size=60, subsystem=Game Props
    (0x0021c9e0, "Lever::msg_load"),  # size=112, subsystem=Game Props
    (0x0021ca50, "Lever::msg_poke"),  # size=132, subsystem=Game Props
    (0x0021cad8, "Lever::msg_draw"),  # size=236, subsystem=Game Props
    (0x0021cbc8, "WeaponRack::msg_getPokeName"),  # size=60, subsystem=Renderer
    (0x0021cc08, "WeaponRack::msg_poke"),  # size=8, subsystem=Renderer
    (0x0021cc10, "Timer::constructor"),  # size=96, subsystem=Game Props
    (0x0021cc70, "Timer::msg_trigger"),  # size=88, subsystem=Game Props
    (0x0021ccc8, "Timer::msg_run"),  # size=64, subsystem=Game Props
    (0x0021cd08, "Counter::constructor"),  # size=96, subsystem=C++ Runtime
    (0x0021cd68, "Counter::msg_save"),  # size=24, subsystem=C++ Runtime
    (0x0021cd80, "Counter::msg_load"),  # size=24, subsystem=C++ Runtime
    (0x0021cd98, "Weather::constructor"),  # size=96, subsystem=Game Entities
    (0x0021cdf8, "Weather::msg_run"),  # size=8, subsystem=Game Entities
    (0x0021ce00, "Teleporter::constructor"),  # size=120, subsystem=Renderer
    (0x0021ce78, "Teleporter::msg_draw"),  # size=8, subsystem=Renderer
    (0x0021ce80, "Teleporter::setState"),  # size=8, subsystem=Renderer
    (0x0021ce88, "TestLocation::constructor"),  # size=128, subsystem=C++ Runtime
    (0x0021cf08, "VehicleBodySphere::constructor"),  # size=124, subsystem=Physics
    (0x0021cf88, "VehicleBodySphere::msg_collision"),  # size=48, subsystem=Physics
    (0x0021cfb8, "PointSourceSound::constructor"),  # size=192, subsystem=Audio
    (0x0021d078, "PointSourceSound::~destructor"),  # size=124, subsystem=Audio
    (0x0021d0f8, "CdEyeball::constructor"),  # size=228, subsystem=C++ Runtime
    (0x0021d1e0, "CdEyeball::msg_run"),  # size=192, subsystem=C++ Runtime
    (0x0021d2a0, "Sparks::constructor"),  # size=432, subsystem=Renderer
    (0x0021d450, "Sparks::msg_draw"),  # size=144, subsystem=Renderer
    (0x0021d4e0, "IceBall::msg_draw"),  # size=148, subsystem=Projectiles
    (0x0021d578, "Container::constructor"),  # size=180, subsystem=Game Props
    (0x0021d630, "Container::msg_save"),  # size=192, subsystem=Game Props
    (0x0021d6f0, "Container::constructor"),  # size=380, subsystem=Game Props
    (0x0021d870, "Container::msg_hurt"),  # size=144, subsystem=Game Props
    (0x0021d900, "Container::msg_draw"),  # size=192, subsystem=Game Props
    (0x0021d9c0, "Container::msg_getPokeName"),  # size=72, subsystem=Game Props
    (0x0021da08, "Container::msg_poke"),  # size=96, subsystem=Game Props
    (0x0021da68, "Chest::msg_save"),  # size=72, subsystem=Game Props
    (0x0021dab0, "Chest::msg_load"),  # size=220, subsystem=Game Props
    (0x0021db90, "Chest::msg_draw"),  # size=240, subsystem=Game Props
    (0x0021dc80, "Chest::msg_getPokeName"),  # size=176, subsystem=Game Props
    (0x0021dd30, "LostSoul::msg_draw"),  # size=8, subsystem=Game Entities
    (0x0021dd38, "Root::msg_draw"),  # size=8, subsystem=C++ Runtime
    (0x0021dd40, "OniBall::msg_draw"),  # size=8, subsystem=Game Entities
    (0x0021dd48, "UnholyAura::constructor"),  # size=252, subsystem=Game Entities
    (0x0021de48, "UnholyAura::msg_draw"),  # size=8, subsystem=Game Entities
    (0x0021de50, "Trap::constructor"),  # size=156, subsystem=Game Props
    (0x0021def0, "Trap::msg_draw"),  # size=8, subsystem=Game Props
    (0x0021e548, "AutoObject::constructor"),  # size=1732, subsystem=Game Entities
    (0x0021ec10, "AutoObject::msg_draw"),  # size=728, subsystem=Game Entities
    (0x0021eee8, "AutoChest::constructor"),  # size=704, subsystem=Game Props
    (0x0021f1a8, "AutoChest::msg_run"),  # size=1328, subsystem=Game Props
    (0x0021f6d8, "AutoChest::msg_poke"),  # size=448, subsystem=Game Props
    (0x0021f898, "AutoChest::spawnItems"),  # size=2528, subsystem=Game Props
    (0x00220278, "AutoProp::constructor"),  # size=1328, subsystem=Game Props
    (0x002207a8, "AutoProp::msg_run"),  # size=652, subsystem=Game Props
    (0x00220a38, "AutoProp::msg_getPokeName"),  # size=392, subsystem=Game Props
    (0x00220bc0, "AutoProp::advanceState"),  # size=876, subsystem=Game Props
    (0x00220f30, "AutoProp::setState"),  # size=272, subsystem=Game Props
    (0x00221040, "AutoProp::setPassableState"),  # size=212, subsystem=Game Props
    (0x00221118, "AutoContainer::constructor"),  # size=1876, subsystem=C++ Runtime
    (0x00221870, "AutoContainer::~destructor"),  # size=204, subsystem=C++ Runtime
    (0x00221940, "AutoContainer::msg_collision"),  # size=220, subsystem=C++ Runtime
    (0x00221a20, "AutoContainer::msg_run"),  # size=4124, subsystem=C++ Runtime
    (0x00222a40, "AddParticle::constructor"),  # size=368, subsystem=Particles
    (0x00222bb0, "AddParticle::constructor"),  # size=368, subsystem=Particles
    (0x00222d20, "AddParticle::particleInit"),  # size=1692, subsystem=Particles
    (0x002233c0, "AddParticle::lightInit"),  # size=932, subsystem=Particles
    (0x00223768, "AddParticle::draw"),  # size=1136, subsystem=Particles
    (0x00223bd8, "AutoPropLP::constructor"),  # size=1828, subsystem=Game Props
    (0x00224300, "AutoPropLP::msg_draw"),  # size=976, subsystem=Game Props
    (0x002246d0, "AutoPropLP::msg_run"),  # size=636, subsystem=Game Props
    (0x00224aa0, "AutoObject::msg_run"),  # size=8, subsystem=Game Entities
    (0x00224aa8, "AutoObject::msg_save"),  # size=8, subsystem=Game Entities
    (0x00224ab0, "AutoObject::msg_load"),  # size=8, subsystem=Game Entities
    (0x00224ab8, "AutoChest::msg_save"),  # size=72, subsystem=Game Props
    (0x00224b00, "AutoChest::msg_load"),  # size=188, subsystem=Game Props
    (0x00224bc0, "AutoChest::msg_getPokeName"),  # size=176, subsystem=Game Props
    (0x00224c70, "AutoProp::~destructor"),  # size=140, subsystem=Game Props
    (0x00224d00, "AutoProp::msg_save"),  # size=24, subsystem=Game Props
    (0x00224d18, "AutoProp::msg_load"),  # size=84, subsystem=Game Props
    (0x00224d70, "AutoProp::msg_hurt"),  # size=264, subsystem=Game Props
    (0x00224e78, "AutoProp::msg_poke"),  # size=76, subsystem=Game Props
    (0x00224ec8, "AutoProp::msg_trigger"),  # size=256, subsystem=Game Props
    (0x00224fc8, "AutoContainer::msg_load"),  # size=104, subsystem=C++ Runtime
    (0x00225030, "AutoContainer::msg_save"),  # size=24, subsystem=C++ Runtime
    (0x00225048, "AutoContainer::msg_getPokeName"),  # size=72, subsystem=C++ Runtime
    (0x00225090, "AutoContainer::msg_poke"),  # size=96, subsystem=C++ Runtime
    (0x002250f0, "AutoContainer::msg_hurt"),  # size=96, subsystem=C++ Runtime
    (0x00225150, "AddParticle::run"),  # size=36, subsystem=Particles
    (0x00225178, "AddParticle::particleOn"),  # size=44, subsystem=Particles
    (0x002251a8, "AddParticle::particleOff"),  # size=8, subsystem=Particles
    (0x002251b0, "AddParticle::lightOn"),  # size=64, subsystem=Particles
    (0x002251f0, "AddParticle::lightOff"),  # size=60, subsystem=Particles
    (0x00225230, "AddParticle::debugReport"),  # size=8, subsystem=Particles
    (0x00225238, "AddParticle::bEdit"),  # size=8, subsystem=Particles
    (0x00225250, "AutoChestLP::constructor"),  # size=144, subsystem=Game Props
    (0x002252e0, "AutoChestLP::~destructor"),  # size=116, subsystem=Game Props
    (0x00225358, "AutoChestLP::msg_draw"),  # size=108, subsystem=Game Props
    (0x002253c8, "AutoChestLP::msg_run"),  # size=104, subsystem=Game Props
    (0x00225430, "AutoChestLP::msg_poke"),  # size=84, subsystem=Game Props
    (0x00225488, "AutoPropLP::~destructor"),  # size=140, subsystem=Game Props
    (0x00225518, "AutoContainerLP::constructor"),  # size=144, subsystem=C++ Runtime
    (0x002255a8, "AutoContainerLP::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00225610, "AutoContainerLP::msg_draw"),  # size=108, subsystem=C++ Runtime
    (0x00225680, "AutoContainerLP::msg_run"),  # size=104, subsystem=C++ Runtime
    (0x00225708, "AntTrap::msg_run"),  # size=516, subsystem=C++ Runtime
    (0x00225910, "HateInto::msg_run"),  # size=472, subsystem=C++ Runtime
    (0x00225ae8, "HateGate::msg_run"),  # size=472, subsystem=C++ Runtime
    (0x00225cc0, "GothTrap::setPassableState"),  # size=300, subsystem=C++ Runtime
    (0x00225df0, "HateBridge::setPassableState"),  # size=252, subsystem=Game Entities
    (0x00225fe8, "AntTrap::constructor"),  # size=204, subsystem=C++ Runtime
    (0x002260b8, "EggSack::constructor"),  # size=136, subsystem=C++ Runtime
    (0x00226140, "HateInto::constructor"),  # size=116, subsystem=C++ Runtime
    (0x002261b8, "HateGate::constructor"),  # size=96, subsystem=C++ Runtime
    (0x00226218, "GothTrap::constructor"),  # size=116, subsystem=C++ Runtime
    (0x00226290, "GothTrap::msg_run"),  # size=8, subsystem=C++ Runtime
    (0x00226298, "HateHole::constructor"),  # size=128, subsystem=C++ Runtime
    (0x00226318, "HateHole::msg_run"),  # size=28, subsystem=C++ Runtime
    (0x00226338, "HateHole::setPassableState"),  # size=172, subsystem=C++ Runtime
    (0x002263e8, "HateBridge::constructor"),  # size=124, subsystem=Game Entities
    (0x00226468, "HateBridge::msg_run"),  # size=124, subsystem=Game Entities
    (0x002264e8, "HackDoor::constructor"),  # size=96, subsystem=C++ Runtime
    (0x00226548, "HackDoor::setPassableState"),  # size=48, subsystem=C++ Runtime
    (0x00226598, "Orc::constructor"),  # size=2588, subsystem=Game Entities
    (0x00226fb8, "Orc::setWeapon"),  # size=256, subsystem=Game Entities
    (0x002270b8, "Orc::initType"),  # size=1408, subsystem=Game Entities
    (0x00227638, "Orc::msg_draw"),  # size=416, subsystem=Game Entities
    (0x002277d8, "Orc::msg_run"),  # size=5068, subsystem=Game Entities
    (0x00228ba8, "Orc::setState"),  # size=3244, subsystem=Game Entities
    (0x00229858, "Orc::dropItem"),  # size=964, subsystem=Game Entities
    (0x00229c20, "Orc::findCommander"),  # size=216, subsystem=Game Entities
    (0x00229cf8, "SuperOrc::constructor"),  # size=664, subsystem=Game Entities
    (0x00229f90, "SuperOrc::msg_draw"),  # size=276, subsystem=Game Entities
    (0x0022a0a8, "SuperOrc::msg_run"),  # size=3156, subsystem=Game Entities
    (0x0022ad00, "SuperOrc::setState"),  # size=964, subsystem=Game Entities
    (0x0022b0c8, "SuperOrc::superorcSlamEffect"),  # size=888, subsystem=Game Entities
    (0x0022b550, "Orc::msg_hurt"),  # size=28, subsystem=Game Entities
    (0x0022b570, "Orc::msg_alert"),  # size=328, subsystem=Game Entities
    (0x0022b6b8, "Orc::msg_save"),  # size=108, subsystem=Game Entities
    (0x0022b728, "Orc::msg_load"),  # size=144, subsystem=Game Entities
    (0x0022b7b8, "Orc::addCommander"),  # size=88, subsystem=Game Entities
    (0x0022b810, "Orc::deleteCommander"),  # size=108, subsystem=Game Entities
    (0x0022b880, "Orc::joinCommander"),  # size=92, subsystem=Game Entities
    (0x0022b8e0, "Orc::leaveCommander"),  # size=80, subsystem=Game Entities
    (0x0022b930, "Orc::commanderValid"),  # size=44, subsystem=Game Entities
    (0x0022b960, "Orc::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x0022b998, "Orc::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x0022b9d8, "SuperOrc::msg_trigger"),  # size=136, subsystem=Game Entities
    (0x0022ba60, "SuperOrc::msg_hurt"),  # size=112, subsystem=Game Entities
    (0x0022bb10, "Goblin::constructor"),  # size=1644, subsystem=Game Entities
    (0x0022c180, "Goblin::setWeapons"),  # size=204, subsystem=Game Entities
    (0x0022c250, "Goblin::initType"),  # size=1464, subsystem=Game Entities
    (0x0022c808, "Goblin::msg_draw"),  # size=400, subsystem=Game Entities
    (0x0022c998, "Goblin::msg_run"),  # size=5264, subsystem=Game Entities
    (0x0022de28, "Goblin::setState"),  # size=2412, subsystem=Game Entities
    (0x0022e798, "Goblin::dropItem"),  # size=312, subsystem=Game Entities
    (0x0022e8d0, "SnowballSpell::msg_run"),  # size=1136, subsystem=Game Entities
    (0x0022ed40, "SnowballSpell::msg_collision"),  # size=444, subsystem=Game Entities
    (0x0022ef80, "Goblin::msg_alert"),  # size=340, subsystem=Game Entities
    (0x0022f0d8, "Goblin::msg_save"),  # size=108, subsystem=Game Entities
    (0x0022f148, "Goblin::msg_load"),  # size=144, subsystem=Game Entities
    (0x0022f1d8, "Goblin::msg_collisionWorld"),  # size=100, subsystem=Game Entities
    (0x0022f240, "Goblin::msg_moveCollision"),  # size=268, subsystem=Game Entities
    (0x0022f350, "Goblin::hasShield"),  # size=16, subsystem=Game Entities
    (0x0022f360, "SnowballSpell::constructor"),  # size=184, subsystem=Game Entities
    (0x0022f418, "SnowballSpell::msg_draw"),  # size=224, subsystem=Game Entities
    (0x0022f4f8, "Goblin::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x0022f530, "Goblin::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x0022f590, "Torch::constructor"),  # size=368, subsystem=C++ Runtime
    (0x0022f700, "Torch::msg_run"),  # size=2024, subsystem=C++ Runtime
    (0x0022fee8, "Torch::msg_collision"),  # size=328, subsystem=C++ Runtime
    (0x00230030, "Torch::msg_draw"),  # size=372, subsystem=C++ Runtime
    (0x002301a8, "Candle::constructor"),  # size=332, subsystem=Renderer
    (0x002302f8, "Candle::msg_run"),  # size=792, subsystem=Renderer
    (0x00230610, "Candle2::msg_run"),  # size=636, subsystem=Renderer
    (0x00230890, "Lantern::constructor"),  # size=344, subsystem=C++ Runtime
    (0x002309e8, "Lamp::constructor"),  # size=312, subsystem=C++ Runtime
    (0x00230b20, "Lamp::msg_run"),  # size=548, subsystem=C++ Runtime
    (0x00231008, "Torch::msg_save"),  # size=24, subsystem=C++ Runtime
    (0x00231020, "Torch::msg_load"),  # size=72, subsystem=C++ Runtime
    (0x00231068, "Candle::msg_draw"),  # size=64, subsystem=Renderer
    (0x002310a8, "Candle2::constructor"),  # size=120, subsystem=Renderer
    (0x00231120, "Candle2::msg_draw"),  # size=64, subsystem=Renderer
    (0x00231160, "Lantern::msg_run"),  # size=220, subsystem=C++ Runtime
    (0x00231240, "Lantern::msg_draw"),  # size=212, subsystem=C++ Runtime
    (0x00231318, "Lamp::msg_draw"),  # size=140, subsystem=C++ Runtime
    (0x002313c8, "NPC::constructor"),  # size=556, subsystem=Game Entities
    (0x002315f8, "NPC::constructor"),  # size=896, subsystem=Game Entities
    (0x00231978, "NPC::msg_load"),  # size=324, subsystem=Game Entities
    (0x00231ac0, "NPC::msg_draw"),  # size=1584, subsystem=Game Entities
    (0x002320f0, "NPC::msg_run"),  # size=1212, subsystem=Game Entities
    (0x002325b0, "NPC::msg_trigger"),  # size=264, subsystem=Game Entities
    (0x002326b8, "NPC::setState"),  # size=352, subsystem=Game Entities
    (0x00232818, "Rondo::constructor"),  # size=388, subsystem=Game Entities
    (0x002329a0, "Rondo::msg_draw"),  # size=472, subsystem=Game Entities
    (0x00232b78, "Rondo::msg_run"),  # size=720, subsystem=Game Entities
    (0x00232e48, "Rondo::setState"),  # size=708, subsystem=Game Entities
    (0x00233198, "NPC::specificSetup"),  # size=8, subsystem=Game Entities
    (0x002331a0, "NPC::msg_save"),  # size=144, subsystem=Game Entities
    (0x00233230, "NPC::msg_hurt"),  # size=8, subsystem=Game Entities
    (0x00233238, "Rondo::msg_trigger"),  # size=72, subsystem=Game Entities
    (0x002332a0, "Natasla::constructor"),  # size=352, subsystem=C++ Runtime
    (0x00233400, "Natasla::msg_draw"),  # size=940, subsystem=C++ Runtime
    (0x002337b0, "Natasla::msg_run"),  # size=80, subsystem=C++ Runtime
    (0x00233800, "Natasla::setState"),  # size=116, subsystem=C++ Runtime
    (0x00233878, "Minion::constructor"),  # size=852, subsystem=C++ Runtime
    (0x00233bd0, "Minion::msg_run"),  # size=4700, subsystem=C++ Runtime
    (0x00234e30, "Minion::setState"),  # size=1180, subsystem=C++ Runtime
    (0x002352d0, "Minion::msg_draw"),  # size=100, subsystem=C++ Runtime
    (0x00235338, "Minion::msg_trigger"),  # size=120, subsystem=C++ Runtime
    (0x002353b0, "Minion::msg_hurt"),  # size=112, subsystem=C++ Runtime
    (0x00235420, "Minion::getSoulAttachMatrix"),  # size=88, subsystem=C++ Runtime
    (0x00235478, "Arenabeast::constructor"),  # size=888, subsystem=Game Entities
    (0x002357f0, "Arenabeast::msg_run"),  # size=3288, subsystem=Game Entities
    (0x002364c8, "Arenabeast::setState"),  # size=1160, subsystem=Game Entities
    (0x00236950, "Arenabeast::msg_draw"),  # size=68, subsystem=Game Entities
    (0x00236998, "Arenabeast::msg_trigger"),  # size=112, subsystem=Game Entities
    (0x00236a08, "Arenabeast::msg_hurt"),  # size=104, subsystem=Game Entities
    (0x00236a70, "Arenabeast::msg_moveCollision"),  # size=244, subsystem=Game Entities
    (0x00236b68, "Mummy::constructor"),  # size=1600, subsystem=Game Entities
    (0x002371a8, "Mummy::initType"),  # size=1196, subsystem=Game Entities
    (0x00237658, "Mummy::msg_draw"),  # size=304, subsystem=Game Entities
    (0x00237788, "Mummy::msg_run"),  # size=6268, subsystem=Game Entities
    (0x00239008, "Mummy::setState"),  # size=2196, subsystem=Game Entities
    (0x002398a0, "Mummy::dropWeapon"),  # size=228, subsystem=Game Entities
    (0x00239988, "Mummy::runSpells"),  # size=256, subsystem=Game Entities
    (0x00239a88, "MummyKing::constructor"),  # size=732, subsystem=Game Entities
    (0x00239d68, "MummyKing::msg_run"),  # size=4040, subsystem=Game Entities
    (0x0023ad30, "MummyKing::msg_trigger"),  # size=348, subsystem=Game Entities
    (0x0023ae90, "MummyKing::setState"),  # size=1112, subsystem=Game Entities
    (0x0023b2e8, "DustDevil::msg_run"),  # size=672, subsystem=C++ Runtime
    (0x0023b588, "SpawnMummy::msg_run"),  # size=312, subsystem=C++ Runtime
    (0x0023b6c0, "MummySnake::msg_run"),  # size=1448, subsystem=Game Entities
    (0x0023bcf0, "Mummy::setWeapon"),  # size=104, subsystem=Game Entities
    (0x0023bd58, "Mummy::msg_save"),  # size=96, subsystem=Game Entities
    (0x0023bdb8, "Mummy::msg_load"),  # size=132, subsystem=Game Entities
    (0x0023be40, "Mummy::initMiniboss"),  # size=56, subsystem=Game Entities
    (0x0023be78, "Mummy::getMinibossName"),  # size=60, subsystem=Game Entities
    (0x0023beb8, "MummyKing::msg_draw"),  # size=108, subsystem=Game Entities
    (0x0023bf28, "MummyKing::msg_hurt"),  # size=120, subsystem=Game Entities
    (0x0023bfa0, "MummyKing::bSpawnSnake"),  # size=108, subsystem=Game Entities
    (0x0023c010, "MummyKing::bSpawnMummy"),  # size=76, subsystem=Game Entities
    (0x0023c060, "DustDevil::constructor"),  # size=128, subsystem=C++ Runtime
    (0x0023c0e0, "DustDevil::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x0023c150, "SpawnMummy::constructor"),  # size=228, subsystem=C++ Runtime
    (0x0023c238, "MummySnake::constructor"),  # size=216, subsystem=Game Entities
    (0x0023c330, "UndeadKnight::constructor"),  # size=772, subsystem=Game Entities
    (0x0023c638, "UndeadKnight::msg_draw"),  # size=352, subsystem=Game Entities
    (0x0023c798, "UndeadKnight::msg_run"),  # size=2448, subsystem=Game Entities
    (0x0023d128, "UndeadKnight::setState"),  # size=1648, subsystem=Game Entities
    (0x0023d798, "UndeadKnightClone::constructor"),  # size=1004, subsystem=Game Entities
    (0x0023db88, "UndeadKnightClone::msg_draw"),  # size=1380, subsystem=Game Entities
    (0x0023e0f0, "UndeadKnightClone::msg_run"),  # size=4992, subsystem=Game Entities
    (0x0023f470, "UndeadKnightClone::setState"),  # size=824, subsystem=Game Entities
    (0x0023f8f8, "UndeadKnight::msg_trigger"),  # size=152, subsystem=Game Entities
    (0x0023f990, "UndeadKnight::msg_hurt"),  # size=104, subsystem=Game Entities
    (0x0023f9f8, "UndeadKnight::setHorse"),  # size=92, subsystem=Game Entities
    (0x0023fa78, "Vampire::constructor"),  # size=552, subsystem=C++ Runtime
    (0x0023fca0, "Vampire::msg_run"),  # size=1392, subsystem=C++ Runtime
    (0x00240210, "Vampire::setState"),  # size=1196, subsystem=C++ Runtime
    (0x002406c0, "VampireLord::constructor"),  # size=1020, subsystem=Game Entities
    (0x00240ac0, "VampireLord::msg_draw"),  # size=296, subsystem=Game Entities
    (0x00240be8, "VampireLord::msg_run"),  # size=8064, subsystem=Game Entities
    (0x00242b68, "VampireLord::msg_trigger"),  # size=548, subsystem=Game Entities
    (0x00242d90, "VampireLord::setState"),  # size=2032, subsystem=Game Entities
    (0x00243600, "Vampire::msg_draw"),  # size=40, subsystem=C++ Runtime
    (0x00243628, "VampireLord::msg_hurt"),  # size=172, subsystem=Game Entities
    (0x002436d8, "VampireLord::convertToBat"),  # size=108, subsystem=Game Entities
    (0x00243748, "VampireLord::convertToLord"),  # size=180, subsystem=Game Entities
    (0x00243800, "VampireLord::getModel"),  # size=68, subsystem=Game Entities
    (0x00243868, "Skeleton::constructor"),  # size=2640, subsystem=Game Entities
    (0x002442b8, "Skeleton::initType"),  # size=1088, subsystem=Game Entities
    (0x002446f8, "Skeleton::msg_draw"),  # size=388, subsystem=Game Entities
    (0x00244880, "Skeleton::msg_run"),  # size=2924, subsystem=Game Entities
    (0x002453f0, "Skeleton::setState"),  # size=1352, subsystem=Game Entities
    (0x00245938, "Skeleton::dropItem"),  # size=984, subsystem=Game Entities
    (0x00245d10, "Skeleton::findLeader"),  # size=580, subsystem=Game Entities
    (0x00245f58, "Skeleton::followLeader"),  # size=952, subsystem=Game Entities
    (0x00246310, "Skelight::constructor"),  # size=648, subsystem=Renderer
    (0x00246598, "Skelight::initWeapon"),  # size=776, subsystem=Renderer
    (0x002468a0, "Skelight::msg_draw"),  # size=304, subsystem=Renderer
    (0x002469d0, "Skelight::msg_run"),  # size=800, subsystem=Renderer
    (0x00246cf0, "Skelight::setState"),  # size=544, subsystem=Renderer
    (0x00246f10, "Skeleton::msg_save"),  # size=108, subsystem=Game Entities
    (0x00246f80, "Skeleton::msg_load"),  # size=144, subsystem=Game Entities
    (0x00247010, "Skeleton::msg_alert"),  # size=180, subsystem=Game Entities
    (0x002470c8, "Skeleton::msg_hurt"),  # size=148, subsystem=Game Entities
    (0x00247160, "Skeleton::isEnemy"),  # size=240, subsystem=Game Entities
    (0x00247250, "Skeleton::bIsCircular"),  # size=52, subsystem=Game Entities
    (0x00247288, "Skelight::msg_save"),  # size=132, subsystem=Renderer
    (0x00247310, "Skelight::msg_load"),  # size=220, subsystem=Renderer
    (0x002473f0, "Skelight::dropItem"),  # size=12, subsystem=Renderer
    (0x00247400, "WoodElfSoldier::constructor"),  # size=944, subsystem=Game Entities
    (0x002477b0, "WoodElfSoldier::msg_run"),  # size=3360, subsystem=Game Entities
    (0x002484d0, "WoodElfSoldier::msg_trigger"),  # size=444, subsystem=Game Entities
    (0x00248690, "WoodElfSoldier::setState"),  # size=2472, subsystem=Game Entities
    (0x00249038, "WoodElfSoldier::dropItem"),  # size=976, subsystem=Game Entities
    (0x00249408, "WoodElfSoldier::findCommander"),  # size=232, subsystem=Game Entities
    (0x002494f0, "WoodElfSoldier::bNextToEdge"),  # size=652, subsystem=Game Entities
    (0x00249780, "WoodElfSoldier::TurnToFaceEdge"),  # size=788, subsystem=Game Entities
    (0x00249a98, "WoodElfSoldier::moveArrow"),  # size=220, subsystem=Game Entities
    (0x00249c28, "WoodElfSoldier::initType"),  # size=96, subsystem=Game Entities
    (0x00249c88, "WoodElfSoldier::msg_draw"),  # size=60, subsystem=Game Entities
    (0x00249cc8, "WoodElfSoldier::msg_hurt"),  # size=28, subsystem=Game Entities
    (0x00249ce8, "WoodElfSoldier::addCommander"),  # size=88, subsystem=Game Entities
    (0x00249d40, "WoodElfSoldier::deleteCommander"),  # size=108, subsystem=Game Entities
    (0x00249db0, "WoodElfSoldier::joinCommander"),  # size=92, subsystem=Game Entities
    (0x00249e10, "WoodElfSoldier::leaveCommander"),  # size=80, subsystem=Game Entities
    (0x00249e60, "WoodElfSoldier::commanderValid"),  # size=44, subsystem=Game Entities
    (0x00249e90, "WoodElfSoldier::FindEdgePos"),  # size=32, subsystem=Game Entities
    (0x00249eb0, "WoodElfSoldier::drawArrow"),  # size=192, subsystem=Game Entities
    (0x00263088, "MGInst::cycle"),  # size=300, subsystem=Networking
    (0x002631b8, "MGInst::init"),  # size=1868, subsystem=Networking
    (0x00263908, "MGInst::doEntry"),  # size=568, subsystem=Networking
    (0x00263b40, "MGInst::Exits::pickRandom"),  # size=248, subsystem=Networking
    (0x00263c38, "MGWorldmap::place"),  # size=1128, subsystem=DMA/GIF Pipeline
    (0x002640a0, "MGWorldmap::remove"),  # size=1684, subsystem=DMA/GIF Pipeline
    (0x00264738, "MGWorldmap::test"),  # size=2060, subsystem=DMA/GIF Pipeline
    (0x00266218, "MGInst::destroy"),  # size=148, subsystem=Networking
    (0x002662b0, "MGInst::childKilled"),  # size=144, subsystem=Networking
    (0x00266340, "MGInst::Exits::addPossible"),  # size=336, subsystem=Networking
    (0x00266490, "MGWorldmap::get"),  # size=220, subsystem=DMA/GIF Pipeline
    (0x00266570, "MGWorldmap::getEdge"),  # size=240, subsystem=DMA/GIF Pipeline
    (0x00266708, "MGWorldmap::init"),  # size=92, subsystem=DMA/GIF Pipeline
    (0x00266768, "MGWorldmap::getid"),  # size=28, subsystem=DMA/GIF Pipeline
    (0x00266788, "MGWorldmap::spanTo"),  # size=292, subsystem=DMA/GIF Pipeline
    (0x002668b0, "MGGlobals::init"),  # size=160, subsystem=Networking
    (0x00266950, "MGGlobals::cycle"),  # size=112, subsystem=Networking
    (0x002669c0, "MGGlobals::activate"),  # size=92, subsystem=Networking
    (0x00266a20, "MGGlobals::deactivate"),  # size=92, subsystem=Networking
    (0x00266a80, "MGGlobals::createNewInstance"),  # size=360, subsystem=Networking
    (0x00266be8, "MGGlobals::removeInstance"),  # size=168, subsystem=Networking
    (0x0026be00, "Camera::Reset"),  # size=480, subsystem=Camera
    (0x0026bfe0, "Camera::Update"),  # size=284, subsystem=Camera
    (0x0026c100, "Camera::DisableZooming"),  # size=140, subsystem=Camera
    (0x0026c190, "Camera::BuildMatrix"),  # size=828, subsystem=Camera
    (0x0026c4d0, "Camera::Save"),  # size=260, subsystem=Camera
    (0x0026c5d8, "Camera::Load"),  # size=408, subsystem=Camera
    (0x0026c770, "Camera::StartDialogSwoop"),  # size=1656, subsystem=Camera
    (0x0026cde8, "Camera::AdvanceDialogSwoop"),  # size=392, subsystem=Camera
    (0x0026cf70, "Camera::doDebugCam"),  # size=1376, subsystem=Camera
    (0x0026d4d0, "Camera::doNormalCam"),  # size=1492, subsystem=Camera
    (0x0026daa8, "Camera::doAutoPitch"),  # size=2020, subsystem=Camera
    (0x0026e290, "Camera::doUserZoom"),  # size=1280, subsystem=Camera
    (0x0026e790, "Camera::doUserYaw"),  # size=1492, subsystem=Camera
    (0x0026ed68, "Camera::checkYawReset"),  # size=300, subsystem=Camera
    (0x0026ee98, "Camera::obtainTarget"),  # size=1676, subsystem=Camera
    (0x0026f528, "Camera::determineBestController"),  # size=632, subsystem=Camera
    (0x0026f7a0, "Camera::doInnorukCam"),  # size=420, subsystem=Camera
    (0x0026f948, "Camera::constructor"),  # size=100, subsystem=Camera
    (0x0026f9b0, "Camera::Push"),  # size=108, subsystem=Camera
    (0x0026fa20, "Camera::Pop"),  # size=100, subsystem=Camera
    (0x0026fa88, "Camera::SetMode"),  # size=112, subsystem=Camera
    (0x0026faf8, "Camera::SetYaw"),  # size=8, subsystem=Camera
    (0x0026fb00, "Camera::SetPitch"),  # size=8, subsystem=Camera
    (0x0026fb08, "Camera::SetZoomDistance"),  # size=112, subsystem=Camera
    (0x0026fb78, "Camera::SetMaxHeight"),  # size=8, subsystem=Camera
    (0x0026fb80, "Camera::SetPitchAtLevel"),  # size=32, subsystem=Camera
    (0x0026fba0, "Camera::SetDistanceAtLevel"),  # size=132, subsystem=Camera
    (0x0026fc28, "Camera::SetNoTargetUpdates"),  # size=8, subsystem=Camera
    (0x0026fc30, "Camera::SetCutWasActive"),  # size=12, subsystem=Camera
    (0x0026fc40, "Camera::GetYaw"),  # size=8, subsystem=Camera
    (0x0026fc48, "Camera::GetPitch"),  # size=8, subsystem=Camera
    (0x0026fc50, "Camera::GetZoomDistance"),  # size=8, subsystem=Camera
    (0x0026fc58, "Camera::GetToggle"),  # size=8, subsystem=Camera
    (0x0026fc60, "Camera::GetMode"),  # size=8, subsystem=Camera
    (0x0026fc68, "Camera::GetLastTarget"),  # size=32, subsystem=Camera
    (0x0026fc88, "Camera::GetTargetNum"),  # size=8, subsystem=Camera
    (0x0026fc90, "Camera::GetSaveFootPrint"),  # size=28, subsystem=Camera
    (0x0026fcb0, "Camera::ChangeNetCam"),  # size=240, subsystem=Camera
    (0x0026fda0, "Camera::clampZoomMag"),  # size=64, subsystem=Camera
    (0x0026fde0, "Camera::playerCountChanged"),  # size=16, subsystem=Camera
    (0x0026fdf0, "Camera::enforceMaxSpeed"),  # size=148, subsystem=Camera
    (0x002702d8, "Vehicle::constructor"),  # size=700, subsystem=Physics
    (0x00270598, "Vehicle::~destructor"),  # size=212, subsystem=Physics
    (0x00270670, "Vehicle::msg_run"),  # size=1616, subsystem=Physics
    (0x00270cc0, "Vehicle::msg_draw"),  # size=612, subsystem=Physics
    (0x00270f28, "Vehicle::Reset"),  # size=576, subsystem=Physics
    (0x00271168, "Vehicle::GetPlayerPosition"),  # size=336, subsystem=Physics
    (0x002712b8, "Vehicle::getSeatPosition"),  # size=460, subsystem=Physics
    (0x00271488, "Vehicle::addPassenger"),  # size=544, subsystem=Physics
    (0x002716a8, "Vehicle::removePassenger"),  # size=456, subsystem=Physics
    (0x00271870, "Vehicle::processParams"),  # size=688, subsystem=Physics
    (0x00271b20, "Vehicle::addWheel"),  # size=364, subsystem=Physics
    (0x00271c90, "Vehicle::accumForceAndTorque"),  # size=468, subsystem=Physics
    (0x00271e68, "Vehicle::getNewRotAndPos"),  # size=1104, subsystem=Physics
    (0x002722b8, "Vehicle::getParticleVelocity"),  # size=296, subsystem=Physics
    (0x002723e0, "Vehicle::impulse"),  # size=712, subsystem=Physics
    (0x002726a8, "Vehicle::dualImpulse"),  # size=1292, subsystem=Physics
    (0x00272bb8, "Vehicle::backupJustForces"),  # size=260, subsystem=Physics
    (0x00272cc0, "Vehicle::backup"),  # size=352, subsystem=Physics
    (0x00272e20, "Vehicle::addImpulse"),  # size=336, subsystem=Physics
    (0x00272f70, "Vehicle::finalizePosition"),  # size=1116, subsystem=Physics
    (0x002733d0, "Vehicle::checkWallCollision"),  # size=1236, subsystem=Physics
    (0x002738a8, "Vehicle::checkVehicleCollision"),  # size=556, subsystem=Physics
    (0x00273ad8, "Vehicle::doMisc"),  # size=1288, subsystem=Physics
    (0x00273fe0, "Vehicle::doSuspension"),  # size=1448, subsystem=Physics
    (0x00274588, "Vehicle::doThrottle"),  # size=788, subsystem=Physics
    (0x002748a0, "Vehicle::doBrakes"),  # size=316, subsystem=Physics
    (0x002749e0, "Vehicle::doAI"),  # size=560, subsystem=Physics
    (0x00274c10, "Vehicle::getBlockingVehicle"),  # size=448, subsystem=Physics
    (0x00274dd0, "Vehicle::doSteering"),  # size=1220, subsystem=Physics
    (0x00275298, "Vehicle::doDriveline"),  # size=3712, subsystem=Physics
    (0x00276118, "Vehicle::doDifferential"),  # size=324, subsystem=Physics
    (0x00276260, "Vehicle::scalePatchLimit"),  # size=272, subsystem=Physics
    (0x00276370, "Vehicle::buildCollisionBox"),  # size=540, subsystem=Physics
    (0x00276590, "Vehicle::resolveCreatureCollisions"),  # size=1476, subsystem=Physics
    (0x00276b58, "Vehicle::buildCollisionInfo"),  # size=1136, subsystem=Physics
    (0x00276fc8, "Wheel::constructor"),  # size=436, subsystem=Game Props
    (0x00277180, "Wheel::msg_run"),  # size=376, subsystem=Game Props
    (0x002772f8, "Wheel::msg_draw"),  # size=324, subsystem=Game Props
    (0x00277440, "Wheel::FinalizePosition"),  # size=464, subsystem=Game Props
    (0x002778a0, "Vehicle::msg_collision"),  # size=64, subsystem=Physics
    (0x002778e0, "Vehicle::msg_getPokeName"),  # size=204, subsystem=Physics
    (0x002779b0, "Vehicle::msg_poke"),  # size=28, subsystem=Physics
    (0x002779d0, "Vehicle::GetNPCPosition"),  # size=84, subsystem=Physics
    (0x00277a28, "Vehicle::GetPositionAndYaw"),  # size=176, subsystem=Physics
    (0x00277ad8, "Vehicle::AddNPCDriver"),  # size=40, subsystem=Physics
    (0x00277b00, "Vehicle::RemoveNPCDriver"),  # size=124, subsystem=Physics
    (0x00277b80, "Vehicle::SetHold"),  # size=8, subsystem=Physics
    (0x00277b88, "Vehicle::Kick"),  # size=108, subsystem=Physics
    (0x00277bf8, "Vehicle::getClosestSeat"),  # size=232, subsystem=Physics
    (0x00277ce0, "Vehicle::haveRoom"),  # size=52, subsystem=Physics
    (0x00277d18, "Vehicle::isPassenger"),  # size=72, subsystem=Physics
    (0x00277d60, "Vehicle::setMassAndIBody"),  # size=176, subsystem=Physics
    (0x00277e10, "Vehicle::startForces"),  # size=32, subsystem=Physics
    (0x00277e30, "Vehicle::startGuessForce"),  # size=144, subsystem=Physics
    (0x00277ec0, "Vehicle::stopGuessForce"),  # size=280, subsystem=Physics
    (0x00277fd8, "Vehicle::changeOrientation"),  # size=216, subsystem=Physics
    (0x002780b0, "Vehicle::queryGuessPosition"),  # size=108, subsystem=Physics
    (0x00278120, "Vehicle::getEngineTorque"),  # size=180, subsystem=Physics
    (0x002781d8, "Vehicle::rayHit"),  # size=220, subsystem=Physics
    (0x002782b8, "Vehicle::refreshSettings"),  # size=236, subsystem=Physics
    (0x002783a8, "Wheel::Reset"),  # size=20, subsystem=Game Props
    (0x002783c0, "Wheel::SetNaturalRPM"),  # size=148, subsystem=Game Props
    (0x00278458, "Wheel::ModifyRPM"),  # size=8, subsystem=Game Props
    (0x00278f08, "Line::constructor"),  # size=1016, subsystem=Game Props
    (0x00279300, "Line::constructor"),  # size=364, subsystem=Game Props
    (0x00279470, "Line::initializeMe"),  # size=1124, subsystem=Game Props
    (0x00279c60, "Line::~destructor"),  # size=84, subsystem=Game Props
    (0x00280a88, "Cthulu::constructor"),  # size=796, subsystem=Renderer
    (0x00280da8, "Cthulu::msg_run"),  # size=3448, subsystem=Renderer
    (0x00281b20, "Cthulu::setState"),  # size=1260, subsystem=Renderer
    (0x00282010, "Cthulu::msg_draw"),  # size=40, subsystem=Renderer
    (0x00282038, "Cthulu::msg_moveCollision"),  # size=236, subsystem=Renderer
    (0x00282128, "JumpGate::constructor"),  # size=1016, subsystem=Game Props
    (0x00282520, "JumpGate::msg_run"),  # size=2720, subsystem=Game Props
    (0x00282fc0, "JumpGate::msg_draw"),  # size=276, subsystem=Game Props
    (0x002830d8, "JumpGate::msg_getPokeName"),  # size=472, subsystem=Game Props
    (0x00284450, "JumpGate::~destructor"),  # size=160, subsystem=Game Props
    (0x002844f0, "JumpGate::msg_poke"),  # size=72, subsystem=Game Props
    (0x00284538, "JumpGate::msg_save"),  # size=36, subsystem=Game Props
    (0x00284560, "JumpGate::msg_load"),  # size=140, subsystem=Game Props
    (0x00284918, "LavaTractor::set"),  # size=620, subsystem=Physics
    (0x00284b88, "LavaTractor::constructor"),  # size=128, subsystem=Physics
    (0x00284c08, "LavaTractor::eventActivate"),  # size=164, subsystem=Physics
    (0x00284cb0, "LavaTractor::eventDeActivate"),  # size=48, subsystem=Physics
    (0x00284ce0, "LavaTractor::eventGasOn"),  # size=104, subsystem=Physics
    (0x00284d48, "LavaTractor::eventGasOff"),  # size=104, subsystem=Physics
    (0x00284db0, "LavaTractor::eventCurRPM"),  # size=84, subsystem=Physics
    (0x00284e08, "LavaTractor::eventCollisionGround"),  # size=8, subsystem=Physics
    (0x00284e10, "LavaTractor::eventCollisionWall"),  # size=164, subsystem=Physics
    (0x00284eb8, "LavaTractor::eventSteeringChange"),  # size=104, subsystem=Physics
    (0x00284f20, "FemaleDarkElf::constructor"),  # size=1160, subsystem=Game Entities
    (0x002853a8, "FemaleDarkElf::initType"),  # size=864, subsystem=Game Entities
    (0x00285708, "FemaleDarkElf::msg_draw"),  # size=296, subsystem=Game Entities
    (0x00285830, "FemaleDarkElf::msg_run"),  # size=2504, subsystem=Game Entities
    (0x002861f8, "FemaleDarkElf::setState"),  # size=1832, subsystem=Game Entities
    (0x00286920, "MaleDarkElf::constructor"),  # size=1976, subsystem=Renderer
    (0x002870d8, "MaleDarkElf::initType"),  # size=1336, subsystem=Renderer
    (0x00287610, "MaleDarkElf::msg_draw"),  # size=380, subsystem=Renderer
    (0x00287790, "MaleDarkElf::msg_run"),  # size=4232, subsystem=Renderer
    (0x00288818, "MaleDarkElf::setState"),  # size=3264, subsystem=Renderer
    (0x002894d8, "FemaleDarkElf::msg_save"),  # size=108, subsystem=Game Entities
    (0x00289548, "FemaleDarkElf::msg_load"),  # size=128, subsystem=Game Entities
    (0x002895c8, "FemaleDarkElf::msg_alert"),  # size=180, subsystem=Game Entities
    (0x00289680, "MaleDarkElf::msg_save"),  # size=120, subsystem=Renderer
    (0x002896f8, "MaleDarkElf::msg_load"),  # size=140, subsystem=Renderer
    (0x00289788, "MaleDarkElf::msg_alert"),  # size=180, subsystem=Renderer
    (0x00289840, "MaleDarkElf::initMiniboss"),  # size=48, subsystem=Renderer
    (0x00289870, "MaleDarkElf::getMinibossName"),  # size=60, subsystem=Renderer
    (0x002898b0, "FireBomb::constructor"),  # size=392, subsystem=C++ Runtime
    (0x00289a38, "FireBomb::msg_run"),  # size=808, subsystem=C++ Runtime
    (0x00289d60, "FireBomblet::constructor"),  # size=576, subsystem=C++ Runtime
    (0x00289fa0, "FireBomblet::msg_run"),  # size=2368, subsystem=C++ Runtime
    (0x0028a8e0, "FireBomblet::msg_draw"),  # size=216, subsystem=C++ Runtime
    (0x0028a9b8, "FireBomblet::bounce"),  # size=752, subsystem=C++ Runtime
    (0x0028aca8, "FireBombletJr::constructor"),  # size=1040, subsystem=C++ Runtime
    (0x0028b0b8, "FireBombletJr::msg_run"),  # size=944, subsystem=C++ Runtime
    (0x0028b468, "FireBombletJr::msg_draw"),  # size=216, subsystem=C++ Runtime
    (0x0028b540, "FireBombletJr::bounce"),  # size=472, subsystem=C++ Runtime
    (0x0028b7a0, "FireBomblet::~destructor"),  # size=136, subsystem=C++ Runtime
    (0x0028b828, "FireBomblet::detach"),  # size=8, subsystem=C++ Runtime
    (0x0028b830, "FireBomblet::setHold"),  # size=8, subsystem=C++ Runtime
    (0x0028b858, "Catapult::constructor"),  # size=944, subsystem=C++ Runtime
    (0x0028bc08, "Catapult::~destructor"),  # size=252, subsystem=C++ Runtime
    (0x0028bd08, "Catapult::msg_run"),  # size=620, subsystem=C++ Runtime
    (0x0028bf78, "Catapult::msg_draw"),  # size=600, subsystem=C++ Runtime
    (0x0028c1d0, "Catapult::msg_hurt"),  # size=656, subsystem=C++ Runtime
    (0x0028c460, "Catapult::msg_trigger"),  # size=76, subsystem=C++ Runtime
    (0x0028c4b0, "Catapult::msg_save"),  # size=28, subsystem=C++ Runtime
    (0x0028c4d0, "Catapult::msg_load"),  # size=120, subsystem=C++ Runtime
    (0x0028c548, "SkillShock::getRankDescription"),  # size=296, subsystem=Skills
    (0x0028c670, "ShockProjectile::constructor"),  # size=672, subsystem=Projectiles
    (0x0028c910, "ShockProjectile::msg_run"),  # size=3004, subsystem=Projectiles
    (0x0028d4d0, "ShockProjectile::msg_draw"),  # size=280, subsystem=Projectiles
    (0x0028d5e8, "ShockProjectile::buildShockChainList"),  # size=312, subsystem=Projectiles
    (0x0028d810, "SkillShock::constructor"),  # size=44, subsystem=Skills
    (0x0028d840, "SkillShock::initRamps"),  # size=108, subsystem=Skills
    (0x0028d8b0, "SkillShock::cast"),  # size=144, subsystem=Skills
    (0x0028d940, "SkillShock::getEnergyCost"),  # size=52, subsystem=Skills
    (0x0028d978, "ShockProjectile::~destructor"),  # size=140, subsystem=Projectiles
    (0x0028da08, "ShockProjectile::alreadyChained"),  # size=64, subsystem=Projectiles
    (0x0028da68, "StaticFire::constructor"),  # size=664, subsystem=C++ Runtime
    (0x0028dd00, "StaticFire::constructor"),  # size=620, subsystem=C++ Runtime
    (0x0028df70, "StaticFire::init"),  # size=276, subsystem=C++ Runtime
    (0x0028e088, "StaticFire::msg_run"),  # size=2768, subsystem=C++ Runtime
    (0x0028eb58, "StaticFire::msg_draw"),  # size=1180, subsystem=C++ Runtime
    (0x0028eff8, "StaticFire::newWind"),  # size=288, subsystem=C++ Runtime
    (0x0028f118, "StaticFire::addSmokelet"),  # size=560, subsystem=C++ Runtime
    (0x0028f490, "StaticFire::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x0028f518, "StaticFire::updateSmokelets"),  # size=208, subsystem=C++ Runtime
    (0x0028f608, "SkillGroundPound::getRankDescription"),  # size=396, subsystem=Skills
    (0x0028f798, "GroundPoundEffect::constructor"),  # size=836, subsystem=Game Entities
    (0x0028fae0, "GroundPoundEffect::msg_run"),  # size=2752, subsystem=Game Entities
    (0x00290888, "SkillGroundPound::constructor"),  # size=44, subsystem=Skills
    (0x002908b8, "SkillGroundPound::initRamps"),  # size=112, subsystem=Skills
    (0x00290928, "SkillGroundPound::canCast"),  # size=172, subsystem=Skills
    (0x002909d8, "SkillGroundPound::cast"),  # size=240, subsystem=Skills
    (0x00290ac8, "SkillGroundPound::getEnergyCost"),  # size=52, subsystem=Skills
    (0x00290b20, "SkillCharge::getRankDescription"),  # size=856, subsystem=Skills
    (0x00290e78, "SpellCharge::constructor"),  # size=632, subsystem=Spells
    (0x002910f0, "SpellCharge::run"),  # size=1604, subsystem=Spells
    (0x00291738, "SpellCharge::hitSomething"),  # size=1596, subsystem=Spells
    (0x00291d78, "SpellCharge::~destructor"),  # size=200, subsystem=Spells
    (0x00291f98, "SkillCharge::constructor"),  # size=44, subsystem=Skills
    (0x00291fc8, "SkillCharge::initRamps"),  # size=112, subsystem=Skills
    (0x00292038, "SkillCharge::cast"),  # size=160, subsystem=Skills
    (0x002920d8, "SkillCharge::getEnergyCost"),  # size=52, subsystem=Skills
    (0x00292110, "SpellCharge::getYawScale"),  # size=72, subsystem=Spells
    (0x00292178, "DiseaseBolt::constructor"),  # size=476, subsystem=Projectiles
    (0x00292358, "DiseaseBolt::msg_run"),  # size=3476, subsystem=Projectiles
    (0x002930f0, "DiseaseBolt::msg_collision"),  # size=548, subsystem=Projectiles
    (0x00293318, "SkillDiseaseBolt::getRankDescription"),  # size=436, subsystem=Skills
    (0x00293628, "DiseaseBolt::msg_draw"),  # size=268, subsystem=Projectiles
    (0x00293738, "SkillDiseaseBolt::constructor"),  # size=44, subsystem=Skills
    (0x00293768, "SkillDiseaseBolt::initRamps"),  # size=88, subsystem=Skills
    (0x002937c0, "SkillDiseaseBolt::cast"),  # size=164, subsystem=Skills
    (0x00293868, "SkillDiseaseBolt::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00293870, "SkillDiseaseBolt::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00293878, "SkillDiseaseBolt::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002938a0, "SkillDiseaseBolt::canCast"),  # size=8, subsystem=Skills
    (0x002938c8, "DiseaseTrail::msg_run"),  # size=2624, subsystem=Game Entities
    (0x00294308, "SpellDiseaseTrail::constructor"),  # size=708, subsystem=Spells
    (0x002945d0, "SpellDiseaseTrail::run"),  # size=2528, subsystem=Spells
    (0x00294fb0, "SkillDiseaseTrail::getRankDescription"),  # size=436, subsystem=Skills
    (0x002952b8, "DiseaseTrail::constructor"),  # size=364, subsystem=Game Entities
    (0x00295428, "SkillDiseaseTrail::constructor"),  # size=44, subsystem=Skills
    (0x00295458, "SkillDiseaseTrail::initRamps"),  # size=52, subsystem=Skills
    (0x00295490, "SkillDiseaseTrail::cast"),  # size=156, subsystem=Skills
    (0x00295530, "SkillDiseaseTrail::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00295538, "SkillDiseaseTrail::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00295540, "SkillDiseaseTrail::getEnergyCost"),  # size=36, subsystem=Skills
    (0x00295568, "SkillDiseaseTrail::canCast"),  # size=52, subsystem=Skills
    (0x002955c0, "SpellDiseaseShield::constructor"),  # size=764, subsystem=Spells
    (0x002958c0, "SpellDiseaseShield::run"),  # size=3004, subsystem=Spells
    (0x00296480, "SkillDiseaseShield::getRankDescription"),  # size=488, subsystem=Skills
    (0x00296760, "SkillDiseaseShield::constructor"),  # size=44, subsystem=Skills
    (0x00296790, "SkillDiseaseShield::initRamps"),  # size=116, subsystem=Skills
    (0x00296808, "SkillDiseaseShield::cast"),  # size=152, subsystem=Skills
    (0x002968a0, "SkillDiseaseShield::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002968a8, "SkillDiseaseShield::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002968b0, "SkillDiseaseShield::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002968d8, "SkillDiseaseShield::canCast"),  # size=52, subsystem=Skills
    (0x00296930, "DiseaseCorpse::msg_run"),  # size=380, subsystem=Game Entities
    (0x00296ab0, "DiseaseCloud::msg_run"),  # size=2236, subsystem=C++ Runtime
    (0x002974b8, "DiseaseCorpse::constructor"),  # size=172, subsystem=Game Entities
    (0x00297568, "DiseaseCloud::constructor"),  # size=204, subsystem=C++ Runtime
    (0x00297658, "SkillDarkness::cast"),  # size=312, subsystem=Skills
    (0x00297790, "DarknessProjectile::constructor"),  # size=544, subsystem=Other
    (0x002979b0, "DarknessProjectile::msg_run"),  # size=1824, subsystem=Other
    (0x00298150, "SkillDarkness::constructor"),  # size=44, subsystem=Skills
    (0x00298180, "SkillDarkness::initRamps"),  # size=100, subsystem=Skills
    (0x002981e8, "SkillDarkness::getRankDescription"),  # size=260, subsystem=Skills
    (0x002982f0, "SkillDarkness::getSkillPointCost"),  # size=12, subsystem=Skills
    (0x00298300, "SkillDarkness::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00298308, "SkillDarkness::getEnergyCost"),  # size=52, subsystem=Skills
    (0x00298360, "SpellConvertEnemy::constructor"),  # size=484, subsystem=Spells
    (0x00298548, "SpellConvertEnemy::run"),  # size=1192, subsystem=Spells
    (0x00298a78, "SkillConvertEnemy::constructor"),  # size=44, subsystem=Skills
    (0x00298aa8, "SkillConvertEnemy::initRamps"),  # size=88, subsystem=Skills
    (0x00298b00, "SkillConvertEnemy::cast"),  # size=156, subsystem=Skills
    (0x00298ba0, "SkillConvertEnemy::getRankDescription"),  # size=260, subsystem=Skills
    (0x00298ca8, "SkillConvertEnemy::getEnergyCost"),  # size=52, subsystem=Skills
    (0x00298d00, "SkillConvertUndead::canCast"),  # size=268, subsystem=Skills
    (0x00298e10, "SpellConvertUndead::constructor"),  # size=508, subsystem=Spells
    (0x00299010, "SpellConvertUndead::run"),  # size=1076, subsystem=Spells
    (0x002994d0, "SkillConvertUndead::constructor"),  # size=44, subsystem=Skills
    (0x00299500, "SkillConvertUndead::initRamps"),  # size=88, subsystem=Skills
    (0x00299558, "SkillConvertUndead::cast"),  # size=156, subsystem=Skills
    (0x002995f8, "SkillConvertUndead::getRankDescription"),  # size=260, subsystem=Skills
    (0x00299700, "SkillConvertUndead::getEnergyCost"),  # size=52, subsystem=Skills
    (0x00299758, "SpellCyclone::constructor"),  # size=684, subsystem=Spells
    (0x00299a08, "SpellCyclone::run"),  # size=1728, subsystem=Spells
    (0x0029a0c8, "SpellCyclone::runEffect"),  # size=1360, subsystem=Spells
    (0x0029a710, "SkillCyclone::constructor"),  # size=48, subsystem=Skills
    (0x0029a740, "SkillCyclone::canCast"),  # size=132, subsystem=Skills
    (0x0029a7c8, "SkillCyclone::initRamps"),  # size=84, subsystem=Skills
    (0x0029a820, "SkillCyclone::cast"),  # size=132, subsystem=Skills
    (0x0029a8a8, "SkillCyclone::getRankDescription"),  # size=244, subsystem=Skills
    (0x0029a9a0, "SkillCyclone::getEnergyCost"),  # size=52, subsystem=Skills
    (0x0029a9d8, "SkillCyclone::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x0029aa00, "SpellHarmTouch::attack"),  # size=944, subsystem=Spells
    (0x0029aea8, "SkillHarmTouch::constructor"),  # size=48, subsystem=Skills
    (0x0029aed8, "SkillHarmTouch::initRamps"),  # size=100, subsystem=Skills
    (0x0029af40, "SkillHarmTouch::getEnergyCost"),  # size=52, subsystem=Skills
    (0x0029af78, "SkillHarmTouch::cast"),  # size=132, subsystem=Skills
    (0x0029b000, "SkillHarmTouch::getRankDescription"),  # size=204, subsystem=Skills
    (0x0029b0d0, "SpellHarmTouch::constructor"),  # size=160, subsystem=Spells
    (0x0029b170, "SpellHarmTouch::run"),  # size=168, subsystem=Spells
    (0x0029b238, "FireStormFlare::msg_run"),  # size=2824, subsystem=C++ Runtime
    (0x0029bd40, "FireStorm::constructor"),  # size=860, subsystem=Game Entities
    (0x0029c0a0, "FireStorm::msg_run"),  # size=2204, subsystem=Game Entities
    (0x0029c940, "SkillFireStorm::cast"),  # size=324, subsystem=Skills
    (0x0029ca88, "SkillFireStorm::getRankDescription"),  # size=488, subsystem=Skills
    (0x0029cc70, "SkillFireStorm::canCast"),  # size=260, subsystem=Skills
    (0x0029cec0, "FireStormFlare::constructor"),  # size=280, subsystem=C++ Runtime
    (0x0029cfd8, "FireStormFlare::msg_draw"),  # size=280, subsystem=C++ Runtime
    (0x0029d0f0, "FireStorm::~destructor"),  # size=160, subsystem=Game Entities
    (0x0029d190, "SkillFireStorm::constructor"),  # size=44, subsystem=Skills
    (0x0029d1c0, "SkillFireStorm::initRamps"),  # size=112, subsystem=Skills
    (0x0029d230, "SkillFireStorm::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x0029d238, "SkillFireStorm::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x0029d240, "SkillFireStorm::getEnergyCost"),  # size=36, subsystem=Skills
    (0x0029d288, "SpellDiseaseEffect::constructor"),  # size=624, subsystem=Spells
    (0x0029d4f8, "SpellDiseaseEffect::run"),  # size=1684, subsystem=Spells
    (0x0029db90, "FireArrowProjectile::constructor"),  # size=484, subsystem=C++ Runtime
    (0x0029dd78, "FireArrowProjectile::msg_run"),  # size=300, subsystem=C++ Runtime
    (0x0029dea8, "FireArrowProjectile::msg_collision"),  # size=1056, subsystem=C++ Runtime
    (0x0029e2c8, "SkillFireArrow::constructor"),  # size=48, subsystem=Skills
    (0x0029e2f8, "SkillFireArrow::initRamps"),  # size=112, subsystem=Skills
    (0x0029e368, "SkillFireArrow::cast"),  # size=204, subsystem=Skills
    (0x0029e438, "SkillFireArrow::getRankDescription"),  # size=252, subsystem=Skills
    (0x0029e538, "SkillFireArrow::getEnergyCost"),  # size=52, subsystem=Skills
    (0x0029e570, "FireArrowProjectile::msg_draw"),  # size=112, subsystem=C++ Runtime
    (0x0029e5e0, "FireArrowProjectile::terminate"),  # size=196, subsystem=C++ Runtime
    (0x0029e6a8, "ColdArrowProjectile::constructor"),  # size=444, subsystem=Projectiles
    (0x0029e868, "ColdArrowProjectile::msg_run"),  # size=1540, subsystem=Projectiles
    (0x0029ee70, "ColdArrowProjectile::msg_draw"),  # size=292, subsystem=Projectiles
    (0x0029ef98, "ColdArrowProjectile::msg_collision"),  # size=976, subsystem=Projectiles
    (0x0029f368, "ColdArrowProjectile::terminate"),  # size=1676, subsystem=Projectiles
    (0x0029fb40, "SkillColdArrow::constructor"),  # size=48, subsystem=Skills
    (0x0029fb70, "SkillColdArrow::initRamps"),  # size=132, subsystem=Skills
    (0x0029fbf8, "SkillColdArrow::cast"),  # size=204, subsystem=Skills
    (0x0029fcc8, "SkillColdArrow::getRankDescription"),  # size=252, subsystem=Skills
    (0x0029fdc8, "SkillColdArrow::getEnergyCost"),  # size=52, subsystem=Skills
    (0x0029fe20, "SkillPoisonArrow::getRankDescription"),  # size=356, subsystem=Skills
    (0x0029ff88, "PoisonArrowProjectile::constructor"),  # size=448, subsystem=C++ Runtime
    (0x002a0148, "PoisonArrowProjectile::msg_run"),  # size=952, subsystem=C++ Runtime
    (0x002a0500, "PoisonArrowProjectile::msg_draw"),  # size=308, subsystem=C++ Runtime
    (0x002a0638, "PoisonArrowProjectile::msg_collision"),  # size=592, subsystem=C++ Runtime
    (0x002a0888, "PoisonArrowProjectile::terminate"),  # size=424, subsystem=C++ Runtime
    (0x002a0b80, "SkillPoisonArrow::constructor"),  # size=48, subsystem=Skills
    (0x002a0bb0, "SkillPoisonArrow::initRamps"),  # size=124, subsystem=Skills
    (0x002a0c30, "SkillPoisonArrow::cast"),  # size=204, subsystem=Skills
    (0x002a0d00, "SkillPoisonArrow::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a0d58, "SkillMultiFire::cast"),  # size=1408, subsystem=Skills
    (0x002a12d8, "MultiFireProjectile::constructor"),  # size=332, subsystem=C++ Runtime
    (0x002a1428, "MultiFireProjectile::msg_run"),  # size=716, subsystem=C++ Runtime
    (0x002a16f8, "MultiFireProjectile::msg_collision"),  # size=792, subsystem=C++ Runtime
    (0x002a1a10, "MultiFireProjectile::terminate"),  # size=288, subsystem=C++ Runtime
    (0x002a1bb0, "SkillMultiFire::constructor"),  # size=48, subsystem=Skills
    (0x002a1be0, "SkillMultiFire::initRamps"),  # size=148, subsystem=Skills
    (0x002a1c78, "SkillMultiFire::getRankDescription"),  # size=232, subsystem=Skills
    (0x002a1d60, "SkillMultiFire::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a1d98, "MultiFireProjectile::msg_draw"),  # size=192, subsystem=C++ Runtime
    (0x002a1e78, "ExplodeArrowProjectile::msg_run"),  # size=732, subsystem=C++ Runtime
    (0x002a2158, "ExplodeArrowProjectile::msg_collision"),  # size=556, subsystem=C++ Runtime
    (0x002a2388, "ExplodeArrowProjectile::terminate"),  # size=572, subsystem=C++ Runtime
    (0x002a2648, "SkillExplodeArrow::constructor"),  # size=48, subsystem=Skills
    (0x002a2678, "SkillExplodeArrow::initRamps"),  # size=164, subsystem=Skills
    (0x002a2720, "SkillExplodeArrow::cast"),  # size=192, subsystem=Skills
    (0x002a27e0, "SkillExplodeArrow::getRankDescription"),  # size=280, subsystem=Skills
    (0x002a28f8, "SkillExplodeArrow::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a2930, "ExplodeArrowProjectile::constructor"),  # size=296, subsystem=C++ Runtime
    (0x002a2a58, "ExplodeArrowProjectile::msg_draw"),  # size=192, subsystem=C++ Runtime
    (0x002a2b38, "SkillArchery::constructor"),  # size=48, subsystem=Skills
    (0x002a2b68, "SkillArchery::initRamps"),  # size=48, subsystem=Skills
    (0x002a2b98, "SkillArchery::getRankDescription"),  # size=136, subsystem=Skills
    (0x002a2c20, "SkillArchery::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a2c58, "SkillArchery::getDamageScale"),  # size=108, subsystem=Skills
    (0x002a2cc8, "FireFlare::msg_run"),  # size=3600, subsystem=Renderer
    (0x002a3ad8, "SpellFireFlares::constructor"),  # size=1032, subsystem=Spells
    (0x002a3ee0, "SpellFireFlares::~destructor"),  # size=232, subsystem=Spells
    (0x002a3fc8, "SpellFireFlares::run"),  # size=592, subsystem=Spells
    (0x002a4218, "SkillFireFlares::getRankDescription"),  # size=784, subsystem=Skills
    (0x002a4670, "FireFlare::constructor"),  # size=224, subsystem=Renderer
    (0x002a4750, "FireFlare::msg_draw"),  # size=264, subsystem=Renderer
    (0x002a4858, "SkillFireFlares::constructor"),  # size=44, subsystem=Skills
    (0x002a4888, "SkillFireFlares::initRamps"),  # size=88, subsystem=Skills
    (0x002a48e0, "SkillFireFlares::cast"),  # size=136, subsystem=Skills
    (0x002a4968, "SkillFireFlares::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002a4970, "SkillFireFlares::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a4978, "SkillFireFlares::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002a49a0, "SkillFireFlares::canCast"),  # size=52, subsystem=Skills
    (0x002a49f8, "SkillRiposte::getRankDescription"),  # size=268, subsystem=Skills
    (0x002a4b08, "SkillRiposte::handleCounter"),  # size=1128, subsystem=Skills
    (0x002a5058, "SkillRiposte::constructor"),  # size=48, subsystem=Skills
    (0x002a5088, "SkillRiposte::initRamps"),  # size=84, subsystem=Skills
    (0x002a50e0, "SkillRiposte::cast"),  # size=40, subsystem=Skills
    (0x002a5108, "SkillRiposte::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002a5110, "SkillRiposte::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a5138, "SkillBash::getRankDescription"),  # size=392, subsystem=Skills
    (0x002a52c0, "SpellBash::constructor"),  # size=384, subsystem=Spells
    (0x002a5440, "SpellBash::run"),  # size=1592, subsystem=Spells
    (0x002a5a78, "SpellBash::doEffect"),  # size=552, subsystem=Spells
    (0x002a5d28, "SkillBash::constructor"),  # size=44, subsystem=Skills
    (0x002a5d58, "SkillBash::initRamps"),  # size=108, subsystem=Skills
    (0x002a5dc8, "SkillBash::canCast"),  # size=120, subsystem=Skills
    (0x002a5e40, "SkillBash::cast"),  # size=200, subsystem=Skills
    (0x002a5f08, "SkillBash::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a5f40, "SkillBash::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a5f48, "SpellBash::canQueue"),  # size=8, subsystem=Spells
    (0x002a5f70, "SpellBlessed::constructor"),  # size=856, subsystem=Spells
    (0x002a62c8, "SpellBlessed::run"),  # size=2404, subsystem=Spells
    (0x002a6d20, "SpellBlessed::~destructor"),  # size=144, subsystem=Spells
    (0x002a6db0, "SpellBlessed::getRegenAmount"),  # size=56, subsystem=Spells
    (0x002a6de8, "SkillBlessed::constructor"),  # size=44, subsystem=Skills
    (0x002a6e18, "SkillBlessed::initRamps"),  # size=84, subsystem=Skills
    (0x002a6e70, "SkillBlessed::cast"),  # size=204, subsystem=Skills
    (0x002a6f40, "SkillBlessed::getRankDescription"),  # size=136, subsystem=Skills
    (0x002a6fc8, "SkillBlessed::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002a6fd0, "SkillBlessed::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a6fd8, "SkillBlessed::canCast"),  # size=52, subsystem=Skills
    (0x002a7010, "SkillBlessed::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a7068, "SpellMinorHealing::constructor"),  # size=340, subsystem=Spells
    (0x002a71c0, "SpellMinorHealing::run"),  # size=252, subsystem=Spells
    (0x002a72c0, "SkillMinorHealing::constructor"),  # size=44, subsystem=Skills
    (0x002a72f0, "SkillMinorHealing::initRamps"),  # size=48, subsystem=Skills
    (0x002a7320, "SkillMinorHealing::cast"),  # size=160, subsystem=Skills
    (0x002a73c0, "SkillMinorHealing::getRankDescription"),  # size=136, subsystem=Skills
    (0x002a7448, "SkillMinorHealing::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a7480, "SkillMinorHealing::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a7488, "SkillAncestralCall::getRankDescription"),  # size=404, subsystem=Skills
    (0x002a7620, "SpellAncestralCall::constructor"),  # size=844, subsystem=Spells
    (0x002a7970, "SpellAncestralCall::run"),  # size=2156, subsystem=Spells
    (0x002a81e0, "SpellAncestralCall::posInAura"),  # size=336, subsystem=Spells
    (0x002a83b8, "SkillAncestralCall::canCast"),  # size=52, subsystem=Skills
    (0x002a83f0, "SkillAncestralCall::constructor"),  # size=48, subsystem=Skills
    (0x002a8420, "SkillAncestralCall::initRamps"),  # size=108, subsystem=Skills
    (0x002a8490, "SkillAncestralCall::cast"),  # size=160, subsystem=Skills
    (0x002a8530, "SkillAncestralCall::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002a8568, "SpellAncestralCall::getDamageScale"),  # size=72, subsystem=Spells
    (0x002a85b0, "SpellAncestralCall::getAttackSpeedScale"),  # size=72, subsystem=Spells
    (0x002a85f8, "SpellAncestralCall::runEffect"),  # size=148, subsystem=Spells
    (0x002a86b0, "SkillSummonSkeleton::cast"),  # size=1972, subsystem=Skills
    (0x002a8f58, "SpellSummonSkeleton::constructor"),  # size=136, subsystem=Spells
    (0x002a8fe0, "SpellSummonSkeleton::run"),  # size=92, subsystem=Spells
    (0x002a9040, "SkillSummonSkeleton::constructor"),  # size=44, subsystem=Skills
    (0x002a9070, "SkillSummonSkeleton::initRamps"),  # size=56, subsystem=Skills
    (0x002a90a8, "SkillSummonSkeleton::getRankDescription"),  # size=196, subsystem=Skills
    (0x002a9170, "SkillSummonSkeleton::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002a9178, "SkillSummonSkeleton::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002a9180, "SkillSummonSkeleton::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002a91a8, "SkillSummonSkeleton::canCast"),  # size=84, subsystem=Skills
    (0x002a9220, "SpellLightningWeapons::constructor"),  # size=1176, subsystem=Particles
    (0x002a96b8, "SpellLightningWeapons::run"),  # size=1048, subsystem=Particles
    (0x002a9ad0, "SkillLightningWeapons::getRankDescription"),  # size=592, subsystem=Particles
    (0x002a9d20, "SkillLightningWeapons::constructor"),  # size=44, subsystem=Particles
    (0x002a9d50, "SkillLightningWeapons::initRamps"),  # size=112, subsystem=Particles
    (0x002a9dc0, "SkillLightningWeapons::cast"),  # size=132, subsystem=Particles
    (0x002a9e48, "SkillLightningWeapons::getSkillPointCost"),  # size=8, subsystem=Particles
    (0x002a9e50, "SkillLightningWeapons::getLevelRequirement"),  # size=8, subsystem=Particles
    (0x002a9e58, "SkillLightningWeapons::getEnergyCost"),  # size=40, subsystem=Particles
    (0x002a9e80, "SkillLightningWeapons::canCast"),  # size=52, subsystem=Particles
    (0x002a9eb8, "SpellFireWeapons::constructor"),  # size=1124, subsystem=Spells
    (0x002aa320, "SpellFireWeapons::run"),  # size=3144, subsystem=Spells
    (0x002aaf68, "SkillFireWeapons::getRankDescription"),  # size=592, subsystem=Skills
    (0x002ab300, "SpellFireWeapons::~destructor"),  # size=144, subsystem=Spells
    (0x002ab390, "SkillFireWeapons::constructor"),  # size=44, subsystem=Skills
    (0x002ab3c0, "SkillFireWeapons::initRamps"),  # size=112, subsystem=Skills
    (0x002ab430, "SkillFireWeapons::cast"),  # size=132, subsystem=Skills
    (0x002ab4b8, "SkillFireWeapons::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002ab4c0, "SkillFireWeapons::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002ab4c8, "SkillFireWeapons::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002ab4f0, "SkillFireWeapons::canCast"),  # size=52, subsystem=Skills
    (0x002ab548, "SpellColdWeapons::constructor"),  # size=1168, subsystem=Spells
    (0x002ab9d8, "SpellColdWeapons::run"),  # size=1556, subsystem=Spells
    (0x002abff0, "SkillColdWeapons::getRankDescription"),  # size=592, subsystem=Skills
    (0x002ac330, "SkillColdWeapons::constructor"),  # size=44, subsystem=Skills
    (0x002ac360, "SkillColdWeapons::initRamps"),  # size=116, subsystem=Skills
    (0x002ac3d8, "SkillColdWeapons::cast"),  # size=132, subsystem=Skills
    (0x002ac460, "SkillColdWeapons::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002ac468, "SkillColdWeapons::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002ac470, "SkillColdWeapons::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002ac498, "SkillColdWeapons::canCast"),  # size=52, subsystem=Skills
    (0x002ac4f0, "SkillRoot::cast"),  # size=500, subsystem=Skills
    (0x002ac6e8, "SpellRoot::run"),  # size=1612, subsystem=Spells
    (0x002ace88, "SkillRoot::constructor"),  # size=44, subsystem=Skills
    (0x002aceb8, "SkillRoot::initRamps"),  # size=84, subsystem=Skills
    (0x002acf10, "SkillRoot::getRankDescription"),  # size=260, subsystem=Skills
    (0x002ad018, "SkillRoot::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002ad050, "SkillRoot::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002ad058, "SpellRoot::constructor"),  # size=164, subsystem=Spells
    (0x002ad100, "SpellRoot::~destructor"),  # size=116, subsystem=Spells
    (0x002ad198, "SkillCriticalHit::getCriticalChance"),  # size=604, subsystem=Skills
    (0x002ad3f8, "SpellCriticalHit::constructor"),  # size=304, subsystem=Spells
    (0x002ad528, "SpellCriticalHit::run"),  # size=1408, subsystem=Spells
    (0x002adb38, "SkillCriticalHit::canCast"),  # size=52, subsystem=Skills
    (0x002adb70, "SkillCriticalHit::constructor"),  # size=44, subsystem=Skills
    (0x002adba0, "SkillCriticalHit::initRamps"),  # size=88, subsystem=Skills
    (0x002adbf8, "SkillCriticalHit::cast"),  # size=132, subsystem=Skills
    (0x002adc80, "SkillCriticalHit::getRankDescription"),  # size=244, subsystem=Skills
    (0x002add78, "SkillCriticalHit::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002addb0, "SkillCriticalHit::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002addb8, "SpellCriticalHit::runEffect"),  # size=52, subsystem=Spells
    (0x002ade10, "SkillHolyShield::getRankDescription"),  # size=300, subsystem=Skills
    (0x002adf40, "SpellHolyShield::constructor"),  # size=288, subsystem=Spells
    (0x002ae060, "SpellHolyShield::manaAbsorbOnHit"),  # size=864, subsystem=Spells
    (0x002ae440, "SkillHolyShield::constructor"),  # size=44, subsystem=Skills
    (0x002ae470, "SkillHolyShield::initRamps"),  # size=68, subsystem=Skills
    (0x002ae4b8, "SkillHolyShield::cast"),  # size=160, subsystem=Skills
    (0x002ae558, "SkillHolyShield::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002ae590, "SpellHolyShield::run"),  # size=264, subsystem=Spells
    (0x002ae6b8, "SkillDodge::constructor"),  # size=48, subsystem=Skills
    (0x002ae6e8, "SkillDodge::initRamps"),  # size=48, subsystem=Skills
    (0x002ae718, "SkillDodge::getRankDescription"),  # size=136, subsystem=Skills
    (0x002ae7a0, "SkillDodge::getEnergyCost"),  # size=56, subsystem=Skills
    (0x002ae7d8, "SkillDodge::getDeflectionChance"),  # size=116, subsystem=Skills
    (0x002ae850, "SkillHealing::getRankDescription"),  # size=388, subsystem=Skills
    (0x002ae9d8, "SpellHealing::constructor"),  # size=352, subsystem=Spells
    (0x002aeb38, "SpellHealing::run"),  # size=1600, subsystem=Spells
    (0x002af208, "SkillHealing::constructor"),  # size=44, subsystem=Skills
    (0x002af238, "SkillHealing::initRamps"),  # size=84, subsystem=Skills
    (0x002af290, "SkillHealing::cast"),  # size=160, subsystem=Skills
    (0x002af330, "SkillHealing::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002af368, "SkillHealing::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002af390, "SpellConeOfFrost::constructor"),  # size=376, subsystem=Spells
    (0x002af508, "SpellConeOfFrost::run"),  # size=1616, subsystem=Spells
    (0x002afca0, "SkillConeOfFrost::constructor"),  # size=48, subsystem=Skills
    (0x002afcd0, "SkillConeOfFrost::initRamps"),  # size=84, subsystem=Skills
    (0x002afd28, "SkillConeOfFrost::cast"),  # size=160, subsystem=Skills
    (0x002afdc8, "SkillConeOfFrost::getRankDescription"),  # size=252, subsystem=Skills
    (0x002afec8, "SkillConeOfFrost::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002aff00, "SpellConeOfFrost::~destructor"),  # size=132, subsystem=Spells
    (0x002affa8, "SpellUndeadShield::constructor"),  # size=440, subsystem=Spells
    (0x002b0160, "SpellUndeadShield::~destructor"),  # size=168, subsystem=Spells
    (0x002b0208, "SpellUndeadShield::run"),  # size=1604, subsystem=Spells
    (0x002b0850, "SpellUndeadShield::handleShieldHit"),  # size=404, subsystem=Spells
    (0x002b09e8, "SpellSecondaryUndeadShield::run"),  # size=1156, subsystem=Spells
    (0x002b0e70, "SpellSecondaryUndeadShield::handleShieldHit"),  # size=340, subsystem=Spells
    (0x002b10b8, "SpellSecondaryUndeadShield::constructor"),  # size=156, subsystem=Spells
    (0x002b1158, "SpellSecondaryUndeadShield::~destructor"),  # size=116, subsystem=Spells
    (0x002b11d0, "SkillUndeadShield::constructor"),  # size=44, subsystem=Skills
    (0x002b1200, "SkillUndeadShield::initRamps"),  # size=76, subsystem=Skills
    (0x002b1250, "SkillUndeadShield::cast"),  # size=132, subsystem=Skills
    (0x002b12d8, "SkillUndeadShield::getRankDescription"),  # size=244, subsystem=Skills
    (0x002b13d0, "SkillUndeadShield::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b13d8, "SkillUndeadShield::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b13e0, "SkillUndeadShield::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002b1408, "SkillUndeadShield::canCast"),  # size=52, subsystem=Skills
    (0x002b1460, "HolyStrike::constructor"),  # size=504, subsystem=Renderer
    (0x002b1658, "HolyStrike::msg_run"),  # size=3780, subsystem=Renderer
    (0x002b2520, "HolyStrike::msg_collision"),  # size=680, subsystem=Renderer
    (0x002b27c8, "HolyStrike::msg_draw"),  # size=348, subsystem=Renderer
    (0x002b2928, "SkillHolyStrike::getRankDescription"),  # size=612, subsystem=Skills
    (0x002b2cd8, "SkillHolyStrike::constructor"),  # size=44, subsystem=Skills
    (0x002b2d08, "SkillHolyStrike::initRamps"),  # size=72, subsystem=Skills
    (0x002b2d50, "SkillHolyStrike::cast"),  # size=192, subsystem=Skills
    (0x002b2e10, "SkillHolyStrike::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b2e18, "SkillHolyStrike::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b2e20, "SkillHolyStrike::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002b2e48, "SkillHolyStrike::canCast"),  # size=8, subsystem=Skills
    (0x002b2e70, "SkillShockOfFire::cast"),  # size=416, subsystem=Skills
    (0x002b3010, "SkillShockOfFire::getRankDescription"),  # size=352, subsystem=Skills
    (0x002b3170, "SkillShockOfFire::constructor"),  # size=44, subsystem=Skills
    (0x002b31a0, "SkillShockOfFire::initRamps"),  # size=184, subsystem=Skills
    (0x002b3258, "SkillShockOfFire::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002b3290, "SkillShockOfFire::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b3298, "SkillFrostStorm::cast"),  # size=580, subsystem=Skills
    (0x002b34e0, "SkillFrostStorm::constructor"),  # size=44, subsystem=Skills
    (0x002b3510, "SkillFrostStorm::initRamps"),  # size=180, subsystem=Skills
    (0x002b35c8, "SkillFrostStorm::getRankDescription"),  # size=252, subsystem=Skills
    (0x002b36c8, "SkillFrostStorm::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002b3700, "HammerOfWrath::constructor"),  # size=612, subsystem=Game Entities
    (0x002b3968, "HammerOfWrath::msg_run"),  # size=4744, subsystem=Game Entities
    (0x002b4bf0, "HammerOfWrath::msg_draw"),  # size=1236, subsystem=Game Entities
    (0x002b50c8, "SkillHammerOfWrath::cast"),  # size=644, subsystem=Skills
    (0x002b5350, "SkillHammerOfWrath::getRankDescription"),  # size=384, subsystem=Skills
    (0x002b5610, "HammerOfWrath::~destructor"),  # size=148, subsystem=Game Entities
    (0x002b56a8, "SpellHammerOfWrath::constructor"),  # size=136, subsystem=Spells
    (0x002b5730, "SpellHammerOfWrath::run"),  # size=92, subsystem=Spells
    (0x002b5790, "SkillHammerOfWrath::constructor"),  # size=44, subsystem=Skills
    (0x002b57c0, "SkillHammerOfWrath::initRamps"),  # size=72, subsystem=Skills
    (0x002b5808, "SkillHammerOfWrath::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b5810, "SkillHammerOfWrath::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b5818, "SkillHammerOfWrath::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002b5840, "SkillHammerOfWrath::canCast"),  # size=52, subsystem=Skills
    (0x002b5898, "SpellConeOfFire::constructor"),  # size=360, subsystem=Spells
    (0x002b5a00, "SpellConeOfFire::~destructor"),  # size=216, subsystem=Spells
    (0x002b5ad8, "SpellConeOfFire::run"),  # size=3248, subsystem=Spells
    (0x002b6788, "SkillConeOfFire::getRankDescription"),  # size=268, subsystem=Skills
    (0x002b69e0, "SkillConeOfFire::constructor"),  # size=48, subsystem=Skills
    (0x002b6a10, "SkillConeOfFire::initRamps"),  # size=92, subsystem=Skills
    (0x002b6a70, "SkillConeOfFire::cast"),  # size=132, subsystem=Skills
    (0x002b6af8, "SkillConeOfFire::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b6b00, "SkillConeOfFire::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b6b08, "SkillConeOfFire::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002b6b30, "SkillConeOfFire::canCast"),  # size=8, subsystem=Skills
    (0x002b6b58, "SkillRegeneration::constructor"),  # size=48, subsystem=Skills
    (0x002b6b88, "SkillRegeneration::initRamps"),  # size=28, subsystem=Skills
    (0x002b6ba8, "SkillRegeneration::cast"),  # size=40, subsystem=Skills
    (0x002b6bd0, "SkillRegeneration::getRankDescription"),  # size=136, subsystem=Skills
    (0x002b6c58, "SkillRegeneration::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b6c60, "SkillRegeneration::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b6c68, "SkillRegeneration::getRegenAmount"),  # size=56, subsystem=Skills
    (0x002b6ca0, "SpellWizardBeam::constructor"),  # size=1080, subsystem=Spells
    (0x002b70d8, "SpellWizardBeam::run"),  # size=7688, subsystem=Spells
    (0x002b8ee0, "SpellWizardBeam::~destructor"),  # size=300, subsystem=Spells
    (0x002b9010, "SkillWizardBeam::getRankDescription"),  # size=524, subsystem=Skills
    (0x002b9368, "SkillWizardBeam::constructor"),  # size=48, subsystem=Skills
    (0x002b9398, "SkillWizardBeam::initRamps"),  # size=88, subsystem=Skills
    (0x002b93f0, "SkillWizardBeam::cast"),  # size=132, subsystem=Skills
    (0x002b9478, "SkillWizardBeam::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002b9480, "SkillWizardBeam::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002b9488, "SkillWizardBeam::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002b94d0, "BlindingLightEffect::constructor"),  # size=916, subsystem=Game Entities
    (0x002b9868, "BlindingLightEffect::msg_run"),  # size=440, subsystem=Game Entities
    (0x002b9a20, "SpellBlindingLight::run"),  # size=444, subsystem=Spells
    (0x002b9be0, "SkillBlindingLight::cast"),  # size=396, subsystem=Skills
    (0x002b9d70, "SkillBlindingLight::getRankDescription"),  # size=364, subsystem=Skills
    (0x002ba028, "SpellBlindingLight::constructor"),  # size=184, subsystem=Spells
    (0x002ba0e0, "SkillBlindingLight::constructor"),  # size=44, subsystem=Skills
    (0x002ba110, "SkillBlindingLight::initRamps"),  # size=100, subsystem=Skills
    (0x002ba178, "SkillBlindingLight::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002ba180, "SkillBlindingLight::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002ba188, "SkillBlindingLight::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002ba1b0, "SkillBlindingLight::canCast"),  # size=8, subsystem=Skills
    (0x002ba1d8, "SkillRepulseUndead::cast"),  # size=732, subsystem=Skills
    (0x002ba600, "SkillRepulseUndead::constructor"),  # size=44, subsystem=Skills
    (0x002ba630, "SkillRepulseUndead::initRamps"),  # size=56, subsystem=Skills
    (0x002ba668, "SkillRepulseUndead::getRankDescription"),  # size=196, subsystem=Skills
    (0x002ba730, "SkillRepulseUndead::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002ba738, "SkillRepulseUndead::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002ba740, "SkillRepulseUndead::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002ba788, "HolyBolt::constructor"),  # size=1348, subsystem=Renderer
    (0x002bacd0, "HolyBolt::msg_run"),  # size=1568, subsystem=Renderer
    (0x002bb2f0, "HolyBolt::msg_draw"),  # size=444, subsystem=Renderer
    (0x002bb4b0, "HolyBolt::msg_collision"),  # size=980, subsystem=Renderer
    (0x002bb888, "SkillDismissUndead::getRankDescription"),  # size=384, subsystem=Skills
    (0x002bbc18, "SkillDismissUndead::constructor"),  # size=44, subsystem=Skills
    (0x002bbc48, "SkillDismissUndead::initRamps"),  # size=72, subsystem=Skills
    (0x002bbc90, "SkillDismissUndead::cast"),  # size=144, subsystem=Skills
    (0x002bbd20, "SkillDismissUndead::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002bbd28, "SkillDismissUndead::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002bbd30, "SkillDismissUndead::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002bbd78, "FrostShard::msg_draw"),  # size=284, subsystem=C++ Runtime
    (0x002bbe98, "FrostShard::msg_run"),  # size=1676, subsystem=C++ Runtime
    (0x002bc528, "FrostShard::msg_collision"),  # size=604, subsystem=C++ Runtime
    (0x002bc788, "ShockOfFrost::constructor"),  # size=492, subsystem=Physics
    (0x002bc978, "ShockOfFrost::~destructor"),  # size=168, subsystem=Physics
    (0x002bca20, "ShockOfFrost::msg_run"),  # size=3548, subsystem=Physics
    (0x002bd800, "ShockOfFrost::msg_collision"),  # size=588, subsystem=Physics
    (0x002bda50, "SkillShockOfFrost::getRankDescription"),  # size=540, subsystem=Skills
    (0x002bddb8, "FrostShard::constructor"),  # size=308, subsystem=C++ Runtime
    (0x002bdef0, "ShockOfFrost::msg_draw"),  # size=280, subsystem=Physics
    (0x002be008, "SkillShockOfFrost::constructor"),  # size=44, subsystem=Skills
    (0x002be038, "SkillShockOfFrost::initRamps"),  # size=140, subsystem=Skills
    (0x002be0c8, "SkillShockOfFrost::cast"),  # size=144, subsystem=Skills
    (0x002be158, "SkillShockOfFrost::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002be160, "SkillShockOfFrost::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002be168, "SkillShockOfFrost::getEnergyCost"),  # size=36, subsystem=Skills
    (0x002be190, "SkillShockOfFrost::canCast"),  # size=8, subsystem=Skills
    (0x002be1b8, "SkillLifeTap::constructor"),  # size=48, subsystem=Skills
    (0x002be1e8, "SkillLifeTap::initRamps"),  # size=48, subsystem=Skills
    (0x002be218, "SkillLifeTap::cast"),  # size=40, subsystem=Skills
    (0x002be240, "SkillLifeTap::getRankDescription"),  # size=196, subsystem=Skills
    (0x002be308, "SkillLifeTap::getEnergyCost"),  # size=56, subsystem=Skills
    (0x002be340, "SkillLifeTap::getChance"),  # size=108, subsystem=Skills
    (0x002be3b0, "SkillLifeTap::getAmount"),  # size=92, subsystem=Skills
    (0x002be410, "PoisonRain::constructor"),  # size=704, subsystem=Game Entities
    (0x002be6d0, "PoisonRain::msg_run"),  # size=1708, subsystem=Game Entities
    (0x002bed80, "SkillPoisonRain::cast"),  # size=324, subsystem=Skills
    (0x002beec8, "SkillPoisonRain::getRankDescription"),  # size=488, subsystem=Skills
    (0x002bf198, "SkillPoisonRain::constructor"),  # size=44, subsystem=Skills
    (0x002bf1c8, "SkillPoisonRain::initRamps"),  # size=104, subsystem=Skills
    (0x002bf230, "SkillPoisonRain::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x002bf238, "SkillPoisonRain::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002bf240, "SkillPoisonRain::getEnergyCost"),  # size=40, subsystem=Skills
    (0x002bf268, "SkillPoisonRain::canCast"),  # size=8, subsystem=Skills
    (0x002bf290, "Boat::set"),  # size=328, subsystem=Game Props
    (0x002bf3d8, "Boat::doMyUniqueForces"),  # size=616, subsystem=Game Props
    (0x002bf640, "SkulBoat::set"),  # size=328, subsystem=Game Props
    (0x002bf788, "SkulBoat::doMyUniqueForces"),  # size=660, subsystem=Game Props
    (0x002bfa20, "Boat::constructor"),  # size=208, subsystem=Game Props
    (0x002bfaf0, "SkulBoat::constructor"),  # size=208, subsystem=Game Props
    (0x002c57e8, "SkillClericRoot::cast"),  # size=460, subsystem=Skills
    (0x002c59b8, "SpellClericRoot::run"),  # size=1612, subsystem=Spells
    (0x002c6158, "SkillClericRoot::constructor"),  # size=44, subsystem=Skills
    (0x002c6188, "SkillClericRoot::initRamps"),  # size=76, subsystem=Skills
    (0x002c61d8, "SkillClericRoot::getRankDescription"),  # size=260, subsystem=Skills
    (0x002c62e0, "SkillClericRoot::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002c6318, "SkillClericRoot::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002c6320, "SpellClericRoot::constructor"),  # size=164, subsystem=Spells
    (0x002c63c8, "SpellClericRoot::~destructor"),  # size=116, subsystem=Spells
    (0x002c6460, "SkillEntangle::cast"),  # size=460, subsystem=Skills
    (0x002c6630, "SpellEntangle::run"),  # size=1612, subsystem=Spells
    (0x002c6dd0, "SkillEntangle::constructor"),  # size=44, subsystem=Skills
    (0x002c6e00, "SkillEntangle::initRamps"),  # size=80, subsystem=Skills
    (0x002c6e50, "SkillEntangle::getRankDescription"),  # size=260, subsystem=Skills
    (0x002c6f58, "SkillEntangle::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002c6f90, "SkillEntangle::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002c6f98, "SpellEntangle::constructor"),  # size=164, subsystem=Spells
    (0x002c7040, "SpellEntangle::~destructor"),  # size=116, subsystem=Spells
    (0x002c70d8, "SkillRangerCriticalHit::getRankDescription"),  # size=348, subsystem=Skills
    (0x002c7238, "SkillRangerCriticalHit::getCriticalChance"),  # size=604, subsystem=Skills
    (0x002c7498, "SpellRangerCriticalHit::constructor"),  # size=308, subsystem=Spells
    (0x002c75d0, "SpellRangerCriticalHit::run"),  # size=1388, subsystem=Spells
    (0x002c7bd0, "SkillRangerCriticalHit::constructor"),  # size=44, subsystem=Skills
    (0x002c7c00, "SkillRangerCriticalHit::initRamps"),  # size=96, subsystem=Skills
    (0x002c7c60, "SkillRangerCriticalHit::cast"),  # size=132, subsystem=Skills
    (0x002c7ce8, "SkillRangerCriticalHit::canCast"),  # size=52, subsystem=Skills
    (0x002c7d20, "SkillRangerCriticalHit::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002c7d58, "SkillRangerCriticalHit::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002c7d60, "SpellRangerCriticalHit::runEffect"),  # size=44, subsystem=Spells
    (0x002c7db0, "SkillShieldBash::getRankDescription"),  # size=392, subsystem=Skills
    (0x002c7f38, "SpellShieldBash::constructor"),  # size=384, subsystem=Spells
    (0x002c80b8, "SpellShieldBash::run"),  # size=1600, subsystem=Spells
    (0x002c86f8, "SpellShieldBash::doEffect"),  # size=552, subsystem=Spells
    (0x002c89a8, "SkillShieldBash::constructor"),  # size=44, subsystem=Skills
    (0x002c89d8, "SkillShieldBash::initRamps"),  # size=104, subsystem=Skills
    (0x002c8a40, "SkillShieldBash::canCast"),  # size=120, subsystem=Skills
    (0x002c8ab8, "SkillShieldBash::cast"),  # size=160, subsystem=Skills
    (0x002c8b58, "SkillShieldBash::getEnergyCost"),  # size=52, subsystem=Skills
    (0x002c8b90, "SkillShieldBash::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x002c8b98, "SpellShieldBash::canQueue"),  # size=8, subsystem=Spells
    (0x002c8bc0, "SpellPlanarSteelEffect::constructor"),  # size=488, subsystem=Spells
    (0x002c8da8, "SpellPlanarSteelEffect::run"),  # size=2616, subsystem=Spells
    (0x002c9988, "SpellPlanarSteelEffect::~destructor"),  # size=144, subsystem=Spells
    (0x002c9a38, "SpellHornOmenEffect::run"),  # size=2052, subsystem=Spells
    (0x002ca2c8, "SpellHornOmenEffect::constructor"),  # size=144, subsystem=Spells
    (0x002ca358, "SpellHornOmenEffect::~destructor"),  # size=116, subsystem=Spells
    (0x002cb4a0, "VIKeyboard::Read"),  # size=1352, subsystem=Engine (VIKeyboard)
    (0x002cb9e8, "VIKeyboard::PrepareQueueKeyEvent"),  # size=504, subsystem=Engine (VIKeyboard)
    (0x002cbbe0, "VIKeyboard::CombineDeadkey"),  # size=696, subsystem=Engine (VIKeyboard)
    (0x002cbef0, "VIKeyboard::constructor"),  # size=12, subsystem=Engine (VIKeyboard)
    (0x002cbf00, "VIKeyboard::~destructor"),  # size=44, subsystem=Engine (VIKeyboard)
    (0x002cbf30, "VIKeyboard::Init"),  # size=84, subsystem=Engine (VIKeyboard)
    (0x002cbf88, "VIKeyboard::Free"),  # size=80, subsystem=Engine (VIKeyboard)
    (0x002cbfd8, "VIKeyboard::TranslateEvent"),  # size=148, subsystem=Engine (VIKeyboard)
    (0x002cc070, "VIKeyboard::QueueKeyEvent"),  # size=64, subsystem=Engine (VIKeyboard)
    (0x002cc0b0, "VIKeyboard::DequeueKeyEvent"),  # size=120, subsystem=Engine (VIKeyboard)
    (0x002fd2a8, "type_info::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0030d510, "Creature::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x0030d560, "Creature::setState"),  # size=8, subsystem=Game Entities
    (0x0030d568, "Creature::root"),  # size=8, subsystem=Game Entities
    (0x0030d570, "Creature::getModel"),  # size=12, subsystem=Game Entities
    (0x0030d580, "Creature::getSkillRank"),  # size=8, subsystem=Game Entities
    (0x0030d588, "GroundPoundEffect::~destructor"),  # size=124, subsystem=Game Entities
    (0x0030d608, "GroundPoundEffect::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x0030d658, "Projectile::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x0030d6c8, "Projectile::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030d718, "Player1::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030d780, "Player1::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030d7d0, "charAmbient_Light::~destructor"),  # size=100, subsystem=Lighting
    (0x0030d838, "charAmbient_Light::__typeinfo"),  # size=76, subsystem=Lighting
    (0x0030d888, "charDirectional_Light::~destructor"),  # size=100, subsystem=Lighting
    (0x0030d8f0, "charDirectional_Light::__typeinfo"),  # size=76, subsystem=Lighting
    (0x0030d940, "charDirectional_LightD::~destructor"),  # size=100, subsystem=Lighting
    (0x0030d9a8, "charDirectional_LightD::__typeinfo"),  # size=76, subsystem=Lighting
    (0x0030d9f8, "WorldPart::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030da48, "Prop::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030dab0, "Prop::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030db00, "ParticleProp::~destructor"),  # size=100, subsystem=Particles
    (0x0030db68, "ParticleProp::__typeinfo"),  # size=132, subsystem=Particles
    (0x0030dbf0, "ItemProp::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030dc58, "ItemProp::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x0030dce0, "PhProp::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030dd48, "PhProp::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x0030ddd0, "PhIce::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030de38, "PhIce::__typeinfo"),  # size=176, subsystem=Game Entities
    (0x0030dee8, "Gold::~destructor"),  # size=116, subsystem=Renderer
    (0x0030df60, "Gold::__typeinfo"),  # size=76, subsystem=Renderer
    (0x0030dfb0, "Container::~destructor"),  # size=100, subsystem=Game Props
    (0x0030e018, "Container::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e068, "Ice::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030e0d0, "Ice::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x0030e120, "Chest::~destructor"),  # size=116, subsystem=Game Props
    (0x0030e198, "Chest::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e1e8, "CosmeticPropAnim::~destructor"),  # size=116, subsystem=Game Props
    (0x0030e260, "CosmeticPropAnim::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e2b0, "CosmeticProp::~destructor"),  # size=100, subsystem=Game Props
    (0x0030e318, "CosmeticProp::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e368, "UserParamProp::~destructor"),  # size=116, subsystem=Game Props
    (0x0030e3e0, "UserParamProp::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e430, "TriggerParams::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030e498, "TriggerParams::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030e4e8, "Trigger::~destructor"),  # size=100, subsystem=Game Props
    (0x0030e550, "Trigger::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e5a0, "Blocker::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030e608, "Blocker::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x0030e658, "WaveMaker::~destructor"),  # size=100, subsystem=Audio
    (0x0030e6c0, "WaveMaker::__typeinfo"),  # size=76, subsystem=Audio
    (0x0030e710, "PushTrigger::~destructor"),  # size=100, subsystem=Game Props
    (0x0030e778, "PushTrigger::__typeinfo"),  # size=76, subsystem=Game Props
    (0x0030e7c8, "Player::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030e818, "Player::setActiveChunks"),  # size=8, subsystem=Game Entities
    (0x0030e820, "Player::stun"),  # size=8, subsystem=Game Entities
    (0x0030e828, "Player::getModel"),  # size=8, subsystem=Game Entities
    (0x0030e830, "Player::getSkillRank"),  # size=24, subsystem=Game Entities
    (0x0030e848, "Ant::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030e8b0, "Ant::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030e900, "AntQueen::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030e968, "AntQueen::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030e9b8, "Badger::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030ea20, "Badger::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0030ea70, "BlackWidow::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030eae0, "BlackWidow::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030eb30, "Cat::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030eb98, "Cat::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030ebe8, "Critter::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030ec50, "Critter::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030eca0, "Critter::getModel"),  # size=8, subsystem=Game Entities
    (0x0030eca8, "Cyclops::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030ed10, "Cyclops::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030ed60, "FireBeetle::~destructor"),  # size=100, subsystem=Renderer
    (0x0030edc8, "FireBeetle::__typeinfo"),  # size=80, subsystem=Renderer
    (0x0030ee18, "FireFly::~destructor"),  # size=124, subsystem=Game Entities
    (0x0030ee98, "FireFly::__typeinfo"),  # size=136, subsystem=Game Entities
    (0x0030ef20, "FireFly::msg_moveCollision"),  # size=8, subsystem=Game Entities
    (0x0030ef28, "Froglock::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030ef90, "Froglock::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030efe0, "Generator::~destructor"),  # size=108, subsystem=Game Props
    (0x0030f050, "Generator::__typeinfo"),  # size=80, subsystem=Game Props
    (0x0030f0a0, "Generator::getModel"),  # size=8, subsystem=Game Props
    (0x0030f0a8, "Ghoul::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030f110, "Ghoul::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f160, "Gnome::~destructor"),  # size=108, subsystem=Renderer
    (0x0030f1d0, "Gnome::__typeinfo"),  # size=80, subsystem=Renderer
    (0x0030f220, "Goblin::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030f290, "Goblin::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f2e0, "LavaMonster::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030f348, "LavaMonster::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f398, "Orc::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030f408, "Orc::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f458, "Scorpion::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030f4c0, "Scorpion::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f510, "SmallSpider::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030f578, "SmallSpider::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0030f5c8, "Spider::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030f630, "Spider::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0030f680, "SpiderQueen::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030f6f0, "SpiderQueen::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f740, "SuperOrc::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030f7a8, "SuperOrc::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030f7f8, "CdEyeball::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030f860, "CdEyeball::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0030f8b0, "Vampire::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0030f918, "Vampire::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0030f968, "WoodElfSoldier::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030f9d8, "WoodElfSoldier::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030fa28, "Wraith::~destructor"),  # size=108, subsystem=Game Entities
    (0x0030fa98, "Wraith::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030fae8, "NPC::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030fb50, "NPC::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x0030fba0, "NPC::getModel"),  # size=8, subsystem=Game Entities
    (0x0030fba8, "GutChunk::~destructor"),  # size=100, subsystem=Renderer
    (0x0030fc10, "GutChunk::__typeinfo"),  # size=176, subsystem=Renderer
    (0x0030fcc0, "LooseIceChunk::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030fd28, "LooseIceChunk::__typeinfo"),  # size=176, subsystem=Game Entities
    (0x0030fdd8, "FrostStormIceChunk::~destructor"),  # size=100, subsystem=Game Entities
    (0x0030fe40, "FrostStormIceChunk::__typeinfo"),  # size=176, subsystem=Game Entities
    (0x0030fef0, "Torch::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x0030ff68, "Torch::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x0030ffb8, "Fire::~destructor"),  # size=100, subsystem=Game Props
    (0x00310020, "Fire::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00310070, "FlyingText::~destructor"),  # size=100, subsystem=Renderer
    (0x003100d8, "FlyingText::__typeinfo"),  # size=76, subsystem=Renderer
    (0x00310128, "Candle::~destructor"),  # size=116, subsystem=Renderer
    (0x003101a0, "Candle::__typeinfo"),  # size=76, subsystem=Renderer
    (0x003101f0, "Candle2::~destructor"),  # size=100, subsystem=Renderer
    (0x00310258, "Candle2::__typeinfo"),  # size=76, subsystem=Renderer
    (0x003102a8, "Lantern::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x00310320, "Lantern::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00310370, "Lamp::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x003103e8, "Lamp::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00310438, "FireEffect::~destructor"),  # size=108, subsystem=Game Entities
    (0x003104a8, "FireEffect::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x003104f8, "RecallEffect::~destructor"),  # size=100, subsystem=Game Entities
    (0x00310560, "RecallEffect::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x003105b0, "IceChunk::~destructor"),  # size=100, subsystem=Game Entities
    (0x00310618, "IceChunk::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00310668, "GlowingCylinder::~destructor"),  # size=100, subsystem=Game Entities
    (0x003106d0, "GlowingCylinder::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00310720, "GlowingShaft::~destructor"),  # size=100, subsystem=Renderer
    (0x00310788, "GlowingShaft::__typeinfo"),  # size=76, subsystem=Renderer
    (0x003107d8, "MissileTrap::~destructor"),  # size=100, subsystem=Game Props
    (0x00310840, "MissileTrap::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00310890, "Shooter::~destructor"),  # size=100, subsystem=Game Entities
    (0x003108f8, "Shooter::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00310948, "WaterSpout::~destructor"),  # size=100, subsystem=Renderer
    (0x003109b0, "WaterSpout::__typeinfo"),  # size=76, subsystem=Renderer
    (0x00310a00, "DummyDamager::~destructor"),  # size=108, subsystem=Renderer
    (0x00310a70, "DummyDamager::__typeinfo"),  # size=132, subsystem=Renderer
    (0x00310af8, "Sparks::~destructor"),  # size=132, subsystem=Renderer
    (0x00310b80, "Sparks::__typeinfo"),  # size=132, subsystem=Renderer
    (0x00310c08, "HolyBolt::~destructor"),  # size=132, subsystem=Renderer
    (0x00310c90, "HolyBolt::__typeinfo"),  # size=132, subsystem=Renderer
    (0x00310d18, "OniBall::~destructor"),  # size=132, subsystem=Game Entities
    (0x00310da0, "OniBall::__typeinfo"),  # size=132, subsystem=Game Entities
    (0x00310e28, "LostSoul::~destructor"),  # size=132, subsystem=Game Entities
    (0x00310eb0, "LostSoul::__typeinfo"),  # size=132, subsystem=Game Entities
    (0x00310f38, "Root::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x00310fc0, "Root::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00311048, "UnholyAura::~destructor"),  # size=124, subsystem=Game Entities
    (0x003110c8, "UnholyAura::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00311118, "IceBall::~destructor"),  # size=132, subsystem=Projectiles
    (0x003111a0, "IceBall::__typeinfo"),  # size=132, subsystem=Projectiles
    (0x00311228, "MissileWeapon::__typeinfo"),  # size=132, subsystem=Projectiles
    (0x003112b0, "AnimatedMissile::~destructor"),  # size=132, subsystem=Renderer
    (0x00311338, "AnimatedMissile::__typeinfo"),  # size=132, subsystem=Renderer
    (0x003113c0, "AnimatedMissile::msg_draw"),  # size=8, subsystem=Renderer
    (0x003113c8, "AnimatedMissile::getCollisionEffect"),  # size=8, subsystem=Renderer
    (0x003113d0, "playerProjectile::~destructor"),  # size=108, subsystem=Renderer
    (0x00311440, "playerProjectile::__typeinfo"),  # size=176, subsystem=Renderer
    (0x003114f0, "beetleProjectile::~destructor"),  # size=108, subsystem=Physics
    (0x00311560, "beetleProjectile::__typeinfo"),  # size=176, subsystem=Physics
    (0x00311610, "WebTrap::~destructor"),  # size=108, subsystem=Game Props
    (0x00311680, "WebTrap::__typeinfo"),  # size=76, subsystem=Game Props
    (0x003116d0, "LooseFire::~destructor"),  # size=108, subsystem=Game Props
    (0x00311740, "LooseFire::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00311790, "ShockProjectile::__typeinfo"),  # size=76, subsystem=Projectiles
    (0x003117e0, "LightEffect::~destructor"),  # size=124, subsystem=Lighting
    (0x00311860, "LightEffect::__typeinfo"),  # size=76, subsystem=Lighting
    (0x003118b0, "DoorSwing::~destructor"),  # size=100, subsystem=Game Props
    (0x00311918, "DoorSwing::__typeinfo"),  # size=132, subsystem=Game Props
    (0x003119a0, "RollDoor::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00311a08, "RollDoor::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00311a90, "DoorSecret::~destructor"),  # size=100, subsystem=Game Props
    (0x00311af8, "DoorSecret::__typeinfo"),  # size=132, subsystem=Game Props
    (0x00311b80, "Switch::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00311be8, "Switch::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00311c70, "FloorSwitch::~destructor"),  # size=100, subsystem=Game Props
    (0x00311cd8, "FloorSwitch::__typeinfo"),  # size=132, subsystem=Game Props
    (0x00311d60, "FallPlatform::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00311dc8, "FallPlatform::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00311e50, "FireTrail::~destructor"),  # size=108, subsystem=Game Entities
    (0x00311ec0, "FireTrail::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00311f10, "FireTrailMaker::~destructor"),  # size=124, subsystem=Game Entities
    (0x00311f90, "FireTrailMaker::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00311fe0, "Savepoint::~destructor"),  # size=124, subsystem=Game Props
    (0x00312060, "Savepoint::__typeinfo"),  # size=76, subsystem=Game Props
    (0x003120b0, "JumpGate::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00312100, "FireBomb::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00312168, "FireBomb::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x003121b8, "FireBombletJr::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00312220, "FireBombletJr::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00312270, "StaticFire::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x003122c0, "PokeReflector::~destructor"),  # size=100, subsystem=Game Entities
    (0x00312328, "PokeReflector::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00312378, "Lever::~destructor"),  # size=100, subsystem=Game Props
    (0x003123e0, "Lever::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00312430, "Counter::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00312498, "Counter::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x003124e8, "Timer::~destructor"),  # size=100, subsystem=Game Props
    (0x00312550, "Timer::__typeinfo"),  # size=76, subsystem=Game Props
    (0x003125a0, "ShopDaemon::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00312608, "ShopDaemon::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00312658, "WeaponRack::~destructor"),  # size=100, subsystem=Renderer
    (0x003126c0, "WeaponRack::__typeinfo"),  # size=76, subsystem=Renderer
    (0x00312710, "Weather::~destructor"),  # size=100, subsystem=Game Entities
    (0x00312778, "Weather::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x003127c8, "Teleporter::~destructor"),  # size=100, subsystem=Renderer
    (0x00312830, "Teleporter::__typeinfo"),  # size=80, subsystem=Renderer
    (0x00312880, "Teleporter::setActiveChunks"),  # size=8, subsystem=Renderer
    (0x00312888, "poisonGasSpell::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x003128f8, "poisonGasSpell::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00312948, "dustCloud::~destructor"),  # size=100, subsystem=Projectiles
    (0x003129b0, "dustCloud::__typeinfo"),  # size=76, subsystem=Projectiles
    (0x00312a00, "FrostStormSpell::~destructor"),  # size=124, subsystem=C++ Runtime
    (0x00312a80, "FrostStormSpell::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00312ad0, "AntWave::__typeinfo"),  # size=80, subsystem=Audio
    (0x00312b20, "PointSourceSound::__typeinfo"),  # size=76, subsystem=Audio
    (0x00312b70, "PushPhysicsProp::~destructor"),  # size=100, subsystem=Renderer
    (0x00312bd8, "PushPhysicsProp::__typeinfo"),  # size=76, subsystem=Renderer
    (0x00312c28, "VehicleBodySphere::~destructor"),  # size=100, subsystem=Physics
    (0x00312c90, "VehicleBodySphere::__typeinfo"),  # size=76, subsystem=Physics
    (0x00312dd0, "GameObject::__typeinfo"),  # size=60, subsystem=Game Props
    (0x00312e10, "GameObject::__nw"),  # size=20, subsystem=Game Props
    (0x00312e28, "GameObject::__dl"),  # size=28, subsystem=Game Props
    (0x00312e48, "GameObject::msg_hurt"),  # size=8, subsystem=Game Props
    (0x00312e50, "GameObject::msg_trigger"),  # size=8, subsystem=Game Props
    (0x00312e58, "GameObject::msg_run"),  # size=8, subsystem=Game Props
    (0x00312e60, "GameObject::msg_draw"),  # size=8, subsystem=Game Props
    (0x00312e68, "GameObject::msg_collision"),  # size=8, subsystem=Game Props
    (0x00312e70, "GameObject::msg_route"),  # size=8, subsystem=Game Props
    (0x00312e78, "GameObject::msg_load"),  # size=8, subsystem=Game Props
    (0x00312e80, "GameObject::msg_save"),  # size=8, subsystem=Game Props
    (0x00312e88, "GameObject::msg_collisionWorld"),  # size=36, subsystem=Game Props
    (0x00312eb0, "GameObject::msg_moveCollision"),  # size=8, subsystem=Game Props
    (0x00312eb8, "GameObject::msg_alert"),  # size=36, subsystem=Game Props
    (0x00312ee0, "GameObject::msg_getPokeName"),  # size=8, subsystem=Game Props
    (0x00312ee8, "GameObject::msg_poke"),  # size=8, subsystem=Game Props
    (0x00312ef0, "GameObject::eRandf"),  # size=48, subsystem=Game Props
    (0x00312f20, "GameObject::eRandv"),  # size=208, subsystem=Game Props
    (0x00312ff0, "GameObject::eRandv"),  # size=236, subsystem=Game Props
    (0x003130e0, "GameObject::getModel"),  # size=8, subsystem=Game Props
    (0x003130e8, "ParticleMorphEffect::~destructor"),  # size=100, subsystem=Particles
    (0x00313150, "ParticleMorphEffect::__typeinfo"),  # size=76, subsystem=Particles
    (0x003131b8, "Skill::canCast"),  # size=8, subsystem=Skills
    (0x003131c0, "Skill::cast"),  # size=40, subsystem=Skills
    (0x003131e8, "Skill::piggyBackCast"),  # size=40, subsystem=Skills
    (0x00313210, "Skill::getRankDescription"),  # size=56, subsystem=Skills
    (0x00313248, "Skill::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00313250, "Skill::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00313258, "Skill::getEnergyCost"),  # size=16, subsystem=Skills
    (0x00313268, "Skill::getIcon"),  # size=36, subsystem=Skills
    (0x00313290, "Skill::getRampDamage"),  # size=692, subsystem=Skills
    (0x00313548, "Skill::evaluateRampAtRank"),  # size=156, subsystem=Skills
    (0x003135e8, "Skill::evaluateCreatureRampAtRank"),  # size=156, subsystem=Skills
    (0x00313688, "Skill::evaluateRampAtRank"),  # size=116, subsystem=Skills
    (0x00313700, "Skill::evaluateRampAtRank"),  # size=124, subsystem=Skills
    (0x00313780, "Skill::tweekRank"),  # size=8, subsystem=Skills
    (0x00313788, "Skill::energyCostRamp4"),  # size=96, subsystem=Skills
    (0x003137e8, "SkillDiseaseEffect::__typeinfo"),  # size=76, subsystem=Skills
    (0x00313838, "SkillDiseaseWeapons::__typeinfo"),  # size=76, subsystem=Skills
    (0x00313888, "SkillPoisonWeapons::__typeinfo"),  # size=76, subsystem=Skills
    (0x003138d8, "SkillHateBeam::__typeinfo"),  # size=76, subsystem=Skills
    (0x00313928, "SkillBallOfHate::__typeinfo"),  # size=76, subsystem=Skills
    (0x00313978, "SkillHateEffect::__typeinfo"),  # size=76, subsystem=Skills
    (0x003139c8, "Skill::__typeinfo"),  # size=60, subsystem=Skills
    (0x00313a08, "Skill::initRamps"),  # size=76, subsystem=Skills
    (0x00313a58, "SkillBlunt::__typeinfo"),  # size=104, subsystem=Skills
    (0x00313ac0, "SkillBlunt::getRankDescription"),  # size=120, subsystem=Skills
    (0x00313b38, "SkillBlunt::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00313b40, "SkillBlunt::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00313b48, "SkillSlashing::__typeinfo"),  # size=104, subsystem=Skills
    (0x00313bb0, "SkillSlashing::getRankDescription"),  # size=120, subsystem=Skills
    (0x00313c28, "SkillSlashing::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00313c30, "SkillSlashing::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00313c38, "SkillResistPoison::__typeinfo"),  # size=104, subsystem=Skills
    (0x00313ca0, "SkillResistPoison::getRankDescription"),  # size=112, subsystem=Skills
    (0x00313d10, "SkillResistPoison::getSkillPointCost"),  # size=8, subsystem=Skills
    (0x00313d18, "SkillResistPoison::getLevelRequirement"),  # size=8, subsystem=Skills
    (0x00313d20, "FrostStormIceShard::~destructor"),  # size=100, subsystem=Game Entities
    (0x00313d88, "FrostStormIceShard::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00313dd8, "RainOfFireSpell::~destructor"),  # size=124, subsystem=C++ Runtime
    (0x00313e58, "RainOfFireSpell::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00313ea8, "BoltGoRound::~destructor"),  # size=100, subsystem=Game Entities
    (0x00313f10, "BoltGoRound::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00313f60, "CloudGiant::~destructor"),  # size=100, subsystem=Game Entities
    (0x00313fc8, "CloudGiant::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00314018, "Demon::~destructor"),  # size=100, subsystem=Game Entities
    (0x00314080, "Demon::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003140d0, "LavaBomb::~destructor"),  # size=100, subsystem=Renderer
    (0x00314138, "LavaBomb::__typeinfo"),  # size=80, subsystem=Renderer
    (0x00314188, "LavaBomb::constructor"),  # size=236, subsystem=Renderer
    (0x00314278, "Soul::~destructor"),  # size=116, subsystem=Game Entities
    (0x003142f0, "Soul::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00314340, "Ulthork::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x003143a8, "Ulthork::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x003143f8, "Nightmare::~destructor"),  # size=108, subsystem=Game Entities
    (0x00314468, "Nightmare::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003144b8, "Mermaid::~destructor"),  # size=100, subsystem=Game Entities
    (0x00314520, "Mermaid::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00314570, "SeaMonster::~destructor"),  # size=100, subsystem=Game Entities
    (0x003145d8, "SeaMonster::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00314628, "Spell::draw"),  # size=8, subsystem=Spells
    (0x00314630, "Spell::canQueue"),  # size=8, subsystem=Spells
    (0x00314638, "SpellHateEffect::~destructor"),  # size=124, subsystem=Spells
    (0x003146b8, "SpellHateEffect::__typeinfo"),  # size=76, subsystem=Spells
    (0x00314708, "Innoruuk::~destructor"),  # size=124, subsystem=Game Entities
    (0x00314788, "Innoruuk::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003147d8, "HateSoul::~destructor"),  # size=132, subsystem=Game Entities
    (0x00314860, "HateSoul::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003148b0, "HateBeam::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00314900, "HateProjectile::__typeinfo"),  # size=76, subsystem=Projectiles
    (0x00314950, "Spell::__typeinfo"),  # size=60, subsystem=Spells
    (0x00314990, "Spell::~destructor"),  # size=100, subsystem=Spells
    (0x003149f8, "Spell::run"),  # size=36, subsystem=Spells
    (0x00314a20, "GnomeNavigator::~destructor"),  # size=100, subsystem=Game Entities
    (0x00314a88, "GnomeNavigator::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00314ad8, "PoisonProjectile::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x00314b60, "PoisonProjectile::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00314bb0, "Trap::~destructor"),  # size=100, subsystem=Game Props
    (0x00314c18, "Trap::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00314c68, "TestLocation::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00314cd0, "TestLocation::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00314d20, "AutoObject::~destructor"),  # size=116, subsystem=Game Entities
    (0x00314d98, "AutoObject::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00314de8, "AutoObject::getModel"),  # size=8, subsystem=Game Entities
    (0x00314df0, "AutoChest::~destructor"),  # size=116, subsystem=Game Props
    (0x00314e68, "AutoChest::__typeinfo"),  # size=132, subsystem=Game Props
    (0x00314ef0, "AutoProp::__typeinfo"),  # size=132, subsystem=Game Props
    (0x00314f78, "AutoContainer::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00315000, "AddParticle::__typeinfo"),  # size=76, subsystem=Particles
    (0x00315050, "AddParticle::~destructor"),  # size=116, subsystem=Particles
    (0x003150c8, "AutoChestLP::__typeinfo"),  # size=176, subsystem=Game Props
    (0x00315178, "AutoPropLP::__typeinfo"),  # size=176, subsystem=Game Props
    (0x00315228, "AutoContainerLP::__typeinfo"),  # size=176, subsystem=C++ Runtime
    (0x003152d8, "AntTrap::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00315340, "AntTrap::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315390, "HateInto::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x00315408, "HateInto::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315458, "HateGate::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x003154d0, "HateGate::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315520, "GothTrap::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00315588, "GothTrap::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x003155d8, "HateHole::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00315640, "HateHole::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315690, "HateBridge::~destructor"),  # size=100, subsystem=Game Entities
    (0x003156f8, "HateBridge::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00315748, "HackDoor::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x003157b0, "HackDoor::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315800, "EggSack::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00315868, "EggSack::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x003158b8, "SnowballSpell::~destructor"),  # size=108, subsystem=Game Entities
    (0x00315928, "SnowballSpell::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00315978, "Rondo::~destructor"),  # size=108, subsystem=Game Entities
    (0x003159e8, "Rondo::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00315a38, "Natasla::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00315aa0, "Natasla::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315af0, "Minion::~destructor"),  # size=116, subsystem=C++ Runtime
    (0x00315b68, "Minion::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00315bb8, "Arenabeast::~destructor"),  # size=100, subsystem=Game Entities
    (0x00315c20, "Arenabeast::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00315c70, "Mummy::~destructor"),  # size=100, subsystem=Game Entities
    (0x00315cd8, "Mummy::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00315d28, "DustDevil::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00315d78, "SpawnMummy::~destructor"),  # size=140, subsystem=C++ Runtime
    (0x00315e08, "SpawnMummy::__typeinfo"),  # size=132, subsystem=C++ Runtime
    (0x00315e90, "MummySnake::~destructor"),  # size=116, subsystem=Game Entities
    (0x00315f08, "MummySnake::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00315f58, "MummyKing::~destructor"),  # size=228, subsystem=Game Entities
    (0x00316040, "MummyKing::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00316090, "UndeadKnight::~destructor"),  # size=116, subsystem=Game Entities
    (0x00316108, "UndeadKnight::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00316158, "UndeadKnightClone::~destructor"),  # size=116, subsystem=Game Entities
    (0x003161d0, "UndeadKnightClone::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x00316220, "VampireLord::~destructor"),  # size=108, subsystem=Game Entities
    (0x00316290, "VampireLord::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003162e0, "Skeleton::~destructor"),  # size=116, subsystem=Game Entities
    (0x00316358, "Skeleton::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003163a8, "Skelight::~destructor"),  # size=100, subsystem=Renderer
    (0x00316410, "Skelight::__typeinfo"),  # size=80, subsystem=Renderer
    (0x00316490, "Wheel::~destructor"),  # size=116, subsystem=Game Props
    (0x00316508, "Wheel::__typeinfo"),  # size=76, subsystem=Game Props
    (0x00316558, "Vehicle::__typeinfo"),  # size=76, subsystem=Physics
    (0x003165a8, "Vehicle::eventActivate"),  # size=8, subsystem=Physics
    (0x003165b0, "Vehicle::eventDeActivate"),  # size=8, subsystem=Physics
    (0x003165b8, "Vehicle::eventGasOn"),  # size=8, subsystem=Physics
    (0x003165c0, "Vehicle::eventGasOff"),  # size=8, subsystem=Physics
    (0x003165c8, "Vehicle::eventCurRPM"),  # size=8, subsystem=Physics
    (0x003165d0, "Vehicle::eventCollisionGround"),  # size=8, subsystem=Physics
    (0x003165d8, "Vehicle::eventCollisionWall"),  # size=8, subsystem=Physics
    (0x003165e0, "Vehicle::eventSteeringChange"),  # size=8, subsystem=Physics
    (0x003165e8, "Vehicle::doMyUniqueForces"),  # size=8, subsystem=Physics
    (0x003165f0, "Cthulu::~destructor"),  # size=100, subsystem=Renderer
    (0x00316658, "Cthulu::__typeinfo"),  # size=80, subsystem=Renderer
    (0x003166a8, "LavaTractor::~destructor"),  # size=100, subsystem=Physics
    (0x00316710, "LavaTractor::__typeinfo"),  # size=80, subsystem=Physics
    (0x00316760, "LavaVehicle::~destructor"),  # size=100, subsystem=Physics
    (0x003167c8, "LavaVehicle::__typeinfo"),  # size=80, subsystem=Physics
    (0x00316818, "FemaleDarkElf::~destructor"),  # size=100, subsystem=Game Entities
    (0x00316880, "FemaleDarkElf::__typeinfo"),  # size=80, subsystem=Game Entities
    (0x003168d0, "MaleDarkElf::~destructor"),  # size=100, subsystem=Renderer
    (0x00316938, "MaleDarkElf::__typeinfo"),  # size=80, subsystem=Renderer
    (0x00316988, "FireBomblet::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x003169d8, "Catapult::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00316a28, "SkillShock::__typeinfo"),  # size=76, subsystem=Skills
    (0x00316a78, "SkillShock::getIcon"),  # size=36, subsystem=Skills
    (0x00316aa0, "SkillGroundPound::__typeinfo"),  # size=76, subsystem=Skills
    (0x00316af0, "SkillGroundPound::getIcon"),  # size=36, subsystem=Skills
    (0x00316b18, "SpellCharge::__typeinfo"),  # size=112, subsystem=Spells
    (0x00316b88, "SkillCharge::__typeinfo"),  # size=76, subsystem=Skills
    (0x00316bd8, "SkillCharge::getIcon"),  # size=36, subsystem=Skills
    (0x00316c00, "SkillDiseaseBolt::__typeinfo"),  # size=76, subsystem=Skills
    (0x00316c50, "SkillDiseaseBolt::getIcon"),  # size=36, subsystem=Skills
    (0x00316c78, "DiseaseBolt::~destructor"),  # size=140, subsystem=Projectiles
    (0x00316d08, "DiseaseBolt::__typeinfo"),  # size=80, subsystem=Projectiles
    (0x00316d58, "SpellDiseaseTrail::~destructor"),  # size=116, subsystem=Spells
    (0x00316dd0, "SpellDiseaseTrail::__typeinfo"),  # size=112, subsystem=Spells
    (0x00316e40, "SkillDiseaseTrail::__typeinfo"),  # size=76, subsystem=Skills
    (0x00316e90, "SkillDiseaseTrail::getIcon"),  # size=36, subsystem=Skills
    (0x00316eb8, "DiseaseTrail::~destructor"),  # size=108, subsystem=Game Entities
    (0x00316f28, "DiseaseTrail::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00316f78, "SpellDiseaseShield::~destructor"),  # size=100, subsystem=Spells
    (0x00316fe0, "SpellDiseaseShield::__typeinfo"),  # size=112, subsystem=Spells
    (0x00317050, "SkillDiseaseShield::__typeinfo"),  # size=76, subsystem=Skills
    (0x003170a0, "SkillDiseaseShield::getIcon"),  # size=36, subsystem=Skills
    (0x003170c8, "DiseaseCorpse::~destructor"),  # size=108, subsystem=Game Entities
    (0x00317138, "DiseaseCorpse::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00317188, "DiseaseCloud::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x003171f8, "DiseaseCloud::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00317248, "SkillDarkness::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317298, "SkillDarkness::getIcon"),  # size=36, subsystem=Skills
    (0x003172c0, "DarknessProjectile::~destructor"),  # size=132, subsystem=Other
    (0x00317348, "DarknessProjectile::__typeinfo"),  # size=76, subsystem=Other
    (0x00317398, "SpellConvertEnemy::~destructor"),  # size=116, subsystem=Spells
    (0x00317410, "SpellConvertEnemy::__typeinfo"),  # size=112, subsystem=Spells
    (0x00317480, "SkillConvertEnemy::__typeinfo"),  # size=76, subsystem=Skills
    (0x003174d0, "SkillConvertEnemy::getIcon"),  # size=36, subsystem=Skills
    (0x003174f8, "SpellConvertUndead::~destructor"),  # size=116, subsystem=Spells
    (0x00317570, "SpellConvertUndead::__typeinfo"),  # size=112, subsystem=Spells
    (0x003175e0, "SkillConvertUndead::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317630, "SkillConvertUndead::getIcon"),  # size=36, subsystem=Skills
    (0x00317658, "SkillCyclone::__typeinfo"),  # size=76, subsystem=Skills
    (0x003176a8, "SkillCyclone::getIcon"),  # size=36, subsystem=Skills
    (0x003176d0, "SpellCyclone::~destructor"),  # size=132, subsystem=Spells
    (0x00317758, "SpellCyclone::__typeinfo"),  # size=112, subsystem=Spells
    (0x003177c8, "SkillHarmTouch::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317818, "SkillHarmTouch::getIcon"),  # size=36, subsystem=Skills
    (0x00317840, "SpellHarmTouch::~destructor"),  # size=100, subsystem=Spells
    (0x003178a8, "SpellHarmTouch::__typeinfo"),  # size=76, subsystem=Spells
    (0x003178f8, "SkillFireStorm::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317948, "SkillFireStorm::getIcon"),  # size=36, subsystem=Skills
    (0x00317970, "FireStorm::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x003179c0, "FireStormFlare::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x00317a28, "FireStormFlare::__typeinfo"),  # size=76, subsystem=C++ Runtime
    (0x00317a78, "SpellDiseaseEffect::~destructor"),  # size=116, subsystem=Spells
    (0x00317af0, "SpellDiseaseEffect::__typeinfo"),  # size=112, subsystem=Spells
    (0x00317b60, "SkillFireArrow::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317bb0, "SkillFireArrow::getIcon"),  # size=36, subsystem=Skills
    (0x00317bd8, "FireArrowProjectile::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x00317c60, "FireArrowProjectile::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00317cb0, "SkillColdArrow::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317d00, "SkillColdArrow::getIcon"),  # size=36, subsystem=Skills
    (0x00317d28, "ColdArrowProjectile::~destructor"),  # size=132, subsystem=Projectiles
    (0x00317db0, "ColdArrowProjectile::__typeinfo"),  # size=80, subsystem=Projectiles
    (0x00317e00, "SkillPoisonArrow::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317e50, "SkillPoisonArrow::getIcon"),  # size=36, subsystem=Skills
    (0x00317e78, "PoisonArrowProjectile::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x00317f00, "PoisonArrowProjectile::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00317f50, "SkillMultiFire::__typeinfo"),  # size=76, subsystem=Skills
    (0x00317fa0, "SkillMultiFire::getIcon"),  # size=36, subsystem=Skills
    (0x00317fc8, "MultiFireProjectile::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x00318038, "MultiFireProjectile::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00318088, "SkillExplodeArrow::__typeinfo"),  # size=76, subsystem=Skills
    (0x003180d8, "SkillExplodeArrow::getIcon"),  # size=36, subsystem=Skills
    (0x00318100, "ExplodeArrowProjectile::~destructor"),  # size=108, subsystem=C++ Runtime
    (0x00318170, "ExplodeArrowProjectile::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x003181c0, "SkillArchery::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318210, "SpellFireFlares::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318280, "SkillFireFlares::__typeinfo"),  # size=76, subsystem=Skills
    (0x003182d0, "SkillFireFlares::getIcon"),  # size=36, subsystem=Skills
    (0x003182f8, "FireFlare::~destructor"),  # size=100, subsystem=Renderer
    (0x00318360, "FireFlare::__typeinfo"),  # size=76, subsystem=Renderer
    (0x003183b0, "SkillRiposte::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318400, "SkillBash::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318450, "SkillBash::getIcon"),  # size=36, subsystem=Skills
    (0x00318478, "SpellBash::~destructor"),  # size=100, subsystem=Spells
    (0x003184e0, "SpellBash::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318550, "SpellBlessed::__typeinfo"),  # size=112, subsystem=Spells
    (0x003185c0, "SkillBlessed::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318610, "SkillBlessed::getIcon"),  # size=36, subsystem=Skills
    (0x00318638, "SkillMinorHealing::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318688, "SkillMinorHealing::getIcon"),  # size=36, subsystem=Skills
    (0x003186b0, "SpellMinorHealing::~destructor"),  # size=100, subsystem=Spells
    (0x00318718, "SpellMinorHealing::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318788, "SkillAncestralCall::__typeinfo"),  # size=76, subsystem=Skills
    (0x003187d8, "SkillAncestralCall::getIcon"),  # size=36, subsystem=Skills
    (0x00318800, "SpellAncestralCall::~destructor"),  # size=100, subsystem=Spells
    (0x00318868, "SpellAncestralCall::__typeinfo"),  # size=112, subsystem=Spells
    (0x003188d8, "SpellSummonSkeleton::~destructor"),  # size=116, subsystem=Spells
    (0x00318950, "SpellSummonSkeleton::__typeinfo"),  # size=112, subsystem=Spells
    (0x003189c0, "SkillSummonSkeleton::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318a10, "SkillSummonSkeleton::getIcon"),  # size=36, subsystem=Skills
    (0x00318a38, "SpellLightningWeapons::~destructor"),  # size=100, subsystem=Particles
    (0x00318aa0, "SpellLightningWeapons::__typeinfo"),  # size=112, subsystem=Particles
    (0x00318b10, "SkillLightningWeapons::__typeinfo"),  # size=76, subsystem=Particles
    (0x00318b60, "SkillLightningWeapons::getIcon"),  # size=36, subsystem=Particles
    (0x00318b88, "SpellFireWeapons::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318bf8, "SkillFireWeapons::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318c48, "SkillFireWeapons::getIcon"),  # size=36, subsystem=Skills
    (0x00318c70, "SpellColdWeapons::~destructor"),  # size=100, subsystem=Spells
    (0x00318cd8, "SpellColdWeapons::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318d48, "SkillColdWeapons::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318d98, "SkillColdWeapons::getIcon"),  # size=36, subsystem=Skills
    (0x00318dc0, "SkillRoot::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318e10, "SkillRoot::getIcon"),  # size=36, subsystem=Skills
    (0x00318e38, "SpellRoot::__typeinfo"),  # size=76, subsystem=Spells
    (0x00318e88, "SkillCriticalHit::__typeinfo"),  # size=76, subsystem=Skills
    (0x00318ed8, "SkillCriticalHit::getIcon"),  # size=36, subsystem=Skills
    (0x00318f00, "SpellCriticalHit::~destructor"),  # size=124, subsystem=Spells
    (0x00318f80, "SpellCriticalHit::__typeinfo"),  # size=112, subsystem=Spells
    (0x00318ff0, "SkillHolyShield::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319040, "SkillHolyShield::getIcon"),  # size=36, subsystem=Skills
    (0x00319068, "SpellHolyShield::~destructor"),  # size=100, subsystem=Spells
    (0x003190d0, "SpellHolyShield::__typeinfo"),  # size=112, subsystem=Spells
    (0x00319140, "SkillDodge::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319190, "SkillHealing::__typeinfo"),  # size=76, subsystem=Skills
    (0x003191e0, "SkillHealing::getIcon"),  # size=36, subsystem=Skills
    (0x00319208, "SpellHealing::~destructor"),  # size=100, subsystem=Spells
    (0x00319270, "SpellHealing::__typeinfo"),  # size=112, subsystem=Spells
    (0x003192e0, "SkillConeOfFrost::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319330, "SkillConeOfFrost::getIcon"),  # size=36, subsystem=Skills
    (0x00319358, "SpellConeOfFrost::__typeinfo"),  # size=112, subsystem=Spells
    (0x003193c8, "SpellUndeadShield::__typeinfo"),  # size=112, subsystem=Spells
    (0x00319438, "SpellSecondaryUndeadShield::__typeinfo"),  # size=112, subsystem=Spells
    (0x003194a8, "SkillUndeadShield::__typeinfo"),  # size=76, subsystem=Skills
    (0x003194f8, "SkillUndeadShield::getIcon"),  # size=36, subsystem=Skills
    (0x00319520, "SkillHolyStrike::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319570, "SkillHolyStrike::getIcon"),  # size=36, subsystem=Skills
    (0x00319598, "HolyStrike::~destructor"),  # size=140, subsystem=Renderer
    (0x00319628, "HolyStrike::__typeinfo"),  # size=80, subsystem=Renderer
    (0x00319678, "SkillShockOfFire::__typeinfo"),  # size=76, subsystem=Skills
    (0x003196c8, "SkillShockOfFire::getIcon"),  # size=36, subsystem=Skills
    (0x003196f0, "SkillFrostStorm::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319740, "SkillFrostStorm::getIcon"),  # size=36, subsystem=Skills
    (0x00319768, "SpellHammerOfWrath::~destructor"),  # size=116, subsystem=Spells
    (0x003197e0, "SpellHammerOfWrath::__typeinfo"),  # size=112, subsystem=Spells
    (0x00319850, "SkillHammerOfWrath::__typeinfo"),  # size=76, subsystem=Skills
    (0x003198a0, "SkillHammerOfWrath::getIcon"),  # size=36, subsystem=Skills
    (0x003198c8, "HammerOfWrath::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00319918, "SpellConeOfFire::__typeinfo"),  # size=112, subsystem=Spells
    (0x00319988, "SkillConeOfFire::__typeinfo"),  # size=76, subsystem=Skills
    (0x003199d8, "SkillConeOfFire::getIcon"),  # size=36, subsystem=Skills
    (0x00319a00, "SkillRegeneration::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319a50, "SpellWizardBeam::__typeinfo"),  # size=112, subsystem=Spells
    (0x00319ac0, "SkillWizardBeam::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319b10, "SkillWizardBeam::getIcon"),  # size=36, subsystem=Skills
    (0x00319b38, "SpellBlindingLight::~destructor"),  # size=100, subsystem=Spells
    (0x00319ba0, "SpellBlindingLight::__typeinfo"),  # size=76, subsystem=Spells
    (0x00319bf0, "SkillBlindingLight::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319c40, "SkillBlindingLight::getIcon"),  # size=36, subsystem=Skills
    (0x00319c68, "BlindingLightEffect::~destructor"),  # size=100, subsystem=Game Entities
    (0x00319cd0, "BlindingLightEffect::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x00319d20, "SkillRepulseUndead::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319d70, "SkillRepulseUndead::getIcon"),  # size=36, subsystem=Skills
    (0x00319d98, "SkillDismissUndead::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319de8, "SkillDismissUndead::getIcon"),  # size=36, subsystem=Skills
    (0x00319e10, "SkillShockOfFrost::__typeinfo"),  # size=76, subsystem=Skills
    (0x00319e60, "SkillShockOfFrost::getIcon"),  # size=36, subsystem=Skills
    (0x00319e88, "FrostShard::~destructor"),  # size=132, subsystem=C++ Runtime
    (0x00319f10, "FrostShard::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x00319f60, "ShockOfFrost::__typeinfo"),  # size=80, subsystem=Physics
    (0x00319fb0, "SkillLifeTap::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a000, "SkillLifeTap::getIcon"),  # size=36, subsystem=Skills
    (0x0031a028, "SkillPoisonRain::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a078, "PoisonRain::~destructor"),  # size=108, subsystem=Game Entities
    (0x0031a0e8, "PoisonRain::__typeinfo"),  # size=76, subsystem=Game Entities
    (0x0031a138, "Boat::~destructor"),  # size=100, subsystem=Game Props
    (0x0031a1a0, "Boat::__typeinfo"),  # size=80, subsystem=Game Props
    (0x0031a1f0, "SkulBoat::~destructor"),  # size=100, subsystem=Game Props
    (0x0031a258, "SkulBoat::__typeinfo"),  # size=80, subsystem=Game Props
    (0x0031a448, "SkillClericRoot::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a498, "SkillClericRoot::getIcon"),  # size=36, subsystem=Skills
    (0x0031a4c0, "SpellClericRoot::__typeinfo"),  # size=76, subsystem=Spells
    (0x0031a510, "SkillEntangle::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a560, "SkillEntangle::getIcon"),  # size=36, subsystem=Skills
    (0x0031a588, "SpellEntangle::__typeinfo"),  # size=76, subsystem=Spells
    (0x0031a5d8, "SkillRangerCriticalHit::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a628, "SkillRangerCriticalHit::getIcon"),  # size=36, subsystem=Skills
    (0x0031a650, "SpellRangerCriticalHit::~destructor"),  # size=124, subsystem=Spells
    (0x0031a6d0, "SpellRangerCriticalHit::__typeinfo"),  # size=112, subsystem=Spells
    (0x0031a740, "SkillShieldBash::__typeinfo"),  # size=76, subsystem=Skills
    (0x0031a790, "SkillShieldBash::getIcon"),  # size=36, subsystem=Skills
    (0x0031a7b8, "SpellShieldBash::~destructor"),  # size=100, subsystem=Spells
    (0x0031a820, "SpellShieldBash::__typeinfo"),  # size=112, subsystem=Spells
    (0x0031a890, "SpellPlanarSteelEffect::__typeinfo"),  # size=112, subsystem=Spells
    (0x0031a900, "SpellHornOmenEffect::__typeinfo"),  # size=76, subsystem=Spells
    (0x0031a950, "type_info::__typeinfo"),  # size=64, subsystem=C++ Runtime
    (0x0031a990, "type_info::constructor"),  # size=20, subsystem=C++ Runtime
    (0x0031a9d0, "bad_cast::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031aa20, "bad_cast::constructor"),  # size=16, subsystem=C++ Runtime
    (0x0031aa30, "bad_cast::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0031aa68, "bad_typeid::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031aab8, "bad_typeid::constructor"),  # size=16, subsystem=C++ Runtime
    (0x0031aac8, "bad_typeid::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0031ab00, "__user_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031ab68, "__user_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031abb8, "__user_type_info::constructor"),  # size=20, subsystem=C++ Runtime
    (0x0031abd0, "__user_type_info::contained_p"),  # size=12, subsystem=C++ Runtime
    (0x0031abe0, "__user_type_info::contained_public_p"),  # size=12, subsystem=C++ Runtime
    (0x0031abf0, "__user_type_info::contained_nonpublic_p"),  # size=16, subsystem=C++ Runtime
    (0x0031ac00, "__user_type_info::contained_nonvirtual_p"),  # size=16, subsystem=C++ Runtime
    (0x0031ac10, "__user_type_info::contained_virtual_p"),  # size=16, subsystem=C++ Runtime
    (0x0031ac88, "__si_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031acf0, "__si_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031ad40, "__si_type_info::constructor"),  # size=24, subsystem=C++ Runtime
    (0x0031ad58, "__class_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031adc0, "__class_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031ae10, "__class_type_info::constructor"),  # size=28, subsystem=C++ Runtime
    (0x0031ae30, "__pointer_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031ae98, "__pointer_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031aee8, "__attr_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031af50, "__attr_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031afa0, "__builtin_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031b008, "__builtin_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b058, "__func_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031b0c0, "__func_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b110, "__ptmf_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031b178, "__ptmf_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b1c8, "__ptmd_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031b230, "__ptmd_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b280, "__array_type_info::~destructor"),  # size=100, subsystem=C++ Runtime
    (0x0031b2e8, "__array_type_info::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b338, "exception::__typeinfo"),  # size=64, subsystem=C++ Runtime
    (0x0031b378, "exception::constructor"),  # size=16, subsystem=C++ Runtime
    (0x0031b388, "exception::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0031b3c0, "bad_exception::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x0031b410, "bad_exception::constructor"),  # size=16, subsystem=C++ Runtime
    (0x0031b420, "bad_exception::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0031b458, "bad_alloc::~destructor"),  # size=52, subsystem=C++ Runtime
    (0x0031b490, "bad_alloc::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x010001c0, "VISpellEventList::Destroy"),  # size=256, subsystem=Engine (VISpellEventList)
    (0x010002c0, "VISpellEffect::GetLastImpactTime"),  # size=996, subsystem=Engine (VISpellEffect)
    (0x010006a8, "VISpellEventList::constructor"),  # size=16, subsystem=Engine (VISpellEventList)
    (0x010006b8, "VISpellEventList::~destructor"),  # size=84, subsystem=Engine (VISpellEventList)
    (0x01000710, "VISpellEventList::Create"),  # size=100, subsystem=Engine (VISpellEventList)
    (0x01000778, "VISpellEffect::constructor"),  # size=64, subsystem=Engine (VISpellEffect)
    (0x010007b8, "VISpellEffect::~destructor"),  # size=108, subsystem=Engine (VISpellEffect)
    (0x01000828, "VISpellEffect::Create"),  # size=12, subsystem=Engine (VISpellEffect)
    (0x01000838, "VISpellEffect::Destroy"),  # size=80, subsystem=Engine (VISpellEffect)
    (0x01000be0, "Base::put"),  # size=76, subsystem=Networking
    (0x010012d0, "Base::ByteStream::__as"),  # size=260, subsystem=Engine Utilities
    (0x010013d8, "Base::ByteStream::put"),  # size=712, subsystem=Engine Utilities
    (0x01001830, "Base::get"),  # size=140, subsystem=Networking
    (0x01001960, "Base::ByteStream::reAllocate"),  # size=160, subsystem=Engine Utilities
    (0x01001a28, "Base::AutoByteStream::addVariable"),  # size=84, subsystem=Engine Utilities
    (0x01001b38, "Base::AutoByteStream::unpack"),  # size=164, subsystem=Engine Utilities
    (0x01001c28, "BlockAllocator::realloc"),  # size=228, subsystem=Engine Utilities
    (0x01001d10, "BlockAllocator::constructor"),  # size=40, subsystem=Engine Utilities
    (0x01001d38, "BlockAllocator::~destructor"),  # size=160, subsystem=Engine Utilities
    (0x01001dd8, "BlockAllocator::getBlock"),  # size=84, subsystem=Engine Utilities
    (0x01001e30, "BlockAllocator::returnBlock"),  # size=116, subsystem=Engine Utilities
    (0x01001ea8, "VIFile::MemorySegmRead"),  # size=336, subsystem=File I/O
    (0x01001ff8, "VIFile::MemorySegmWrite"),  # size=332, subsystem=File I/O
    (0x01002148, "VIFile::MemoryOpen"),  # size=100, subsystem=File I/O
    (0x010021b0, "VIFile::MemorySeek"),  # size=104, subsystem=File I/O
    (0x01002218, "VIFile::MemoryRead"),  # size=156, subsystem=File I/O
    (0x010022b8, "VIFile::MemoryWrite"),  # size=152, subsystem=File I/O
    (0x01002350, "VIFile::MemorySegmOpen"),  # size=308, subsystem=File I/O
    (0x01002488, "VIFile::MemorySegmSeek"),  # size=128, subsystem=File I/O
    (0x01002508, "VIFile::MemorySegmCalcSegm"),  # size=176, subsystem=File I/O
    (0x010025b8, "VISpellEffectSystem::ReleaseAllSpellEffects"),  # size=204, subsystem=Engine (VISpellEffectSystem)
    (0x01002688, "VISpellEffectSystem::Play"),  # size=528, subsystem=Engine (VISpellEffectSystem)
    (0x01002898, "VISpellEffectSystem::Process"),  # size=360, subsystem=Engine (VISpellEffectSystem)
    (0x01002a00, "VISpellEffectSystem::~destructor"),  # size=116, subsystem=Engine (VISpellEffectSystem)
    (0x01002a78, "VISpellEffectSystem::constructor"),  # size=124, subsystem=Engine (VISpellEffectSystem)
    (0x01002af8, "VISpellEffectSystem::Init"),  # size=200, subsystem=Engine (VISpellEffectSystem)
    (0x01002bc0, "VISpellEffectSystem::Clear"),  # size=136, subsystem=Engine (VISpellEffectSystem)
    (0x01002c48, "VISpellEffectSystem::SetVibrateCallback"),  # size=16, subsystem=Engine (VISpellEffectSystem)
    (0x01002c58, "VISpellEffectSystem::SetCameraEffect"),  # size=8, subsystem=Engine (VISpellEffectSystem)
    (0x01002c60, "VISpellEffectSystem::SetPlayerActor"),  # size=8, subsystem=Engine (VISpellEffectSystem)
    (0x01002c68, "VISpellEffectSystem::CreateSpellEffect"),  # size=168, subsystem=Engine (VISpellEffectSystem)
    (0x01002d10, "VISpellEffectSystem::SpellEffect"),  # size=28, subsystem=Engine (VISpellEffectSystem)
    (0x01002d30, "VISpellEffectSystem::ShareSpellEffect"),  # size=44, subsystem=Engine (VISpellEffectSystem)
    (0x01002d60, "VISpellEffectSystem::ReleaseSpellEffect"),  # size=172, subsystem=Engine (VISpellEffectSystem)
    (0x01002e10, "VISpellEffectSystem::IsPlaying"),  # size=32, subsystem=Engine (VISpellEffectSystem)
    (0x01002e30, "VISpellEffectSystem::SpellEffectDriver"),  # size=40, subsystem=Engine (VISpellEffectSystem)
    (0x01002e58, "VISpellEffectSystem::Stop"),  # size=124, subsystem=Engine (VISpellEffectSystem)
    (0x01002ed8, "VISpellEffectSystem::NotifyActorWasDestroyed"),  # size=112, subsystem=Engine (VISpellEffectSystem)
    (0x01002f48, "VISpellEffectSystem::StopIfThisWasCaster"),  # size=232, subsystem=Engine (VISpellEffectSystem)
    (0x01003030, "VISpellEffectSystem::NewPlayback"),  # size=76, subsystem=Engine (VISpellEffectSystem)
    (0x01003080, "VISpellEffectSystem::DeletePlayback"),  # size=64, subsystem=Engine (VISpellEffectSystem)
    (0x010030c0, "VISpellEffectSystem::Playback"),  # size=72, subsystem=Engine (VISpellEffectSystem)
    (0x01003108, "VISpellEffectSystem::FirstPlayback"),  # size=16, subsystem=Engine (VISpellEffectSystem)
    (0x01003118, "VISpellEffectSystem::NextPlayback"),  # size=16, subsystem=Engine (VISpellEffectSystem)
    (0x01003ab0, "TcpConnection::finishConnect"),  # size=304, subsystem=Networking
    (0x01003be0, "TcpConnection::Send"),  # size=460, subsystem=Networking
    (0x01003db0, "TcpConnection::Release"),  # size=276, subsystem=Networking
    (0x01003ec8, "TcpConnection::processIncoming"),  # size=664, subsystem=Networking
    (0x01004160, "TcpConnection::processOutgoing"),  # size=384, subsystem=Networking
    (0x010042e0, "TcpConnection::translateRecvSocketEror"),  # size=244, subsystem=Networking
    (0x010043d8, "TcpConnection::constructor"),  # size=324, subsystem=Networking
    (0x01004520, "TcpConnection::setOptions"),  # size=8, subsystem=Networking
    (0x01004528, "TcpConnection::~destructor"),  # size=180, subsystem=Networking
    (0x010045e0, "TcpConnection::Disconnect"),  # size=184, subsystem=Networking
    (0x01004698, "TcpConnection::AddRef"),  # size=16, subsystem=Networking
    (0x010046a8, "VIFlatFileDirectory::~destructor"),  # size=288, subsystem=Engine (VIFlatFileDirectory)
    (0x010047c8, "VIFlatFileDirectory::FindFile"),  # size=312, subsystem=Engine (VIFlatFileDirectory)
    (0x01004900, "VIFlatFileDirectory::MakeFile"),  # size=760, subsystem=Engine (VIFlatFileDirectory)
    (0x01004bf8, "VIFlatFileStructure::ParseFileStructureData"),  # size=384, subsystem=Engine (VIFlatFileStructure)
    (0x01004d78, "VIFlatFile::constructor"),  # size=36, subsystem=Engine (VIFlatFile)
    (0x01004da0, "VIFlatFile::~destructor"),  # size=148, subsystem=Engine (VIFlatFile)
    (0x01004e38, "VIFlatFile::Initialize"),  # size=188, subsystem=Engine (VIFlatFile)
    (0x01004ef8, "VIFlatFile::GetFileData"),  # size=8, subsystem=Engine (VIFlatFile)
    (0x01004f00, "VIFlatFile::GetFileLength"),  # size=8, subsystem=Engine (VIFlatFile)
    (0x01004f08, "VIFlatFile::GetFileType"),  # size=8, subsystem=Engine (VIFlatFile)
    (0x01004f10, "VIFlatFile::GetFileName"),  # size=8, subsystem=Engine (VIFlatFile)
    (0x01004f18, "VIFlatFileDirectory::constructor"),  # size=80, subsystem=Engine (VIFlatFileDirectory)
    (0x01004f68, "VIFlatFileDirectory::Initialize"),  # size=84, subsystem=Engine (VIFlatFileDirectory)
    (0x01004fc0, "VIFlatFileDirectory::AddFile"),  # size=40, subsystem=Engine (VIFlatFileDirectory)
    (0x01004fe8, "VIFlatFileStructure::constructor"),  # size=132, subsystem=Engine (VIFlatFileStructure)
    (0x01005070, "VIFlatFileStructure::~destructor"),  # size=84, subsystem=Engine (VIFlatFileStructure)
    (0x010050c8, "VIFlatFileStructure::FindFile"),  # size=60, subsystem=Engine (VIFlatFileStructure)
    (0x01005108, "VISphere::Init"),  # size=176, subsystem=Engine (VISphere)
    (0x010051b8, "VISphere::Init"),  # size=356, subsystem=Engine (VISphere)
    (0x010057c8, "TcpManager::GiveTime"),  # size=872, subsystem=Networking
    (0x01005b30, "TcpManager::EstablishConnection"),  # size=304, subsystem=Networking
    (0x01005c60, "TcpManager::Release"),  # size=188, subsystem=Networking
    (0x01005d98, "TcpManager::constructor"),  # size=184, subsystem=Networking
    (0x01005e50, "TcpManager::~destructor"),  # size=188, subsystem=Networking
    (0x01005f10, "TcpManager::BindAsServer"),  # size=8, subsystem=Networking
    (0x01005f18, "TcpManager::acceptClient"),  # size=8, subsystem=Networking
    (0x01005f20, "TcpManager::SetHandler"),  # size=8, subsystem=Networking
    (0x01005f28, "TcpManager::getMaxFD"),  # size=88, subsystem=Networking
    (0x01005f80, "TcpManager::getConnection"),  # size=64, subsystem=Networking
    (0x01005fc0, "TcpManager::addNewConnection"),  # size=92, subsystem=Networking
    (0x01006020, "TcpManager::removeConnection"),  # size=124, subsystem=Networking
    (0x010060a0, "TcpManager::AddRef"),  # size=16, subsystem=Networking
    (0x010060b0, "VIFloraSprite::Copy"),  # size=296, subsystem=Engine (VIFloraSprite)
    (0x010061d8, "VIFloraSprite::constructor"),  # size=68, subsystem=Engine (VIFloraSprite)
    (0x01006220, "VIFloraSprite::~destructor"),  # size=100, subsystem=Engine (VIFloraSprite)
    (0x01006288, "VIFloraSprite::Raster"),  # size=40, subsystem=Engine (VIFloraSprite)
    (0x010062b0, "VIFloraSprite::Collide"),  # size=8, subsystem=Engine (VIFloraSprite)
    (0x010062b8, "VIFloraSprite::Collide"),  # size=8, subsystem=Engine (VIFloraSprite)
    (0x010062c0, "VIFloraSprite::Pick"),  # size=36, subsystem=Engine (VIFloraSprite)
    (0x010062e8, "VIFloraSprite::Release"),  # size=132, subsystem=Engine (VIFloraSprite)
    (0x01006380, "VIFloraSprite::SetMaterialPal"),  # size=88, subsystem=Engine (VIFloraSprite)
    (0x010063d8, "VIFloraSprite::SetMaterialPalDither"),  # size=132, subsystem=Engine (VIFloraSprite)
    (0x01007018, "VIFlyCamera::Init"),  # size=212, subsystem=Engine (VIFlyCamera)
    (0x010070f0, "VIFlyCamera::Init"),  # size=480, subsystem=Engine (VIFlyCamera)
    (0x010072d0, "VIFlyCamera::Process"),  # size=732, subsystem=Engine (VIFlyCamera)
    (0x010075b0, "VIFlyCamera::UpdateCameraPhysics"),  # size=692, subsystem=Engine (VIFlyCamera)
    (0x01007868, "VIFlyCamera::TurnLeft"),  # size=164, subsystem=Engine (VIFlyCamera)
    (0x01007910, "VIFlyCamera::PitchDown"),  # size=160, subsystem=Engine (VIFlyCamera)
    (0x010079b0, "VIFlyCamera::Forward"),  # size=260, subsystem=Engine (VIFlyCamera)
    (0x01007ab8, "VIFlyCamera::Hover"),  # size=352, subsystem=Engine (VIFlyCamera)
    (0x01007c18, "VIFlyCamera::SetCamera"),  # size=240, subsystem=Engine (VIFlyCamera)
    (0x01007d08, "VIFlyCamera::InitCameraIntermediate"),  # size=356, subsystem=Engine (VIFlyCamera)
    (0x01007e70, "VIFlyCamera::MoveCamera"),  # size=8, subsystem=Engine (VIFlyCamera)
    (0x01007e78, "VIFlyCamera::FreeLook"),  # size=40, subsystem=Engine (VIFlyCamera)
    (0x01007ea0, "VIFlyCamera::ClearCameraForces"),  # size=44, subsystem=Engine (VIFlyCamera)
    (0x01007ed0, "VISprite::constructor"),  # size=128, subsystem=Engine (VISprite)
    (0x01007f50, "VISprite::QueryEmitters"),  # size=408, subsystem=Engine (VISprite)
    (0x010080e8, "VISprite::~destructor"),  # size=52, subsystem=Engine (VISprite)
    (0x01008128, "VISprite::Raster"),  # size=8, subsystem=Engine (VISprite)
    (0x01008130, "VISprite::Collide"),  # size=8, subsystem=Engine (VISprite)
    (0x01008138, "VISprite::Collide"),  # size=8, subsystem=Engine (VISprite)
    (0x01008140, "VISprite::Pick"),  # size=8, subsystem=Engine (VISprite)
    (0x01008148, "VISprite::QueryIntersection"),  # size=8, subsystem=Engine (VISprite)
    (0x01008150, "VISprite::Copy"),  # size=8, subsystem=Engine (VISprite)
    (0x01008158, "VISprite::Release"),  # size=8, subsystem=Engine (VISprite)
    (0x01008160, "Base::BlockAllocator::getBlock"),  # size=232, subsystem=Engine Utilities
    (0x01008328, "Base::BlockAllocator::returnBlock"),  # size=56, subsystem=Engine Utilities
    (0x01011bf8, "VIFont::SjisToJis"),  # size=136, subsystem=Engine (VIFont)
    (0x01011c90, "VIFont::DrawString"),  # size=180, subsystem=Engine (VIFont)
    (0x01011d48, "VIFont::DrawString"),  # size=180, subsystem=Engine (VIFont)
    (0x01011e00, "VIFont::DrawCenteredString"),  # size=196, subsystem=Engine (VIFont)
    (0x01011ec8, "VIFont::DrawCenteredString"),  # size=196, subsystem=Engine (VIFont)
    (0x01011f90, "VIFont::GetHeight"),  # size=124, subsystem=Engine (VIFont)
    (0x01012010, "VIFont::GetStringWidth"),  # size=140, subsystem=Engine (VIFont)
    (0x010120a0, "VIFont::GetStringWidth"),  # size=140, subsystem=Engine (VIFont)
    (0x01012130, "VIFont::constructor"),  # size=28, subsystem=Engine (VIFont)
    (0x01012150, "VIFont::SetTextColor"),  # size=36, subsystem=Engine (VIFont)
    (0x01012178, "VIFont::SetTextColor"),  # size=96, subsystem=Engine (VIFont)
    (0x010121d8, "VIFont::GetCharacterWidth"),  # size=140, subsystem=Engine (VIFont)
    (0x01012268, "VIFont::FontLoaded"),  # size=68, subsystem=Engine (VIFont)
    (0x010122b0, "VIStaticLighting::Init"),  # size=44, subsystem=Engine (VIStaticLighting)
    (0x010122e0, "VIStaticLighting::Clear"),  # size=20, subsystem=Engine (VIStaticLighting)
    (0x010122f8, "VIStaticLighting::ReleaseResources"),  # size=140, subsystem=Engine (VIStaticLighting)
    (0x01012388, "VIStaticLighting::ShareResources"),  # size=124, subsystem=Engine (VIStaticLighting)
    (0x01017098, "VIFrustum::CalcPlanes"),  # size=816, subsystem=Engine (VIFrustum)
    (0x010174b0, "VIFrustum::Init"),  # size=8, subsystem=Engine (VIFrustum)
    (0x010175a0, "VIFrustum::SetPlane"),  # size=48, subsystem=Engine (VIFrustum)
    (0x010175e8, "VIFrustum::SetVertex"),  # size=44, subsystem=Engine (VIFrustum)
    (0x01017618, "VIStation::constructor"),  # size=640, subsystem=Engine (VIStation)
    (0x01017898, "VIStation::~destructor"),  # size=300, subsystem=Engine (VIStation)
    (0x010179c8, "VIStation::Init"),  # size=1260, subsystem=Engine (VIStation)
    (0x01017eb8, "VIStation::Free"),  # size=212, subsystem=Engine (VIStation)
    (0x01017f90, "VIStation::Process"),  # size=1008, subsystem=Engine (VIStation)
    (0x01018380, "VIStation::DoEula"),  # size=108, subsystem=Engine (VIStation)
    (0x010183f0, "VIStation::StopEula"),  # size=52, subsystem=Engine (VIStation)
    (0x01018428, "VIStation::ReceiveEula"),  # size=60, subsystem=Engine (VIStation)
    (0x01018468, "VIStation::EulaComplete"),  # size=188, subsystem=Engine (VIStation)
    (0x01018528, "VIStation::End"),  # size=64, subsystem=Engine (VIStation)
    (0x01018568, "VIStation::RepeatSound"),  # size=176, subsystem=Engine (VIStation)
    (0x01018618, "VIStation::CheckSound"),  # size=32, subsystem=Engine (VIStation)
    (0x01018638, "VIStation::ConsolePrint"),  # size=92, subsystem=Engine (VIStation)
    (0x01018698, "VIStation::ConsolePrint"),  # size=92, subsystem=Engine (VIStation)
    (0x010186f8, "Clock::constructor"),  # size=12, subsystem=Game Props
    (0x01018708, "Clock::getCurTime"),  # size=20, subsystem=Game Props
    (0x01018720, "Clock::getElapsedSinceLastStart"),  # size=76, subsystem=Game Props
    (0x01018770, "Clock::start"),  # size=52, subsystem=Game Props
    (0x010187a8, "Clock::stop"),  # size=104, subsystem=Game Props
    (0x01018810, "Clock::isDone"),  # size=124, subsystem=Game Props
    (0x01018890, "Clock::reset"),  # size=12, subsystem=Game Props
    (0x01018a20, "VIStreamAudioSprite::QueryEmitters"),  # size=728, subsystem=Engine (VIStreamAudioSprite)
    (0x01018cf8, "VIStreamAudioSprite::ClampScale"),  # size=444, subsystem=Engine (VIStreamAudioSprite)
    (0x01018eb8, "VIStreamAudioSprite::constructor"),  # size=72, subsystem=Engine (VIStreamAudioSprite)
    (0x01018f00, "VIStreamAudioSprite::~destructor"),  # size=100, subsystem=Engine (VIStreamAudioSprite)
    (0x01018f68, "VIStreamAudioSprite::Init"),  # size=100, subsystem=Engine (VIStreamAudioSprite)
    (0x01018fd8, "VIStreamAudioSprite::Raster"),  # size=256, subsystem=Engine (VIStreamAudioSprite)
    (0x010190d8, "VIStreamAudioSprite::Collide"),  # size=8, subsystem=Engine (VIStreamAudioSprite)
    (0x010190e0, "VIStreamAudioSprite::Collide"),  # size=8, subsystem=Engine (VIStreamAudioSprite)
    (0x010190e8, "VIStreamAudioSprite::Pick"),  # size=268, subsystem=Engine (VIStreamAudioSprite)
    (0x010191f8, "VIStreamAudioSprite::Copy"),  # size=252, subsystem=Engine (VIStreamAudioSprite)
    (0x010192f8, "VIStreamAudioSprite::Release"),  # size=64, subsystem=Engine (VIStreamAudioSprite)
    (0x01019978, "VIGameOptions::constructor"),  # size=20, subsystem=Engine (VIGameOptions)
    (0x01019990, "VIGameOptions::Load"),  # size=168, subsystem=Engine (VIGameOptions)
    (0x01019a38, "VIGameOptions::Save"),  # size=36, subsystem=Engine (VIGameOptions)
    (0x01019a60, "VIGameOptions::SetDefaults"),  # size=100, subsystem=Engine (VIGameOptions)
    (0x01019ad0, "VIGameOptions::SetUsername"),  # size=48, subsystem=Engine (VIGameOptions)
    (0x01019b08, "VIGameOptions::SetPassword"),  # size=48, subsystem=Engine (VIGameOptions)
    (0x01019b40, "VIGameOptions::SetHomeShardName"),  # size=36, subsystem=Engine (VIGameOptions)
    (0x01019b88, "VIString::__as"),  # size=180, subsystem=String Utils
    (0x01019c40, "VIString::__pl"),  # size=276, subsystem=String Utils
    (0x01019d58, "VIString::__pl"),  # size=276, subsystem=String Utils
    (0x01019e70, "VIString::__pl"),  # size=268, subsystem=String Utils
    (0x01019f80, "VIString::vsnprintf16"),  # size=172, subsystem=String Utils
    (0x0101a030, "VIString::snprintf"),  # size=88, subsystem=String Utils
    (0x0101a088, "VIString::snprintf16"),  # size=88, subsystem=String Utils
    (0x0101a0e0, "VIString::snprintf16"),  # size=88, subsystem=String Utils
    (0x0101a138, "VIString::constructor"),  # size=16, subsystem=String Utils
    (0x0101a148, "VIString::constructor"),  # size=36, subsystem=String Utils
    (0x0101a170, "VIString::constructor"),  # size=36, subsystem=String Utils
    (0x0101a198, "VIString::~destructor"),  # size=84, subsystem=String Utils
    (0x0101a1f0, "VIString::Init"),  # size=56, subsystem=String Utils
    (0x0101a228, "VIString::Init"),  # size=112, subsystem=String Utils
    (0x0101a298, "VIString::Init"),  # size=120, subsystem=String Utils
    (0x0101a310, "VIString::Init"),  # size=104, subsystem=String Utils
    (0x0101a378, "VIString::Clear"),  # size=20, subsystem=String Utils
    (0x0101a390, "VIString::Init"),  # size=176, subsystem=String Utils
    (0x0101a480, "VIString::Replace"),  # size=76, subsystem=String Utils
    (0x0101a4d0, "VIString::Concat"),  # size=144, subsystem=String Utils
    (0x0101a560, "VIString::Concat"),  # size=148, subsystem=String Utils
    (0x0101a5f8, "VIString::Concat"),  # size=132, subsystem=String Utils
    (0x0101a680, "VIString::Allocate"),  # size=140, subsystem=String Utils
    (0x0101a710, "VIString::Deallocate"),  # size=68, subsystem=String Utils
    (0x0101a758, "VIString::vsnprintf"),  # size=28, subsystem=String Utils
    (0x0101a7e0, "VIString::vsnprintf16"),  # size=28, subsystem=String Utils
    (0x0101a800, "VIString::strlwr"),  # size=28, subsystem=String Utils
    (0x0101a820, "VIString::strupr"),  # size=28, subsystem=String Utils
    (0x0101a840, "VIString::strlwr16"),  # size=72, subsystem=String Utils
    (0x0101a888, "VIString::strupr16"),  # size=72, subsystem=String Utils
    (0x0101a8d0, "VIString::strcasecmp"),  # size=20, subsystem=String Utils
    (0x0101a8e8, "VIString::strcasecmp16"),  # size=148, subsystem=String Utils
    (0x0101a980, "VIString::strncasecmp"),  # size=20, subsystem=String Utils
    (0x0101a998, "VIString::strlen16"),  # size=52, subsystem=String Utils
    (0x0101a9d0, "VIString::strdup16"),  # size=148, subsystem=String Utils
    (0x0101aa68, "VIString::strcpy8"),  # size=96, subsystem=String Utils
    (0x0101aac8, "VIString::strcpy16"),  # size=96, subsystem=String Utils
    (0x0101ab28, "VIString::strncpy16"),  # size=112, subsystem=String Utils
    (0x0101ab98, "VIString::char16to8"),  # size=124, subsystem=String Utils
    (0x0101ac18, "VIString::char8to16"),  # size=44, subsystem=String Utils
    (0x0101ac48, "VIString::str16to8"),  # size=224, subsystem=String Utils
    (0x0101ad28, "VIString::str8to16"),  # size=144, subsystem=String Utils
    (0x0101adb8, "VIString::strcat16"),  # size=160, subsystem=String Utils
    (0x0101ae58, "VIString::strcat16"),  # size=176, subsystem=String Utils
    (0x0101af08, "VIString::strcmp16"),  # size=60, subsystem=String Utils
    (0x0101af48, "VIString::strstr16"),  # size=140, subsystem=String Utils
    (0x0101b498, "VIStringTable::LoadFromMemCard"),  # size=340, subsystem=Engine (VIStringTable)
    (0x0101b5f0, "VIStringTable::FixupTextBuffer"),  # size=472, subsystem=Engine (VIStringTable)
    (0x0101b7c8, "VIStringTable::LoadRawFile"),  # size=340, subsystem=Engine (VIStringTable)
    (0x0101b920, "VIStringTable::ProcessRawFile"),  # size=600, subsystem=Engine (VIStringTable)
    (0x0101bb78, "VIStringTable::constructor"),  # size=20, subsystem=Engine (VIStringTable)
    (0x0101bb90, "VIStringTable::~destructor"),  # size=84, subsystem=Engine (VIStringTable)
    (0x0101bbe8, "VIStringTable::Unload"),  # size=88, subsystem=Engine (VIStringTable)
    (0x0101bc40, "VIStringTable::GetString"),  # size=88, subsystem=Engine (VIStringTable)
    (0x0101bc98, "VIStringTable::LoadFromMemory"),  # size=224, subsystem=Engine (VIStringTable)
    (0x0101bd78, "VIStringTable::Load"),  # size=192, subsystem=Engine (VIStringTable)
    (0x0101be38, "Base::CConfig::LoadFile"),  # size=400, subsystem=Engine Utilities
    (0x0101bfc8, "Base::CConfig::GetLong"),  # size=476, subsystem=Engine Utilities
    (0x0101c1a8, "Base::CConfig::GetString"),  # size=436, subsystem=Engine Utilities
    (0x0101c360, "Base::CConfig::UnloadFile"),  # size=56, subsystem=Engine Utilities
    (0x0101c398, "Base::CConfig::FindKey"),  # size=176, subsystem=Engine Utilities
    (0x0101cb18, "VIGroupSprite::Raster"),  # size=536, subsystem=Engine (VIGroupSprite)
    (0x0101cd30, "VIGroupSprite::Collide"),  # size=620, subsystem=Engine (VIGroupSprite)
    (0x0101cfa0, "VIGroupSprite::Collide"),  # size=620, subsystem=Engine (VIGroupSprite)
    (0x0101d210, "VIGroupSprite::Pick"),  # size=620, subsystem=Engine (VIGroupSprite)
    (0x0101d480, "VIGroupSprite::QueryEmitters"),  # size=468, subsystem=Engine (VIGroupSprite)
    (0x0101d658, "VIGroupSprite::QueryIntersection"),  # size=468, subsystem=Engine (VIGroupSprite)
    (0x0101d830, "VIGroupSprite::Copy"),  # size=644, subsystem=Engine (VIGroupSprite)
    (0x0101dab8, "VIGroupSprite::constructor"),  # size=116, subsystem=Engine (VIGroupSprite)
    (0x0101db30, "VIGroupSprite::~destructor"),  # size=100, subsystem=Engine (VIGroupSprite)
    (0x0101dc40, "VIGroupSprite::CalcMemberTransform"),  # size=60, subsystem=Engine (VIGroupSprite)
    (0x0101dc80, "VIGroupSprite::Release"),  # size=160, subsystem=Engine (VIGroupSprite)
    (0x0101dd20, "VITCPSocket2::Open"),  # size=364, subsystem=Engine (VITCPSocket2)
    (0x0101de90, "VITCPSocket2::constructor"),  # size=152, subsystem=Engine (VITCPSocket2)
    (0x0101df28, "VITCPSocket2::constructor"),  # size=184, subsystem=Engine (VITCPSocket2)
    (0x0101dfe0, "VITCPSocket2::constructor"),  # size=84, subsystem=Engine (VITCPSocket2)
    (0x0101e038, "VITCPSocket2::~destructor"),  # size=148, subsystem=Engine (VITCPSocket2)
    (0x0101e0d0, "VITCPSocket2::SetServer"),  # size=88, subsystem=Engine (VITCPSocket2)
    (0x0101e128, "VITCPSocket2::SetPort"),  # size=8, subsystem=Engine (VITCPSocket2)
    (0x0101e130, "VITCPSocket2::CheckPendingConnection"),  # size=100, subsystem=Engine (VITCPSocket2)
    (0x0101e198, "VITCPSocket2::CanWrite"),  # size=16, subsystem=Engine (VITCPSocket2)
    (0x0101e1a8, "VITCPSocket2::CanRead"),  # size=16, subsystem=Engine (VITCPSocket2)
    (0x0101e1b8, "VITCPSocket2::Send"),  # size=172, subsystem=Engine (VITCPSocket2)
    (0x0101e268, "VITCPSocket2::Recv"),  # size=84, subsystem=Engine (VITCPSocket2)
    (0x0101e2c0, "VITCPSocket2::Close"),  # size=96, subsystem=Engine (VITCPSocket2)
    (0x0101e320, "VITCPSocket2::Poll"),  # size=44, subsystem=Engine (VITCPSocket2)
    (0x0101e350, "VITCPSocket2::IsConnected"),  # size=8, subsystem=Engine (VITCPSocket2)
    (0x01024760, "Plat_Unicode::Blocks::Mapping::explicitDestroy"),  # size=628, subsystem=String Utils
    (0x010260d8, "Plat_Unicode::Blocks::Data::addRangeGroup"),  # size=1516, subsystem=String Utils
    (0x010266c8, "Plat_Unicode::Blocks::Mapping::initSingleton"),  # size=92, subsystem=String Utils
    (0x01026728, "VIGUIButton::constructor"),  # size=72, subsystem=Engine (VIGUIButton)
    (0x01026770, "VIGUIButton::~destructor"),  # size=172, subsystem=Engine (VIGUIButton)
    (0x01026820, "VIGUIButton::SetNextPage"),  # size=84, subsystem=Engine (VIGUIButton)
    (0x01026878, "VIGUIButton::SetAction"),  # size=84, subsystem=Engine (VIGUIButton)
    (0x010268d0, "VIGUIButton::OnKeyDown"),  # size=172, subsystem=Engine (VIGUIButton)
    (0x01026980, "VIGUIButton::OnKeyUp"),  # size=8, subsystem=Engine (VIGUIButton)
    (0x01026b00, "VITrailFx::Init"),  # size=320, subsystem=Engine (VITrailFx)
    (0x01026c40, "VITrailFx::Render"),  # size=736, subsystem=Engine (VITrailFx)
    (0x01027240, "VITrailFx::constructor"),  # size=56, subsystem=Engine (VITrailFx)
    (0x01027278, "VITrailFx::~destructor"),  # size=108, subsystem=Engine (VITrailFx)
    (0x010272e8, "VITrailFx::Clear"),  # size=76, subsystem=Engine (VITrailFx)
    (0x01027338, "VITrailFx::AddSegment"),  # size=260, subsystem=Engine (VITrailFx)
    (0x01027440, "VITrailFx::AddSegment"),  # size=272, subsystem=Engine (VITrailFx)
    (0x01027550, "VITrailFx::Update"),  # size=196, subsystem=Engine (VITrailFx)
    (0x01027618, "VITrailFx::ClearSegmentsForward"),  # size=104, subsystem=Engine (VITrailFx)
    (0x01027bd0, "Plat_Unicode::CharDataMap::generateMapFromBuffer"),  # size=3372, subsystem=String Utils
    (0x01028900, "Plat_Unicode::CharDataMap::generateMap"),  # size=484, subsystem=String Utils
    (0x01028ae8, "Plat_Unicode::CharDataMap::initSingleton"),  # size=84, subsystem=String Utils
    (0x01028b40, "Plat_Unicode::CharDataMap::explicitDestroy"),  # size=60, subsystem=String Utils
    (0x01028b80, "Plat_Unicode::CharDataMap::addBlock"),  # size=60, subsystem=String Utils
    (0x01028bc0, "Plat_Unicode::CharDataMap::removeBlock"),  # size=32, subsystem=String Utils
    (0x01028be0, "Plat_Unicode::CharDataMap::clearBlocks"),  # size=84, subsystem=String Utils
    (0x01028c38, "VIGUIComboBox::~destructor"),  # size=272, subsystem=Engine (VIGUIComboBox)
    (0x01028d48, "VIGUIComboBox::UpdateSelectedIndex"),  # size=336, subsystem=Engine (VIGUIComboBox)
    (0x01028e98, "VIGUIComboBox::OnKeyDown"),  # size=1048, subsystem=Engine (VIGUIComboBox)
    (0x010292b0, "VIGUIComboBox::Render"),  # size=1516, subsystem=Engine (VIGUIComboBox)
    (0x010298a0, "VIGUIComboBox::constructor"),  # size=132, subsystem=Engine (VIGUIComboBox)
    (0x01029928, "VIGUIComboBox::SetAction"),  # size=84, subsystem=Engine (VIGUIComboBox)
    (0x01029980, "VIGUIComboBox::AddOption"),  # size=116, subsystem=Engine (VIGUIComboBox)
    (0x010299f8, "VIGUIComboBox::ModifySelection"),  # size=220, subsystem=Engine (VIGUIComboBox)
    (0x01029ad8, "VIGUIComboBox::SetValue"),  # size=188, subsystem=Engine (VIGUIComboBox)
    (0x01029b98, "VIGUIComboBox::Clear"),  # size=144, subsystem=Engine (VIGUIComboBox)
    (0x01029c28, "VIGUIComboBox::SetPopupSize"),  # size=12, subsystem=Engine (VIGUIComboBox)
    (0x01029c38, "VIGUIComboBox::OnKeyUp"),  # size=8, subsystem=Engine (VIGUIComboBox)
    (0x01029c40, "VIUDPSocket::Open"),  # size=164, subsystem=Engine (VIUDPSocket)
    (0x01029ce8, "VIUDPSocket::SendTo"),  # size=604, subsystem=Engine (VIUDPSocket)
    (0x01029f48, "VIUDPSocket::SendTo"),  # size=560, subsystem=Engine (VIUDPSocket)
    (0x0102a178, "VIUDPSocket::constructor"),  # size=76, subsystem=Engine (VIUDPSocket)
    (0x0102a1c8, "VIUDPSocket::~destructor"),  # size=124, subsystem=Engine (VIUDPSocket)
    (0x0102a248, "VIUDPSocket::GetInetAddress"),  # size=128, subsystem=Engine (VIUDPSocket)
    (0x0102a2c8, "VIUDPSocket::GetLocalAddress"),  # size=100, subsystem=Engine (VIUDPSocket)
    (0x0102a330, "VIUDPSocket::GetStringAddress"),  # size=84, subsystem=Engine (VIUDPSocket)
    (0x0102a388, "VIUDPSocket::SendTo"),  # size=232, subsystem=Engine (VIUDPSocket)
    (0x0102a470, "VIUDPSocket::RecvFrom"),  # size=156, subsystem=Engine (VIUDPSocket)
    (0x0102a510, "VIUDPSocket::Close"),  # size=92, subsystem=Engine (VIUDPSocket)
    (0x0102a570, "VIUDPSocket::IsConnected"),  # size=16, subsystem=Engine (VIUDPSocket)
    (0x0102a640, "RealmService::MatchGameNode::__as"),  # size=276, subsystem=Networking
    (0x0102a950, "RealmService::MatchGameAttrsImp::addMatchAttr"),  # size=408, subsystem=DMA/GIF Pipeline
    (0x0102aae8, "RealmService::MatchGameAttrsImp::addMatchAttr"),  # size=332, subsystem=DMA/GIF Pipeline
    (0x0102ac38, "RealmService::MatchGameAttrsImp::addMatchAttr"),  # size=344, subsystem=DMA/GIF Pipeline
    (0x0102b210, "RealmService::GameAttrsNode::__as"),  # size=404, subsystem=Networking
    (0x0102b838, "RealmService::GameStatsNode::__as"),  # size=220, subsystem=Networking
    (0x0102bca0, "RealmService::MatchGameAttrsImp::__as"),  # size=48, subsystem=DMA/GIF Pipeline
    (0x0102bcf8, "RealmService::GameAttrsImp::__as"),  # size=48, subsystem=Networking
    (0x0102bd28, "RealmService::GameAttrsImp::addNode"),  # size=116, subsystem=Networking
    (0x0102bdc8, "RealmService::GameStatsImp::__as"),  # size=48, subsystem=Networking
    (0x0102bdf8, "RealmService::GameStatsImp::addNode"),  # size=116, subsystem=Networking
    (0x0102bed8, "RealmService::PlayerImp::setPlayerInfo"),  # size=152, subsystem=Networking
    (0x0102bf70, "VIGUIDataModel::constructor"),  # size=32, subsystem=Engine (VIGUIDataModel)
    (0x0102bf90, "VIGUIDataModel::constructor"),  # size=68, subsystem=Engine (VIGUIDataModel)
    (0x0102bfd8, "VIGUIDataModel::Initialize"),  # size=56, subsystem=Engine (VIGUIDataModel)
    (0x0102c010, "VIGUIDataModel::SetName"),  # size=28, subsystem=Engine (VIGUIDataModel)
    (0x0102c030, "VIGUIDataModel::GetName"),  # size=8, subsystem=Engine (VIGUIDataModel)
    (0x0102c038, "VIGUIDataModel::SetModelType"),  # size=8, subsystem=Engine (VIGUIDataModel)
    (0x0102c040, "VIGUIDataModel::GetModelType"),  # size=8, subsystem=Engine (VIGUIDataModel)
    (0x0102c048, "VIUI::FrameFillRectangle"),  # size=508, subsystem=UI
    (0x0102c248, "VIUI::FrameRectangle"),  # size=756, subsystem=UI
    (0x0102c540, "VIUI::Blit"),  # size=348, subsystem=UI
    (0x0102c6a0, "VIUI::Blit"),  # size=400, subsystem=UI
    (0x0102c830, "VIUI::BlitEx"),  # size=356, subsystem=UI
    (0x0102c998, "VIUI::BlitEx"),  # size=400, subsystem=UI
    (0x0102cb28, "VIUI::StretchBlitEx"),  # size=284, subsystem=UI
    (0x0102cc48, "VIUI::BlitBar"),  # size=744, subsystem=UI
    (0x0102cf30, "VIUI::BlitBar"),  # size=768, subsystem=UI
    (0x0102d230, "VIUI::BlitVertBar"),  # size=532, subsystem=UI
    (0x0102d448, "VIUI::BlitRect"),  # size=896, subsystem=UI
    (0x0102d7c8, "VIUI::BlitFrame"),  # size=1088, subsystem=UI
    (0x0102dc08, "VIUI::BlitStuddedFrame"),  # size=1176, subsystem=UI
    (0x0102e0a0, "VIUI::BlitFillFrame"),  # size=544, subsystem=UI
    (0x0102e2c0, "VIUI::BlitFillStuddedFrame"),  # size=704, subsystem=UI
    (0x0102e580, "VIUI::BlitHorz"),  # size=464, subsystem=UI
    (0x0102e750, "VIUI::BlitVert"),  # size=464, subsystem=UI
    (0x0102e920, "VIUI::BlitAbilityIcon"),  # size=324, subsystem=UI
    (0x0102ea68, "VIUI::DrawStringEx"),  # size=284, subsystem=UI
    (0x0102eb88, "VIUI::DrawStringEx"),  # size=284, subsystem=UI
    (0x0102eca8, "VIUI::DrawStringEx"),  # size=340, subsystem=UI
    (0x0102ee00, "VIUI::DrawCenteredStringEx"),  # size=304, subsystem=UI
    (0x0102ef30, "VIUI::DrawCenteredStringEx"),  # size=304, subsystem=UI
    (0x0102f060, "VIUI::DrawCenteredStringEx"),  # size=360, subsystem=UI
    (0x0102f1c8, "VIUI::constructor"),  # size=72, subsystem=UI
    (0x0102f210, "VIUI::~destructor"),  # size=116, subsystem=UI
    (0x0102f288, "VIUI::Close"),  # size=64, subsystem=UI
    (0x0102f2c8, "VIUI::Init"),  # size=120, subsystem=UI
    (0x0102f340, "VIUI::FillRectangle"),  # size=184, subsystem=UI
    (0x0102f3f8, "VIUI::Blit"),  # size=184, subsystem=UI
    (0x0102f4b0, "VIUI::Blit"),  # size=152, subsystem=UI
    (0x0102f548, "VIUI::BlitBar"),  # size=264, subsystem=UI
    (0x0102f650, "VIUI::BlitBar"),  # size=248, subsystem=UI
    (0x0102f748, "VIUI::BlitBar"),  # size=272, subsystem=UI
    (0x0102f858, "VIUI::BlitBar"),  # size=256, subsystem=UI
    (0x0102f958, "VIUI::BlitStuddedHorz"),  # size=308, subsystem=UI
    (0x0102fa90, "VIUI::SetLanguage"),  # size=8, subsystem=UI
    (0x0102fa98, "VIUI::Begin2D"),  # size=28, subsystem=UI
    (0x0102fab8, "VIUI::End2D"),  # size=28, subsystem=UI
    (0x0102fad8, "VIUI::SoundPlay"),  # size=108, subsystem=UI
    (0x0102fb48, "VIUI::SoundPlay"),  # size=120, subsystem=UI
    (0x0102fbc0, "VIUI::ReloadWords"),  # size=92, subsystem=UI
    (0x0102fcf0, "RealmService::Player::__as"),  # size=300, subsystem=Networking
    (0x0102ff40, "RealmService::Blob::__as"),  # size=120, subsystem=Networking
    (0x010300f0, "RealmService::MatchGameAttrs::__as"),  # size=188, subsystem=DMA/GIF Pipeline
    (0x010301b0, "RealmService::MatchGameAttrs::addMatchAttr"),  # size=28, subsystem=DMA/GIF Pipeline
    (0x010301d0, "RealmService::MatchGameAttrs::addMatchAttr"),  # size=28, subsystem=DMA/GIF Pipeline
    (0x010301f0, "RealmService::MatchGameAttrs::addMatchAttr"),  # size=28, subsystem=DMA/GIF Pipeline
    (0x01030348, "RealmService::GameAttrs::__as"),  # size=140, subsystem=Networking
    (0x010303d8, "RealmService::GameAttrs::addAttr"),  # size=28, subsystem=Networking
    (0x01030530, "RealmService::GameStats::__as"),  # size=140, subsystem=Networking
    (0x010305c0, "RealmService::GameStats::addStat"),  # size=28, subsystem=Networking
    (0x010306d0, "RealmService::Player::setPlayerInfo"),  # size=28, subsystem=Networking
    (0x010306f0, "VIGUIDialog::Init"),  # size=148, subsystem=Engine (VIGUIDialog)
    (0x01030788, "VIGUIDialog::Render"),  # size=724, subsystem=Engine (VIGUIDialog)
    (0x01030a60, "VIGUIDialog::OnKeyDown"),  # size=472, subsystem=Engine (VIGUIDialog)
    (0x01030c38, "VIGUIDialog::constructor"),  # size=80, subsystem=Engine (VIGUIDialog)
    (0x01030c88, "VIGUIDialog::~destructor"),  # size=152, subsystem=Engine (VIGUIDialog)
    (0x01030d20, "VIGUIDialog::SetText"),  # size=136, subsystem=Engine (VIGUIDialog)
    (0x01030da8, "VIGUIDialog::SetText"),  # size=112, subsystem=Engine (VIGUIDialog)
    (0x01030e18, "VIGUIDialog::SetText"),  # size=168, subsystem=Engine (VIGUIDialog)
    (0x01030ec0, "VIGUIDialog::IsOpen"),  # size=84, subsystem=Engine (VIGUIDialog)
    (0x01030f18, "VIGUIDialog::Lock"),  # size=12, subsystem=Engine (VIGUIDialog)
    (0x01030f28, "VIGUIDialog::UnLock"),  # size=8, subsystem=Engine (VIGUIDialog)
    (0x01030f30, "VIGUIDialog::Show"),  # size=80, subsystem=Engine (VIGUIDialog)
    (0x01030f80, "VIGUIDialog::Show"),  # size=136, subsystem=Engine (VIGUIDialog)
    (0x01031008, "VIGUIDialog::Hide"),  # size=32, subsystem=Engine (VIGUIDialog)
    (0x01031028, "VIGUIDialog::OnKeyUp"),  # size=8, subsystem=Engine (VIGUIDialog)
    (0x01031030, "VIGUIDialog::OnMessage"),  # size=8, subsystem=Engine (VIGUIDialog)
    (0x01031218, "VIGUIObject::Initialize"),  # size=208, subsystem=Engine (VIGUIObject)
    (0x010312e8, "VIGUIObject::FillRectangle"),  # size=312, subsystem=Engine (VIGUIObject)
    (0x01031420, "VIGUIObject::Render"),  # size=1268, subsystem=Engine (VIGUIObject)
    (0x01031918, "VIGUIObject::CleanUp"),  # size=16, subsystem=Engine (VIGUIObject)
    (0x01031928, "VIGUIObject::constructor"),  # size=164, subsystem=Engine (VIGUIObject)
    (0x010319d0, "VIGUIObject::~destructor"),  # size=164, subsystem=Engine (VIGUIObject)
    (0x01031a78, "VIGUIObject::SetGUIType"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031a80, "VIGUIObject::GetGUIType"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031a88, "VIGUIObject::SetGUIRenderer"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031a90, "VIGUIObject::SetGUIDataStore"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031a98, "VIGUIObject::SetName"),  # size=32, subsystem=Engine (VIGUIObject)
    (0x01031ab8, "VIGUIObject::SetAlphaFadeVal"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031ac0, "VIGUIObject::GetName"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031ac8, "VIGUIObject::SetSelectedX"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031ad0, "VIGUIObject::SetSelectEffect"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031ad8, "VIGUIObject::SetPosition"),  # size=24, subsystem=Engine (VIGUIObject)
    (0x01031af0, "VIGUIObject::GetX"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031af8, "VIGUIObject::GetY"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031b00, "VIGUIObject::SetBGColor"),  # size=76, subsystem=Engine (VIGUIObject)
    (0x01031b50, "VIGUIObject::SetTileSet"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031b58, "VIGUIObject::SetTileType"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031b60, "VIGUIObject::SetSize"),  # size=12, subsystem=Engine (VIGUIObject)
    (0x01031b70, "VIGUIObject::SetButtonPosition"),  # size=12, subsystem=Engine (VIGUIObject)
    (0x01031b80, "VIGUIObject::GetButtonX"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031b88, "VIGUIObject::GetButtonY"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031b90, "VIGUIObject::SetImageOffset"),  # size=12, subsystem=Engine (VIGUIObject)
    (0x01031ba0, "VIGUIObject::GetImageOffsetX"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031ba8, "VIGUIObject::GetImageOffsetY"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bb0, "VIGUIObject::SetDepthLevel"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bb8, "VIGUIObject::GetDepthLevel"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bc0, "VIGUIObject::SetTexture"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bc8, "VIGUIObject::SetRollTexture"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bd0, "VIGUIObject::SetCapTexture"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bd8, "VIGUIObject::SetTextureID"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031be0, "VIGUIObject::SetRollTextureID"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031be8, "VIGUIObject::SetAlphaTarget"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031bf0, "VIGUIObject::AdjustAlpha"),  # size=152, subsystem=Engine (VIGUIObject)
    (0x01031c88, "VIGUIObject::AdjustX"),  # size=92, subsystem=Engine (VIGUIObject)
    (0x01031ce8, "VIGUIObject::SetSelectedAlpha"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031cf0, "VIGUIObject::SetAlpha"),  # size=12, subsystem=Engine (VIGUIObject)
    (0x01031d00, "VIGUIObject::GetDataModel"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031d08, "VIGUIObject::SetSelected"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031d10, "VIGUIObject::IsSelected"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x01031d18, "VIUITextScroll::TextScroll"),  # size=1044, subsystem=Engine (VIUITextScroll)
    (0x01032130, "VIUITextScroll::constructor"),  # size=68, subsystem=Engine (VIUITextScroll)
    (0x01032178, "VIUITextScroll::~destructor"),  # size=84, subsystem=Engine (VIUITextScroll)
    (0x010321d0, "VIUITextScroll::Init"),  # size=68, subsystem=Engine (VIUITextScroll)
    (0x01032218, "VIUITextScroll::Reset"),  # size=28, subsystem=Engine (VIUITextScroll)
    (0x01032238, "VIUITextScroll::TextScroll"),  # size=32, subsystem=Engine (VIUITextScroll)
    (0x01032258, "VIUITextScroll::SetOn"),  # size=8, subsystem=Engine (VIUITextScroll)
    (0x01032260, "Plat_Unicode::toLower"),  # size=616, subsystem=String Utils
    (0x010324c8, "Plat_Unicode::toUpper"),  # size=536, subsystem=String Utils
    (0x010326e0, "Plat_Unicode::toLower"),  # size=552, subsystem=String Utils
    (0x01032908, "Plat_Unicode::toUpper"),  # size=552, subsystem=String Utils
    (0x01032b30, "Plat_Unicode::appendStringField"),  # size=596, subsystem=String Utils
    (0x01032d88, "Plat_Unicode::getFirstToken"),  # size=868, subsystem=String Utils
    (0x010330f0, "Plat_Unicode::getFirstToken"),  # size=776, subsystem=String Utils
    (0x010333f8, "Plat_Unicode::getNthToken"),  # size=1012, subsystem=String Utils
    (0x010337f0, "Plat_Unicode::getNthToken"),  # size=900, subsystem=String Utils
    (0x01033b78, "Base::get"),  # size=164, subsystem=Networking
    (0x01033c20, "Base::put"),  # size=92, subsystem=Networking
    (0x01035c80, "VIGUIPageBuilder::BuildPageFromFile"),  # size=312, subsystem=Engine (VIGUIPageBuilder)
    (0x01035db8, "VIGUIPageBuilder::constructor"),  # size=16, subsystem=Engine (VIGUIPageBuilder)
    (0x01035dc8, "VIGUIPageBuilder::BuildPageFromBuffer"),  # size=152, subsystem=Engine (VIGUIPageBuilder)
    (0x01035e60, "VIGUIPageBuilder::SetCurrentGUIPage"),  # size=8, subsystem=Engine (VIGUIPageBuilder)
    (0x01035e68, "VIGUIPageBuilder::GetCurrentGUIPage"),  # size=8, subsystem=Engine (VIGUIPageBuilder)
    (0x01035e70, "VIGUIPageBuilder::GetGenericRenderer"),  # size=8, subsystem=Engine (VIGUIPageBuilder)
    (0x01035e78, "VIGUIPageBuilder::SetCurrentGUIObject"),  # size=8, subsystem=Engine (VIGUIPageBuilder)
    (0x01035e80, "VIGUIPageBuilder::GetCurrentGUIObject"),  # size=8, subsystem=Engine (VIGUIPageBuilder)
    (0x0103a650, "VIGUISelectionGrid::HandleKeyPress"),  # size=564, subsystem=Engine (VIGUISelectionGrid)
    (0x0103a888, "VIGUIPage::~destructor"),  # size=436, subsystem=Engine (VIGUIPage)
    (0x0103aa40, "VIGUIPage::SelectObject"),  # size=316, subsystem=Engine (VIGUIPage)
    (0x0103ab80, "VIGUIPage::AddGUIObject"),  # size=336, subsystem=Engine (VIGUIPage)
    (0x0103acd0, "VIGUIPage::GetStringValue"),  # size=244, subsystem=Engine (VIGUIPage)
    (0x0103adc8, "VIGUIPage::GetBoolValue"),  # size=228, subsystem=Engine (VIGUIPage)
    (0x0103aeb0, "VIGUIPage::SetStringValue"),  # size=256, subsystem=Engine (VIGUIPage)
    (0x0103afb0, "VIGUIPage::SetStringValue"),  # size=260, subsystem=Engine (VIGUIPage)
    (0x0103b0b8, "VIGUIPage::Render"),  # size=524, subsystem=Engine (VIGUIPage)
    (0x0103b2c8, "VIGUIPage::OnKeyDown"),  # size=304, subsystem=Engine (VIGUIPage)
    (0x0103b3f8, "VIGUISelectionGrid::constructor"),  # size=28, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b418, "VIGUISelectionGrid::Init"),  # size=140, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b4a8, "VIGUISelectionGrid::~destructor"),  # size=228, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b590, "VIGUISelectionGrid::AddObject"),  # size=136, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b618, "VIGUISelectionGrid::SelectObject"),  # size=276, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b730, "VIGUISelectionGrid::GetSelectedObject"),  # size=52, subsystem=Engine (VIGUISelectionGrid)
    (0x0103b768, "VIGUIPage::constructor"),  # size=84, subsystem=Engine (VIGUIPage)
    (0x0103b7c0, "VIGUIPage::constructor"),  # size=108, subsystem=Engine (VIGUIPage)
    (0x0103b830, "VIGUIPage::Init"),  # size=148, subsystem=Engine (VIGUIPage)
    (0x0103b8c8, "VIGUIPage::InternalInit"),  # size=92, subsystem=Engine (VIGUIPage)
    (0x0103b928, "VIGUIPage::GetName"),  # size=8, subsystem=Engine (VIGUIPage)
    (0x0103b930, "VIGUIPage::SetSelector"),  # size=68, subsystem=Engine (VIGUIPage)
    (0x0103b978, "VIGUIPage::SetSelectorX"),  # size=8, subsystem=Engine (VIGUIPage)
    (0x0103b980, "VIGUIPage::SetSelectorY"),  # size=8, subsystem=Engine (VIGUIPage)
    (0x0103b988, "VIGUIPage::SetName"),  # size=28, subsystem=Engine (VIGUIPage)
    (0x0103b9a8, "VIGUIPage::AddGUIObject"),  # size=176, subsystem=Engine (VIGUIPage)
    (0x0103ba58, "VIGUIPage::GetObjectByName"),  # size=168, subsystem=Engine (VIGUIPage)
    (0x0103bb00, "VIGUIPage::SetBoolValue"),  # size=220, subsystem=Engine (VIGUIPage)
    (0x0103bbe0, "VIGUIPage::ClearComboValues"),  # size=192, subsystem=Engine (VIGUIPage)
    (0x0103bca0, "VIGUIPage::AddComboValue"),  # size=208, subsystem=Engine (VIGUIPage)
    (0x0103bd70, "VIGUIPage::SetLabelTextColor"),  # size=240, subsystem=Engine (VIGUIPage)
    (0x0103be60, "VIGUIPage::OnKeyUp"),  # size=100, subsystem=Engine (VIGUIPage)
    (0x0103bec8, "VIGUIPage::OnMessage"),  # size=100, subsystem=Engine (VIGUIPage)
    (0x0103bf30, "VIUIWindow::Draw"),  # size=1836, subsystem=Engine (VIUIWindow)
    (0x0103c660, "VIUIWindow::TextBox"),  # size=3008, subsystem=Engine (VIUIWindow)
    (0x0103d220, "VIUIWindow::DrawFrame"),  # size=824, subsystem=Engine (VIUIWindow)
    (0x0103d558, "VIUIWindow::DrawFrameVScroll"),  # size=508, subsystem=Engine (VIUIWindow)
    (0x0103d758, "VIUIWindow::DrawHScroll"),  # size=648, subsystem=Engine (VIUIWindow)
    (0x0103d9e0, "VIUIWindow::DrawProgress"),  # size=784, subsystem=Engine (VIUIWindow)
    (0x0103dcf0, "VIUIWindow::TickR"),  # size=244, subsystem=Engine (VIUIWindow)
    (0x0103dde8, "VIUIWindow::TickU"),  # size=244, subsystem=Engine (VIUIWindow)
    (0x0103dee0, "VIUIWindow::TickD"),  # size=244, subsystem=Engine (VIUIWindow)
    (0x0103dfd8, "VIUIWindow::TextWidth"),  # size=276, subsystem=Engine (VIUIWindow)
    (0x0103e0f0, "VIUIWindow::DrawTextInternal"),  # size=3608, subsystem=Engine (VIUIWindow)
    (0x0103ef08, "VIUIWindow::constructor"),  # size=108, subsystem=Engine (VIUIWindow)
    (0x0103ef78, "VIUIWindow::~destructor"),  # size=44, subsystem=Engine (VIUIWindow)
    (0x0103efa8, "VIUIWindow::Init"),  # size=208, subsystem=Engine (VIUIWindow)
    (0x0103f078, "VIUIWindow::Init"),  # size=192, subsystem=Engine (VIUIWindow)
    (0x0103f138, "VIUIWindow::Free"),  # size=8, subsystem=Engine (VIUIWindow)
    (0x0103f140, "VIUIWindow::RowCenter"),  # size=144, subsystem=Engine (VIUIWindow)
    (0x0103f1d0, "VIUIWindow::SetTitle"),  # size=76, subsystem=Engine (VIUIWindow)
    (0x0103f220, "VIUIWindow::SetTitle"),  # size=80, subsystem=Engine (VIUIWindow)
    (0x0103f270, "VIUIWindow::T"),  # size=56, subsystem=Engine (VIUIWindow)
    (0x0103f2a8, "VIUIWindow::T"),  # size=8, subsystem=Engine (VIUIWindow)
    (0x0103f2b0, "VIUIWindow::T"),  # size=36, subsystem=Engine (VIUIWindow)
    (0x0103f2d8, "VIUIWindow::Text"),  # size=324, subsystem=Engine (VIUIWindow)
    (0x0103f420, "VIUIWindow::Text"),  # size=332, subsystem=Engine (VIUIWindow)
    (0x0103f570, "VIUIWindow::TextBox"),  # size=32, subsystem=Engine (VIUIWindow)
    (0x0103f590, "VIUIWindow::CountLines"),  # size=48, subsystem=Engine (VIUIWindow)
    (0x0103f5c0, "VIUIWindow::DrawVScroll"),  # size=280, subsystem=Engine (VIUIWindow)
    (0x0103f778, "VIUIWindow::ResetTickPulse"),  # size=40, subsystem=Engine (VIUIWindow)
    (0x0103f800, "VIUIWindow::Open"),  # size=36, subsystem=Engine (VIUIWindow)
    (0x0103f880, "VIUIWindow::Close"),  # size=24, subsystem=Engine (VIUIWindow)
    (0x0103f898, "VIUIWindow::AppendEllipsis"),  # size=212, subsystem=Engine (VIUIWindow)
    (0x0103f970, "VIUIWindow::CopyAsteriks"),  # size=60, subsystem=Engine (VIUIWindow)
    (0x0103f9b0, "VIUIWindow::SetUiColors"),  # size=224, subsystem=Engine (VIUIWindow)
    (0x010462b0, "VIGUIStringDataModel::constructor"),  # size=56, subsystem=Engine (VIGUIStringDataModel)
    (0x010462e8, "VIGUIStringDataModel::constructor"),  # size=56, subsystem=Engine (VIGUIStringDataModel)
    (0x01046320, "VIGUIStringDataModel::InitializeString"),  # size=16, subsystem=Engine (VIGUIStringDataModel)
    (0x01046330, "VIGUIStringDataModel::~destructor"),  # size=132, subsystem=Engine (VIGUIStringDataModel)
    (0x010463b8, "VIGUIStringDataModel::SetString"),  # size=184, subsystem=Engine (VIGUIStringDataModel)
    (0x01046470, "VIGUIStringDataModel::GetString"),  # size=8, subsystem=Engine (VIGUIStringDataModel)
    (0x01046478, "VIGUIStringDataModel::SetMaxLength"),  # size=8, subsystem=Engine (VIGUIStringDataModel)
    (0x01046480, "VIGUIStringDataModel::GetMaxLength"),  # size=8, subsystem=Engine (VIGUIStringDataModel)
    (0x01047398, "VIGUIText::constructor"),  # size=288, subsystem=Engine (VIGUIText)
    (0x010474b8, "VIGUIText::constructor"),  # size=272, subsystem=Engine (VIGUIText)
    (0x010475c8, "VIGUIText::GetFittedString"),  # size=296, subsystem=Engine (VIGUIText)
    (0x010476f0, "VIGUIText::Render"),  # size=1196, subsystem=Engine (VIGUIText)
    (0x01047ba0, "VIGUIText::OnKeyDown"),  # size=332, subsystem=Engine (VIGUIText)
    (0x01047cf0, "VIGUIText::HandleEvent"),  # size=312, subsystem=Engine (VIGUIText)
    (0x01047e28, "VIGUIText::GetStringDataModel"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01047e30, "VIGUIText::SetEditLabel"),  # size=32, subsystem=Engine (VIGUIText)
    (0x01047e50, "VIGUIText::SetMaxChars"),  # size=20, subsystem=Engine (VIGUIText)
    (0x01047e68, "VIGUIText::OnKeyUp"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01047e70, "VIGUIText::SetShadow"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01047e78, "VIGUIText::SetTextColor"),  # size=76, subsystem=Engine (VIGUIText)
    (0x01047ec8, "VIGUIText::SetRollColor"),  # size=76, subsystem=Engine (VIGUIText)
    (0x01047f18, "VIGUIText::GetTextColor"),  # size=44, subsystem=Engine (VIGUIText)
    (0x01047f48, "VIGUIText::GetRollColor"),  # size=44, subsystem=Engine (VIGUIText)
    (0x01047f78, "VIGUIText::SetAlignment"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01047f80, "VIGUIText::SetWrapMode"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01047fb0, "VIVect2::Normalize"),  # size=88, subsystem=Engine (VIVect2)
    (0x01048008, "VIVect2::NormalizeMagn"),  # size=92, subsystem=Engine (VIVect2)
    (0x01048e20, "VIGUITextureSet::constructor"),  # size=8, subsystem=Engine (VIGUITextureSet)
    (0x01048e28, "VIGUITextureSet::AddTexture"),  # size=8, subsystem=Engine (VIGUITextureSet)
    (0x01048e30, "VIGUITextureSet::GetCurrentTexture"),  # size=8, subsystem=Engine (VIGUITextureSet)
    (0x01048f58, "VIGUIToggleButton::Render"),  # size=192, subsystem=Engine (VIGUIToggleButton)
    (0x01049018, "VIGUIToggleButton::constructor"),  # size=108, subsystem=Engine (VIGUIToggleButton)
    (0x01049088, "VIGUIToggleButton::GetToggleDataModel"),  # size=8, subsystem=Engine (VIGUIToggleButton)
    (0x01049090, "VIGUIToggleButton::SetToggleTexture"),  # size=8, subsystem=Engine (VIGUIToggleButton)
    (0x01049098, "VIGUIToggleButton::OnKeyDown"),  # size=64, subsystem=Engine (VIGUIToggleButton)
    (0x010490d8, "VIVect3D::Normalize"),  # size=256, subsystem=Engine (VIVect3D)
    (0x010491d8, "VIVect3D::NormalizeMagn"),  # size=268, subsystem=Engine (VIVect3D)
    (0x01049538, "VIVect3D::HPR"),  # size=192, subsystem=Engine (VIVect3D)
    (0x0104f1c8, "VIGUIToggleDataModel::constructor"),  # size=56, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f200, "VIGUIToggleDataModel::constructor"),  # size=56, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f238, "VIGUIToggleDataModel::InitializeToggle"),  # size=8, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f240, "VIGUIToggleDataModel::SetToggleState"),  # size=8, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f248, "VIGUIToggleDataModel::GetToggleState"),  # size=8, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f250, "VIGUIToggleDataModel::Toggle"),  # size=16, subsystem=Engine (VIGUIToggleDataModel)
    (0x0104f260, "VIVect3::__as"),  # size=88, subsystem=Engine (VIVect3)
    (0x0104f2f0, "VIVect3::Normalize"),  # size=112, subsystem=Engine (VIVect3)
    (0x0104f360, "VIVect3::NormalizeMagn"),  # size=112, subsystem=Engine (VIVect3)
    (0x0104f420, "VIVect3::HPR"),  # size=132, subsystem=Engine (VIVect3)
    (0x01051ed0, "Base::put"),  # size=364, subsystem=Networking
    (0x01052040, "Base::get"),  # size=580, subsystem=Networking
    (0x01052288, "Base::put"),  # size=208, subsystem=Networking
    (0x01052358, "Base::get"),  # size=384, subsystem=Networking
    (0x010524d8, "Base::put"),  # size=380, subsystem=Networking
    (0x01052658, "Base::get"),  # size=568, subsystem=Networking
    (0x01052890, "Base::put"),  # size=436, subsystem=Networking
    (0x01052a48, "Base::get"),  # size=660, subsystem=Networking
    (0x01052ce0, "Base::put"),  # size=448, subsystem=Networking
    (0x01052ea0, "Base::get"),  # size=620, subsystem=Networking
    (0x01053110, "Base::get"),  # size=228, subsystem=Networking
    (0x010531f8, "Base::get"),  # size=212, subsystem=Networking
    (0x010532d0, "Base::get"),  # size=184, subsystem=Networking
    (0x010534e8, "Base::put"),  # size=28, subsystem=Networking
    (0x01053508, "Base::get"),  # size=132, subsystem=Networking
    (0x01053590, "Base::put"),  # size=76, subsystem=Networking
    (0x010535e0, "Base::get"),  # size=96, subsystem=Networking
    (0x01053640, "Base::put"),  # size=28, subsystem=Networking
    (0x01053660, "Base::get"),  # size=132, subsystem=Networking
    (0x010536e8, "Base::put"),  # size=72, subsystem=Networking
    (0x01053730, "Base::get"),  # size=84, subsystem=Networking
    (0x01053788, "Base::put"),  # size=28, subsystem=Networking
    (0x010537a8, "Base::get"),  # size=132, subsystem=Networking
    (0x01053830, "Base::put"),  # size=112, subsystem=Networking
    (0x010538a0, "Base::put"),  # size=116, subsystem=Networking
    (0x01053918, "Base::put"),  # size=88, subsystem=Networking
    (0x0105cce0, "VIHSpriteAnim::GetNodeFrame"),  # size=348, subsystem=Engine (VIHSpriteAnim)
    (0x0105ce40, "VIHSpriteAnim::CalcDataSize"),  # size=136, subsystem=Engine (VIHSpriteAnim)
    (0x0105cec8, "VIHSpriteAnim::constructor"),  # size=36, subsystem=Engine (VIHSpriteAnim)
    (0x0105cef0, "VIHSpriteAnim::~destructor"),  # size=84, subsystem=Engine (VIHSpriteAnim)
    (0x0105cf48, "VIHSpriteAnim::Init"),  # size=188, subsystem=Engine (VIHSpriteAnim)
    (0x0105d008, "VIHSpriteAnim::Clear"),  # size=116, subsystem=Engine (VIHSpriteAnim)
    (0x0105d090, "VIHSpriteAnim::SetPlayRate"),  # size=12, subsystem=Engine (VIHSpriteAnim)
    (0x0105d0a8, "VIHSpriteAnim::SetPlaySpeed"),  # size=12, subsystem=Engine (VIHSpriteAnim)
    (0x0105d0c0, "VIHSpriteAnim::SetPlaybackType"),  # size=12, subsystem=Engine (VIHSpriteAnim)
    (0x0105d0d0, "VIHSpriteAnim::GetNodeRefID"),  # size=20, subsystem=Engine (VIHSpriteAnim)
    (0x0105d0e8, "VIHSpriteAnim::SetNodeRefID"),  # size=24, subsystem=Engine (VIHSpriteAnim)
    (0x0105d100, "VIHSpriteAnim::SetNodeFrame"),  # size=128, subsystem=Engine (VIHSpriteAnim)
    (0x0105d180, "VIHSpriteAnim::SetNodeFrame"),  # size=136, subsystem=Engine (VIHSpriteAnim)
    (0x0105d208, "VIHSpriteAnim::SetKeyframe"),  # size=28, subsystem=Engine (VIHSpriteAnim)
    (0x0105d228, "VIHSpriteAnim::Allocate"),  # size=72, subsystem=Engine (VIHSpriteAnim)
    (0x0105ebe8, "VIActorFilter::constructor"),  # size=32, subsystem=Engine (VIActorFilter)
    (0x0105ec08, "VIActorFilter::Init"),  # size=16, subsystem=Engine (VIActorFilter)
    (0x0105ec18, "VIActorFilter::Init"),  # size=12, subsystem=Engine (VIActorFilter)
    (0x0105ec28, "VIActorFilter::FilterActor"),  # size=16, subsystem=Engine (VIActorFilter)
    (0x0105ec38, "VIHSpriteFrame::Pack"),  # size=2972, subsystem=Engine (VIHSpriteFrame)
    (0x0105f7d8, "VIHSprite::constructor"),  # size=532, subsystem=Sprites
    (0x0105f9f0, "VIHSprite::Clear"),  # size=160, subsystem=Sprites
    (0x0105fa90, "VIHSprite::SetNodeBindPose"),  # size=528, subsystem=Sprites
    (0x0105fca0, "VIHSprite::CalcNodeTransform"),  # size=432, subsystem=Sprites
    (0x0105fe50, "VIHSprite::AddPlay"),  # size=644, subsystem=Sprites
    (0x010600d8, "VIHSprite::ErasePlay"),  # size=268, subsystem=Sprites
    (0x010601e8, "VIHSprite::FreezePlayback"),  # size=272, subsystem=Sprites
    (0x010602f8, "VIHSprite::SetPlayFrame"),  # size=316, subsystem=Sprites
    (0x01060438, "VIHSprite::StopCenterTransformBlend"),  # size=272, subsystem=Sprites
    (0x01060548, "VIHSprite::Raster"),  # size=632, subsystem=Sprites
    (0x010607c0, "VIHSprite::Collide"),  # size=568, subsystem=Sprites
    (0x010609f8, "VIHSprite::Collide"),  # size=568, subsystem=Sprites
    (0x01060c30, "VIHSprite::Pick"),  # size=712, subsystem=Sprites
    (0x01060ef8, "VIHSprite::QueryEmitters"),  # size=532, subsystem=Sprites
    (0x01061110, "VIHSprite::QueryIntersection"),  # size=528, subsystem=Sprites
    (0x01061320, "VIHSprite::Copy"),  # size=888, subsystem=Sprites
    (0x01061698, "VIHSprite::Release"),  # size=332, subsystem=Sprites
    (0x010617e8, "VIHSprite::Add"),  # size=224, subsystem=Sprites
    (0x010618c8, "VIHSprite::UpdateCenterTransform"),  # size=568, subsystem=Sprites
    (0x01061b00, "VIHSprite::InterpTransAboutCenter"),  # size=748, subsystem=Sprites
    (0x01061df0, "VIHSprite::ProcessPlayList"),  # size=2220, subsystem=Sprites
    (0x010626a0, "VIHSprite::ProcessPlayTiming"),  # size=1324, subsystem=Sprites
    (0x01062bd0, "VIHSprite::ProcessHierarchy"),  # size=388, subsystem=Sprites
    (0x01062d58, "VIHSprite::ProcessUpHierarchy"),  # size=392, subsystem=Sprites
    (0x01062ee0, "VIHSprite::SetBlendMatrices"),  # size=368, subsystem=Sprites
    (0x01063050, "VIHSprite::SyncTiming"),  # size=232, subsystem=Sprites
    (0x01063138, "VIHSprite::PrecalcPlayback"),  # size=164, subsystem=Sprites
    (0x010631e0, "VIHSprite::CalcLODLevelIndex"),  # size=160, subsystem=Sprites
    (0x01063280, "VIHSprite::CalcLODLevelIndex"),  # size=316, subsystem=Sprites
    (0x010633c0, "VIHSprite::~destructor"),  # size=188, subsystem=Sprites
    (0x01063480, "VIHSprite::Init"),  # size=44, subsystem=Sprites
    (0x010634b0, "VIHSprite::Size"),  # size=8, subsystem=Sprites
    (0x010634b8, "VIHSprite::Root"),  # size=44, subsystem=Sprites
    (0x010634e8, "VIHSprite::End"),  # size=12, subsystem=Sprites
    (0x010634f8, "VIHSprite::First"),  # size=36, subsystem=Sprites
    (0x01063520, "VIHSprite::Last"),  # size=84, subsystem=Sprites
    (0x01063578, "VIHSprite::Next"),  # size=36, subsystem=Sprites
    (0x010635a0, "VIHSprite::Prev"),  # size=96, subsystem=Sprites
    (0x01063600, "VIHSprite::Parent"),  # size=28, subsystem=Sprites
    (0x01063620, "VIHSprite::IsLeaf"),  # size=28, subsystem=Sprites
    (0x01063640, "VIHSprite::GetNodeBindPose"),  # size=100, subsystem=Sprites
    (0x010636a8, "VIHSprite::SetNodeFixScale"),  # size=48, subsystem=Sprites
    (0x010636d8, "VIHSprite::GetNodeFixScale"),  # size=48, subsystem=Sprites
    (0x01063708, "VIHSprite::FindTrigger"),  # size=76, subsystem=Sprites
    (0x01063758, "VIHSprite::HasTripped"),  # size=20, subsystem=Sprites
    (0x01063770, "VIHSprite::ResetTrigger"),  # size=24, subsystem=Sprites
    (0x01063788, "VIHSprite::AttachSkin"),  # size=92, subsystem=Sprites
    (0x010637e8, "VIHSprite::Attach"),  # size=100, subsystem=Sprites
    (0x01063850, "VIHSprite::Detach"),  # size=108, subsystem=Sprites
    (0x01063a78, "VIHSprite::AddPlay"),  # size=84, subsystem=Sprites
    (0x01063ad0, "VIHSprite::AddPlay"),  # size=96, subsystem=Sprites
    (0x01063b30, "VIHSprite::AddPlayWithSync"),  # size=156, subsystem=Sprites
    (0x01063bd0, "VIHSprite::AddInterpolatedPlay"),  # size=108, subsystem=Sprites
    (0x01063c40, "VIHSprite::AddInterpolatedPlayWithSync"),  # size=220, subsystem=Sprites
    (0x01063d20, "VIHSprite::EraseAllPlay"),  # size=144, subsystem=Sprites
    (0x01063db0, "VIHSprite::StopPlayback"),  # size=108, subsystem=Sprites
    (0x01063e20, "VIHSprite::StopPlaybackAtCycle"),  # size=108, subsystem=Sprites
    (0x01063e90, "VIHSprite::StopAllPlayback"),  # size=196, subsystem=Sprites
    (0x01063f58, "VIHSprite::IsPlaybackStopped"),  # size=44, subsystem=Sprites
    (0x01063f88, "VIHSprite::IsBlendComplete"),  # size=100, subsystem=Sprites
    (0x01063ff0, "VIHSprite::GetPlayAnimation"),  # size=36, subsystem=Sprites
    (0x01064018, "VIHSprite::SetPlaySpeed"),  # size=76, subsystem=Sprites
    (0x01064068, "VIHSprite::GetPlaySpeed"),  # size=36, subsystem=Sprites
    (0x01064090, "VIHSprite::SetPlayRate"),  # size=76, subsystem=Sprites
    (0x010640e0, "VIHSprite::GetPlayRate"),  # size=36, subsystem=Sprites
    (0x01064108, "VIHSprite::SetCenterTransform"),  # size=200, subsystem=Sprites
    (0x010641d0, "VIHSprite::BlendToCenterTransform"),  # size=352, subsystem=Sprites
    (0x01064330, "VIHSprite::IsCenterTransformBlending"),  # size=12, subsystem=Sprites
    (0x01064340, "VIHSprite::IsCenterTransformBlendComplete"),  # size=80, subsystem=Sprites
    (0x01064390, "VIHSprite::AddRoot"),  # size=108, subsystem=Sprites
    (0x01064400, "VIHSprite::Process"),  # size=168, subsystem=Sprites
    (0x010644a8, "VIHSprite::CalcTransAboutCenter"),  # size=120, subsystem=Sprites
    (0x01064520, "VIHSprite::SetBindPose"),  # size=120, subsystem=Sprites
    (0x01064598, "VIHSprite::ProcessHierarchy"),  # size=164, subsystem=Sprites
    (0x01064640, "VIVect4D::Normalize"),  # size=312, subsystem=Engine (VIVect4D)
    (0x01064778, "VIVect4D::NormalizeMagn"),  # size=324, subsystem=Engine (VIVect4D)
    (0x010658e8, "VIActor::constructor"),  # size=188, subsystem=Engine (VIActor)
    (0x010659a8, "VIActor::~destructor"),  # size=84, subsystem=Engine (VIActor)
    (0x01065a00, "VIActor::CalcObjectToWorld"),  # size=40, subsystem=Engine (VIActor)
    (0x01065a28, "VIIconDefinition::constructor"),  # size=540, subsystem=Engine (VIIconDefinition)
    (0x01065c48, "VIIconDefinition::SetTitle"),  # size=316, subsystem=Engine (VIIconDefinition)
    (0x01065d88, "VIIconDefinition::Ascii2Sjis"),  # size=252, subsystem=Engine (VIIconDefinition)
    (0x01065e88, "VIIconDefinition::~destructor"),  # size=44, subsystem=Engine (VIIconDefinition)
    (0x01065eb8, "VIIconDefinition::SetIcon"),  # size=120, subsystem=Engine (VIIconDefinition)
    (0x01065f30, "VIIconDefinition::AsciiString2Sjis"),  # size=172, subsystem=Engine (VIIconDefinition)
    (0x010661a0, "VILanguage::GetName"),  # size=80, subsystem=Engine (VILanguage)
    (0x010661f0, "VILanguage::GetIsoCode"),  # size=80, subsystem=Engine (VILanguage)
    (0x01066240, "VILanguage::GetID"),  # size=112, subsystem=Engine (VILanguage)
    (0x010662b0, "VILanguage::GetDefault"),  # size=12, subsystem=Engine (VILanguage)
    (0x010662c0, "VILanguage::SetDefault"),  # size=12, subsystem=Engine (VILanguage)
    (0x010662d0, "VIVect4::__as"),  # size=100, subsystem=Engine (VIVect4)
    (0x01066378, "VIVect4::Normalize"),  # size=120, subsystem=Engine (VIVect4)
    (0x010663f0, "VIVect4::NormalizeMagn"),  # size=132, subsystem=Engine (VIVect4)
    (0x01066538, "VIAtmosphere::constructor"),  # size=580, subsystem=Engine (VIAtmosphere)
    (0x01066780, "VIAtmosphere::Init"),  # size=2844, subsystem=Engine (VIAtmosphere)
    (0x010672a0, "VIAtmosphere::Clear"),  # size=380, subsystem=Engine (VIAtmosphere)
    (0x01067420, "VIAtmosphere::SetResources"),  # size=1956, subsystem=Engine (VIAtmosphere)
    (0x01067bc8, "VIAtmosphere::SetSkyColor"),  # size=352, subsystem=Engine (VIAtmosphere)
    (0x01067d28, "VIAtmosphere::Update"),  # size=524, subsystem=Engine (VIAtmosphere)
    (0x01067f38, "VIAtmosphere::RenderSky"),  # size=652, subsystem=Engine (VIAtmosphere)
    (0x010681c8, "VIAtmosphere::RenderWeather"),  # size=1464, subsystem=Engine (VIAtmosphere)
    (0x01068780, "VIAtmosphere::ProcessWeather"),  # size=2632, subsystem=Engine (VIAtmosphere)
    (0x010691c8, "VIAtmosphere::ProcessTransitions"),  # size=3672, subsystem=Engine (VIAtmosphere)
    (0x0106a020, "VIAtmosphere::RecomputeLightningPatches"),  # size=620, subsystem=Engine (VIAtmosphere)
    (0x0106a290, "VIAtmosphere::GetLightning"),  # size=576, subsystem=Engine (VIAtmosphere)
    (0x0106a4d0, "VIAtmosphere::RenderStars"),  # size=1640, subsystem=Engine (VIAtmosphere)
    (0x0106ab38, "VIAtmosphere::RenderSplashes"),  # size=420, subsystem=Engine (VIAtmosphere)
    (0x0106ace0, "VIAtmosphere::ProcessLavastorm"),  # size=1572, subsystem=Engine (VIAtmosphere)
    (0x0106b308, "WeatherFilter::FilterActor"),  # size=8, subsystem=C++ Runtime
    (0x0106b310, "VIAtmosphere::~destructor"),  # size=164, subsystem=Engine (VIAtmosphere)
    (0x0106b3b8, "VIAtmosphere::SetWeather"),  # size=172, subsystem=Engine (VIAtmosphere)
    (0x0106b468, "VIAtmosphere::SetPlaneOfSky"),  # size=48, subsystem=Engine (VIAtmosphere)
    (0x0106b498, "VIAtmosphere::SetDefaultSky"),  # size=220, subsystem=Engine (VIAtmosphere)
    (0x0106b578, "VIAtmosphere::GetOvercastInterp"),  # size=104, subsystem=Engine (VIAtmosphere)
    (0x0106b5e8, "VIAtmosphere::SetEffectMix"),  # size=8, subsystem=Engine (VIAtmosphere)
    (0x0106b5f8, "VIAtmosphere::SetIntensity"),  # size=84, subsystem=Engine (VIAtmosphere)
    (0x0106b680, "VIAtmosphere::SetLavastormIntensity"),  # size=112, subsystem=Engine (VIAtmosphere)
    (0x0106b6f8, "VIAtmosphere::SetParticleScale"),  # size=8, subsystem=Engine (VIAtmosphere)
    (0x0106b700, "VIAtmosphere::ResetLightning"),  # size=220, subsystem=Engine (VIAtmosphere)
    (0x0106b7e0, "VIAtmosphere::AddSplash"),  # size=208, subsystem=Engine (VIAtmosphere)
    (0x0106b8b0, "VIAtmosphere::ClearAllSplashes"),  # size=176, subsystem=Engine (VIAtmosphere)
    (0x0106b960, "VIAtmosphere::ClearAllFireballs"),  # size=200, subsystem=Engine (VIAtmosphere)
    (0x0106bc68, "VILauncher::Init"),  # size=276, subsystem=Engine (VILauncher)
    (0x0106bd80, "VILauncher::Free"),  # size=356, subsystem=Engine (VILauncher)
    (0x0106c258, "VILauncher::constructor"),  # size=8, subsystem=Engine (VILauncher)
    (0x0106c260, "VILauncher::~destructor"),  # size=44, subsystem=Engine (VILauncher)
    (0x0106c290, "VILauncher::PreparePowerOff"),  # size=28, subsystem=Engine (VILauncher)
    (0x0106c2b0, "VILauncher::UnpreparePowerOff"),  # size=168, subsystem=Engine (VILauncher)
    (0x0106c358, "VILauncher::LoadIrx"),  # size=252, subsystem=Engine (VILauncher)
    (0x0106c458, "VILauncher::LoadIrx2"),  # size=252, subsystem=Engine (VILauncher)
    (0x0106c558, "VILauncher::Setup"),  # size=20, subsystem=Engine (VILauncher)
    (0x0106c570, "VILauncher::Station"),  # size=188, subsystem=Engine (VILauncher)
    (0x0106c630, "VILauncher::Client"),  # size=8, subsystem=Engine (VILauncher)
    (0x0106c638, "VILauncher::UnpackAndVerify"),  # size=8, subsystem=Engine (VILauncher)
    (0x0106cf18, "GenericAPI::GenericAPICore::submitRequest"),  # size=236, subsystem=Networking
    (0x0106d008, "GenericAPI::GenericAPICore::process"),  # size=2108, subsystem=Networking
    (0x0106d848, "GenericAPI::GenericAPICore::getNextActiveConnection"),  # size=128, subsystem=Networking
    (0x0106d8c8, "GenericAPI::GenericAPICore::changeHostPort"),  # size=84, subsystem=Networking
    (0x0106d920, "VIBattleMusic::Play"),  # size=368, subsystem=Engine (VIBattleMusic)
    (0x0106da90, "VIBattleMusic::Process"),  # size=436, subsystem=Engine (VIBattleMusic)
    (0x0106dc48, "VIBattleMusic::Preload"),  # size=236, subsystem=Engine (VIBattleMusic)
    (0x0106dd38, "VIBattleMusic::Unload"),  # size=200, subsystem=Engine (VIBattleMusic)
    (0x0106de00, "VIBattleMusic::constructor"),  # size=8, subsystem=Engine (VIBattleMusic)
    (0x0106de08, "VIBattleMusic::~destructor"),  # size=84, subsystem=Engine (VIBattleMusic)
    (0x0106de60, "VIBattleMusic::Init"),  # size=52, subsystem=Engine (VIBattleMusic)
    (0x0106de98, "VIBattleMusic::Free"),  # size=64, subsystem=Engine (VIBattleMusic)
    (0x0106ded8, "VIBattleMusic::Stop"),  # size=160, subsystem=Engine (VIBattleMusic)
    (0x0106df78, "VIBattleMusic::StopNow"),  # size=144, subsystem=Engine (VIBattleMusic)
    (0x0106e110, "VIBoltHarmonic::Sample"),  # size=240, subsystem=Engine (VIBoltHarmonic)
    (0x0106e200, "VIBoltHarmonic::Update"),  # size=340, subsystem=Engine (VIBoltHarmonic)
    (0x0106e358, "VIBolt::constructor"),  # size=220, subsystem=Engine (VIBolt)
    (0x0106e438, "VIBolt::Reset"),  # size=1080, subsystem=Engine (VIBolt)
    (0x0106e870, "VIBolt::Update"),  # size=1256, subsystem=Engine (VIBolt)
    (0x0106ed58, "VILightning::constructor"),  # size=404, subsystem=Lighting
    (0x0106eef0, "VILightning::SetLocation"),  # size=548, subsystem=Lighting
    (0x0106f118, "VILightning::Update"),  # size=436, subsystem=Lighting
    (0x0106f2d0, "VILightning::Render"),  # size=612, subsystem=Lighting
    (0x0106f538, "VILightning::RenderBoltVertices"),  # size=1536, subsystem=Lighting
    (0x0106fb88, "VIBoltHarmonic::Create"),  # size=72, subsystem=Engine (VIBoltHarmonic)
    (0x0106fbd0, "VIBoltHarmonic::GenerateSamples"),  # size=236, subsystem=Engine (VIBoltHarmonic)
    (0x0106fcc0, "VILightning::~destructor"),  # size=164, subsystem=Lighting
    (0x0106fd70, "VILightning::SetCharge"),  # size=8, subsystem=Lighting
    (0x0106fd78, "VILightning::SetColor"),  # size=40, subsystem=Lighting
    (0x0106fda0, "VILightning::SetMaxBranchCount"),  # size=20, subsystem=Lighting
    (0x010700f0, "GenericAPI::GenericConnection::OnTerminated"),  # size=136, subsystem=Networking
    (0x01070178, "GenericAPI::GenericConnection::OnRoutePacket"),  # size=1892, subsystem=Networking
    (0x010708e0, "GenericAPI::GenericConnection::process"),  # size=588, subsystem=Networking
    (0x01070b30, "GenericAPI::GenericConnection::changeHostPort"),  # size=132, subsystem=Networking
    (0x01070bb8, "GenericAPI::GenericConnection::disconnect"),  # size=64, subsystem=Networking
    (0x01070bf8, "GenericAPI::GenericConnection::Send"),  # size=60, subsystem=Networking
    (0x01070c38, "VIBBox::Scale"),  # size=160, subsystem=Engine (VIBBox)
    (0x01070cd8, "VIBBox::Scale"),  # size=224, subsystem=Engine (VIBBox)
    (0x01070db8, "VIBBox::Union"),  # size=184, subsystem=Engine (VIBBox)
    (0x01070e70, "VIBBox::Union"),  # size=196, subsystem=Engine (VIBBox)
    (0x01070f38, "VIBBox::Intersect"),  # size=260, subsystem=Engine (VIBBox)
    (0x01072410, "VIBBox::Init"),  # size=112, subsystem=Engine (VIBBox)
    (0x01072480, "VIBBox::Bound"),  # size=164, subsystem=Engine (VIBBox)
    (0x01072528, "VILList::Reverse"),  # size=160, subsystem=Engine (VILList)
    (0x010725c8, "VILList::PriorityInsert"),  # size=168, subsystem=Engine (VILList)
    (0x01072670, "VILNode::constructor"),  # size=12, subsystem=Engine (VILNode)
    (0x01072680, "VILNode::Remove"),  # size=56, subsystem=Engine (VILNode)
    (0x010726b8, "VILNode::InsertAfter"),  # size=44, subsystem=Engine (VILNode)
    (0x01072758, "VILNode::SetName"),  # size=44, subsystem=Engine (VILNode)
    (0x01072788, "VILList::constructor"),  # size=20, subsystem=Engine (VILList)
    (0x010727a0, "VILList::~destructor"),  # size=44, subsystem=Engine (VILList)
    (0x010727d0, "VILList::Init"),  # size=20, subsystem=Engine (VILList)
    (0x010727e8, "VILList::AddHead"),  # size=36, subsystem=Engine (VILList)
    (0x01072810, "VILList::AddTail"),  # size=36, subsystem=Engine (VILList)
    (0x01072838, "VILList::RemHead"),  # size=64, subsystem=Engine (VILList)
    (0x01072878, "VILList::RemTail"),  # size=64, subsystem=Engine (VILList)
    (0x01072a40, "VILoader::Clear"),  # size=300, subsystem=Asset Loading
    (0x01072b70, "VILoader::Process"),  # size=432, subsystem=Asset Loading
    (0x01072d20, "VILoader::Load"),  # size=444, subsystem=Asset Loading
    (0x01072ee0, "VILoader::Release"),  # size=308, subsystem=Asset Loading
    (0x01073018, "VILoader::Find"),  # size=192, subsystem=Asset Loading
    (0x010730d8, "VILoader::Complete"),  # size=316, subsystem=Asset Loading
    (0x01073218, "VILoader::Allocate"),  # size=220, subsystem=Asset Loading
    (0x010732f8, "VILoader::constructor"),  # size=96, subsystem=Asset Loading
    (0x01073358, "VILoader::~destructor"),  # size=132, subsystem=Asset Loading
    (0x010733e0, "VILoader::Init"),  # size=160, subsystem=Asset Loading
    (0x01073480, "VILoader::Open"),  # size=80, subsystem=Asset Loading
    (0x010734d0, "VILoader::OpenResourceFile"),  # size=200, subsystem=Asset Loading
    (0x01073598, "VILoader::Close"),  # size=68, subsystem=Asset Loading
    (0x010735e0, "VILoader::CompleteAll"),  # size=132, subsystem=Asset Loading
    (0x01073668, "VILoader::AllComplete"),  # size=52, subsystem=Asset Loading
    (0x010736a0, "VILoader::ReleaseAllComplete"),  # size=188, subsystem=Asset Loading
    (0x01073760, "VILoader::IsResourceAvailable"),  # size=36, subsystem=Asset Loading
    (0x01073788, "VILoader::Load"),  # size=108, subsystem=Asset Loading
    (0x010737f8, "VILoader::Load"),  # size=24, subsystem=Asset Loading
    (0x01073810, "VILoader::Load"),  # size=44, subsystem=Asset Loading
    (0x01073840, "VILoader::IsComplete"),  # size=36, subsystem=Asset Loading
    (0x01073868, "VILoader::SetProgressCallback"),  # size=72, subsystem=Asset Loading
    (0x010738b0, "VILoader::Align"),  # size=204, subsystem=Asset Loading
    (0x01073980, "VIWadFile::SharedInit"),  # size=188, subsystem=Engine (VIWadFile)
    (0x01073a40, "VIWadFile::constructor"),  # size=44, subsystem=Engine (VIWadFile)
    (0x01073a70, "VIWadFile::~destructor"),  # size=84, subsystem=Engine (VIWadFile)
    (0x01073ac8, "VIWadFile::Init"),  # size=72, subsystem=Engine (VIWadFile)
    (0x01073b10, "VIWadFile::Init"),  # size=72, subsystem=Engine (VIWadFile)
    (0x01073b58, "VIWadFile::Free"),  # size=60, subsystem=Engine (VIWadFile)
    (0x01073b98, "VIWadFile::GetSize"),  # size=44, subsystem=Engine (VIWadFile)
    (0x01073bc8, "VIWadFile::Load"),  # size=148, subsystem=Engine (VIWadFile)
    (0x01073c60, "VIWadFile::LookupEntry"),  # size=124, subsystem=Engine (VIWadFile)
    (0x01073ce0, "VIWadFile::HashStringLowercase"),  # size=144, subsystem=Engine (VIWadFile)
    (0x01075bb0, "VIBRect::Scale"),  # size=112, subsystem=Engine (VIBRect)
    (0x01075c20, "VIBRect::Scale"),  # size=152, subsystem=Engine (VIBRect)
    (0x01075cb8, "VIBRect::Union"),  # size=120, subsystem=Engine (VIBRect)
    (0x01075d30, "VIBRect::Union"),  # size=128, subsystem=Engine (VIBRect)
    (0x01075db0, "VIBRect::Intersect"),  # size=172, subsystem=Engine (VIBRect)
    (0x01076210, "VIBRect::Bound"),  # size=116, subsystem=Engine (VIBRect)
    (0x01076288, "VIBRect::Size"),  # size=40, subsystem=Engine (VIBRect)
    (0x010762e8, "VILODSprite::Raster"),  # size=388, subsystem=Engine (VILODSprite)
    (0x01076470, "VILODSprite::Pick"),  # size=364, subsystem=Engine (VILODSprite)
    (0x010765e0, "VILODSprite::Copy"),  # size=388, subsystem=Engine (VILODSprite)
    (0x01076768, "VILODSprite::constructor"),  # size=60, subsystem=Engine (VILODSprite)
    (0x010767a8, "VILODSprite::~destructor"),  # size=100, subsystem=Engine (VILODSprite)
    (0x01076810, "VILODSprite::SetVisible"),  # size=44, subsystem=Engine (VILODSprite)
    (0x01076840, "VILODSprite::SetLevelSprite"),  # size=124, subsystem=Engine (VILODSprite)
    (0x010768c0, "VILODSprite::Collide"),  # size=128, subsystem=Engine (VILODSprite)
    (0x01076940, "VILODSprite::Collide"),  # size=128, subsystem=Engine (VILODSprite)
    (0x010769c0, "VILODSprite::QueryIntersection"),  # size=128, subsystem=Engine (VILODSprite)
    (0x01076a40, "VILODSprite::Release"),  # size=160, subsystem=Engine (VILODSprite)
    (0x01076ae0, "VIWalkCamera::Init"),  # size=116, subsystem=Engine (VIWalkCamera)
    (0x01076b58, "VIWalkCamera::SetLocation"),  # size=396, subsystem=Engine (VIWalkCamera)
    (0x01076ce8, "VIWalkCamera::Process"),  # size=912, subsystem=Engine (VIWalkCamera)
    (0x01077078, "VIWalkCamera::UpdateCameraPhysics"),  # size=812, subsystem=Engine (VIWalkCamera)
    (0x010773a8, "VIWalkCamera::MoveCamera"),  # size=1688, subsystem=Engine (VIWalkCamera)
    (0x01077a40, "VIWalkCamera::Halt"),  # size=220, subsystem=Engine (VIWalkCamera)
    (0x01077b20, "VIWalkCamera::SetOrbitAngle"),  # size=348, subsystem=Engine (VIWalkCamera)
    (0x01077c80, "VIWalkCamera::OrbitRight"),  # size=192, subsystem=Engine (VIWalkCamera)
    (0x01077d40, "VIWalkCamera::SetCamera"),  # size=540, subsystem=Engine (VIWalkCamera)
    (0x01077f60, "VIWalkCamera::InitCameraIntermediate"),  # size=384, subsystem=Engine (VIWalkCamera)
    (0x010780e0, "VIWalkCamera::FindOrbitAngle"),  # size=756, subsystem=Engine (VIWalkCamera)
    (0x010783d8, "VIWalkCamera::FindBestOrbitAngle"),  # size=848, subsystem=Engine (VIWalkCamera)
    (0x01078728, "VIWalkCamera::Init"),  # size=328, subsystem=Engine (VIWalkCamera)
    (0x01078870, "VIWalkCamera::SetCameraMode"),  # size=100, subsystem=Engine (VIWalkCamera)
    (0x010788d8, "VIWalkCamera::SetDefOrbitPitchAngle"),  # size=24, subsystem=Engine (VIWalkCamera)
    (0x010788f0, "VIWalkCamera::SetOrbitPitchAngle"),  # size=16, subsystem=Engine (VIWalkCamera)
    (0x01078900, "VIWalkCamera::SetOrbitDistance"),  # size=48, subsystem=Engine (VIWalkCamera)
    (0x01078930, "VIWalkCamera::SetOrbitAngleBehind"),  # size=40, subsystem=Engine (VIWalkCamera)
    (0x01078958, "VIWalkCamera::ChooseOrbitAngle"),  # size=96, subsystem=Engine (VIWalkCamera)
    (0x010789b8, "VIWalkCamera::OrbitIn"),  # size=116, subsystem=Engine (VIWalkCamera)
    (0x01078a30, "VIWalkCamera::ClearCameraForces"),  # size=32, subsystem=Engine (VIWalkCamera)
    (0x01079760, "VICameraEffect::Apply"),  # size=1276, subsystem=Camera
    (0x01079c60, "VICameraEffect::constructor"),  # size=88, subsystem=Camera
    (0x01079cb8, "VICameraEffect::~destructor"),  # size=44, subsystem=Camera
    (0x01079ce8, "VICameraEffect::Reset"),  # size=24, subsystem=Camera
    (0x01079d00, "VICameraEffect::Shake"),  # size=20, subsystem=Camera
    (0x01079d18, "VICameraEffect::ShakeTerp"),  # size=64, subsystem=Camera
    (0x01079d58, "VICameraEffect::BeginManual"),  # size=120, subsystem=Camera
    (0x01079dd8, "VICameraEffect::SetManualXyz"),  # size=32, subsystem=Camera
    (0x01079e00, "VICameraEffect::SetManualHpr"),  # size=32, subsystem=Camera
    (0x01079e28, "VICameraEffect::EndManual"),  # size=60, subsystem=Camera
    (0x01079e68, "VICameraEffect::Update"),  # size=208, subsystem=Camera
    (0x01079f38, "VIWalkControl::constructor"),  # size=336, subsystem=Engine (VIWalkControl)
    (0x0107a088, "VIWalkControl::SetLocation"),  # size=564, subsystem=Engine (VIWalkControl)
    (0x0107a2c0, "VIWalkControl::SetPitchRange"),  # size=212, subsystem=Engine (VIWalkControl)
    (0x0107a398, "VIWalkControl::Process"),  # size=800, subsystem=Engine (VIWalkControl)
    (0x0107a6b8, "VIWalkControl::Walk"),  # size=336, subsystem=Engine (VIWalkControl)
    (0x0107a808, "VIWalkControl::Run"),  # size=532, subsystem=Engine (VIWalkControl)
    (0x0107aa20, "VIWalkControl::Move"),  # size=140, subsystem=Engine (VIWalkControl)
    (0x0107aab0, "VIWalkControl::ViewRelativeMove"),  # size=668, subsystem=Engine (VIWalkControl)
    (0x0107ad50, "VIWalkControl::ViewRelativeWalk"),  # size=628, subsystem=Engine (VIWalkControl)
    (0x0107afc8, "VIWalkControl::SetTargetHeading"),  # size=220, subsystem=Engine (VIWalkControl)
    (0x0107b0a8, "VIWalkControl::TurnLeft"),  # size=164, subsystem=Engine (VIWalkControl)
    (0x0107b150, "VIWalkControl::PitchDown"),  # size=312, subsystem=Engine (VIWalkControl)
    (0x0107b288, "VIWalkControl::SetUpdatePhysics"),  # size=824, subsystem=Engine (VIWalkControl)
    (0x0107b5c0, "VIWalkControl::UpdateSprite"),  # size=352, subsystem=Engine (VIWalkControl)
    (0x0107b8e8, "VIWalkControl::UpdatePhysics"),  # size=1236, subsystem=Engine (VIWalkControl)
    (0x0107bdc0, "VIWalkControl::Move"),  # size=2340, subsystem=Engine (VIWalkControl)
    (0x0107c6e8, "VIWalkControl::UpdateDirections"),  # size=304, subsystem=Engine (VIWalkControl)
    (0x0107c818, "VIWalkControl::UpdateLocomotion"),  # size=708, subsystem=Engine (VIWalkControl)
    (0x0107cae0, "VIWalkControl::CalcFit"),  # size=676, subsystem=Engine (VIWalkControl)
    (0x0107cd88, "VIWalkControl::CalcFloor"),  # size=392, subsystem=Engine (VIWalkControl)
    (0x0107cf10, "VIWalkControl::AutoPitch"),  # size=232, subsystem=Engine (VIWalkControl)
    (0x0107cff8, "VIWalkControl::InitParms"),  # size=372, subsystem=Engine (VIWalkControl)
    (0x0107d170, "VIWalkControl::InitIntermediate"),  # size=332, subsystem=Engine (VIWalkControl)
    (0x0107d320, "VIWalkControl::~destructor"),  # size=44, subsystem=Engine (VIWalkControl)
    (0x0107d350, "VIWalkControl::Init"),  # size=108, subsystem=Engine (VIWalkControl)
    (0x0107d3c0, "VIWalkControl::ClearForces"),  # size=44, subsystem=Engine (VIWalkControl)
    (0x0107d3f0, "VIWalkControl::SwimUp"),  # size=108, subsystem=Engine (VIWalkControl)
    (0x0107d460, "VIWalkControl::IsUnderWater"),  # size=20, subsystem=Engine (VIWalkControl)
    (0x0107d478, "VIWalkControl::IsUnderLiquid"),  # size=40, subsystem=Engine (VIWalkControl)
    (0x0107d4a0, "VIWalkControl::IsAtLiquidSurface"),  # size=16, subsystem=Engine (VIWalkControl)
    (0x0107d4b0, "VIWalkControl::IsInLava"),  # size=16, subsystem=Engine (VIWalkControl)
    (0x0107d4c0, "VIWalkControl::IsInSlime"),  # size=16, subsystem=Engine (VIWalkControl)
    (0x0107d4d0, "VIWalkControl::IsInMud"),  # size=16, subsystem=Engine (VIWalkControl)
    (0x0107d530, "VIWalkFloorFilter::FilterActor"),  # size=40, subsystem=Engine (VIWalkFloorFilter)
    (0x010858d8, "VICamera::Init"),  # size=444, subsystem=Camera
    (0x010867c8, "VICamera::CalcAxes"),  # size=532, subsystem=Camera
    (0x010869e0, "VICamera::Update"),  # size=804, subsystem=Camera
    (0x01086d08, "VICamera::CalcFrustum"),  # size=1188, subsystem=Camera
    (0x010871b0, "VICamera::__cl"),  # size=172, subsystem=Camera
    (0x01087260, "VICamera::__cl"),  # size=176, subsystem=Camera
    (0x01087310, "VICamera::__cl"),  # size=48, subsystem=Camera
    (0x01087340, "VICamera::__cl"),  # size=40, subsystem=Camera
    (0x01087488, "VIWidget::Render"),  # size=2036, subsystem=Engine (VIWidget)
    (0x01087c80, "VIWidget::RenderOverlay"),  # size=1188, subsystem=Engine (VIWidget)
    (0x01088128, "VIWidget::constructor"),  # size=32, subsystem=Engine (VIWidget)
    (0x01088148, "VIWidget::~destructor"),  # size=44, subsystem=Engine (VIWidget)
    (0x01088178, "VIWidget::InitButton"),  # size=128, subsystem=Engine (VIWidget)
    (0x010881f8, "VIWidget::InitEdit"),  # size=160, subsystem=Engine (VIWidget)
    (0x01088298, "VIWidget::InitCheckbox"),  # size=120, subsystem=Engine (VIWidget)
    (0x01088310, "VIWidget::InitCombo"),  # size=204, subsystem=Engine (VIWidget)
    (0x010883e0, "VIWidget::InitCombo"),  # size=216, subsystem=Engine (VIWidget)
    (0x010884b8, "VIWidget::Free"),  # size=56, subsystem=Engine (VIWidget)
    (0x010884f0, "VIWidget::Reset"),  # size=8, subsystem=Engine (VIWidget)
    (0x01088508, "VIWidget::SetLabel"),  # size=36, subsystem=Engine (VIWidget)
    (0x01088538, "VIWidget::SetValue"),  # size=120, subsystem=Engine (VIWidget)
    (0x010885b8, "VIWidget::SetState"),  # size=8, subsystem=Engine (VIWidget)
    (0x010885d0, "VIWidget::SetSelection"),  # size=8, subsystem=Engine (VIWidget)
    (0x010885e0, "VIWidget::SetListSelection"),  # size=32, subsystem=Engine (VIWidget)
    (0x01088608, "VIWidget::SetError"),  # size=8, subsystem=Engine (VIWidget)
    (0x01088610, "VIWidget::FitString"),  # size=264, subsystem=Engine (VIWidget)
    (0x0108a168, "VICapsule::PointInSolid"),  # size=552, subsystem=Engine (VICapsule)
    (0x0108a390, "VIMatrix33::Translate"),  # size=88, subsystem=Engine (VIMatrix33)
    (0x0108a3e8, "VIMatrix33::Scale"),  # size=84, subsystem=Engine (VIMatrix33)
    (0x0108a440, "VIMatrix33::Scale"),  # size=92, subsystem=Engine (VIMatrix33)
    (0x0108a4a0, "VIMatrix33::Rotate"),  # size=160, subsystem=Engine (VIMatrix33)
    (0x0108a540, "VIMatrix33::Transform"),  # size=140, subsystem=Engine (VIMatrix33)
    (0x0108a5d0, "VIMatrix33::Transform"),  # size=176, subsystem=Engine (VIMatrix33)
    (0x0108a680, "VIMatrix33::Mul"),  # size=452, subsystem=Engine (VIMatrix33)
    (0x0108a848, "VIMatrix33::Invert"),  # size=772, subsystem=Engine (VIMatrix33)
    (0x0108ab50, "VIMatrix33::Transpose"),  # size=128, subsystem=Engine (VIMatrix33)
    (0x0108ace0, "VIMatrix33::constructor"),  # size=64, subsystem=Engine (VIMatrix33)
    (0x0108ad20, "VIMatrix33::constructor"),  # size=144, subsystem=Engine (VIMatrix33)
    (0x0108adb0, "VIMatrix33::__as"),  # size=96, subsystem=Engine (VIMatrix33)
    (0x0108ae10, "VIMatrix33::~destructor"),  # size=44, subsystem=Engine (VIMatrix33)
    (0x0108ae40, "VIMatrix33::Identity"),  # size=56, subsystem=Engine (VIMatrix33)
    (0x0108ae78, "VIMatrix33::Zero"),  # size=52, subsystem=Engine (VIMatrix33)
    (0x0108aeb0, "VIMatrix33::Add"),  # size=128, subsystem=Engine (VIMatrix33)
    (0x0108af30, "VIMatrix33::Add"),  # size=172, subsystem=Engine (VIMatrix33)
    (0x0108afe0, "VIMatrix33::Mul"),  # size=128, subsystem=Engine (VIMatrix33)
    (0x0108b060, "VIMatrix33::Transpose"),  # size=96, subsystem=Engine (VIMatrix33)
    (0x0108b0c0, "VIMatrix33::SwapRows"),  # size=92, subsystem=Engine (VIMatrix33)
    (0x0108b180, "VIMatrix33::Debug"),  # size=8, subsystem=Engine (VIMatrix33)
    (0x0108b188, "VICollBuffer::constructor"),  # size=96, subsystem=Engine (VICollBuffer)
    (0x0108b1e8, "VICollBuffer::Vertex"),  # size=248, subsystem=Engine (VICollBuffer)
    (0x0108b2e0, "VICollBuffer::End"),  # size=172, subsystem=Engine (VICollBuffer)
    (0x0108b390, "VICollBuffer::CalcBVolumes"),  # size=1152, subsystem=Engine (VICollBuffer)
    (0x0108b810, "VICollBuffer::CalcDataSize"),  # size=232, subsystem=Engine (VICollBuffer)
    (0x0108b8f8, "VICollBuffer::~destructor"),  # size=84, subsystem=Engine (VICollBuffer)
    (0x0108b950, "VICollBuffer::Init"),  # size=144, subsystem=Engine (VICollBuffer)
    (0x0108b9e0, "VICollBuffer::Clear"),  # size=124, subsystem=Engine (VICollBuffer)
    (0x0108ba60, "VICollBuffer::Lock"),  # size=32, subsystem=Engine (VICollBuffer)
    (0x0108ba80, "VICollBuffer::Unlock"),  # size=28, subsystem=Engine (VICollBuffer)
    (0x0108baa0, "VICollBuffer::SetPacking"),  # size=80, subsystem=Engine (VICollBuffer)
    (0x0108baf0, "VICollBuffer::BeginPrimGroup"),  # size=44, subsystem=Engine (VICollBuffer)
    (0x0108bb20, "VICollBuffer::EndPrimGroup"),  # size=20, subsystem=Engine (VICollBuffer)
    (0x0108bb38, "VICollBuffer::Begin"),  # size=116, subsystem=Engine (VICollBuffer)
    (0x0108bbb0, "VICollBuffer::Vertex"),  # size=124, subsystem=Engine (VICollBuffer)
    (0x0108bc30, "VICollBuffer::VertexGroup"),  # size=12, subsystem=Engine (VICollBuffer)
    (0x0108bc40, "VICollBuffer::FloraType"),  # size=12, subsystem=Engine (VICollBuffer)
    (0x0108bc50, "VICollBuffer::Allocate"),  # size=72, subsystem=Engine (VICollBuffer)
    (0x0108bf38, "VIClipper::Clip"),  # size=636, subsystem=Engine (VIClipper)
    (0x0108c1b8, "VIClipper::Init"),  # size=92, subsystem=Engine (VIClipper)
    (0x0108c218, "VIClipper::Clear"),  # size=80, subsystem=Engine (VIClipper)
    (0x0108c268, "VIMatrix44D::constructor"),  # size=212, subsystem=Engine (VIMatrix44D)
    (0x0108c340, "VIMatrix44D::__as"),  # size=368, subsystem=Engine (VIMatrix44D)
    (0x0108c4b0, "VIMatrix44D::Translate"),  # size=136, subsystem=Engine (VIMatrix44D)
    (0x0108c538, "VIMatrix44D::Scale"),  # size=132, subsystem=Engine (VIMatrix44D)
    (0x0108c5c0, "VIMatrix44D::Scale"),  # size=144, subsystem=Engine (VIMatrix44D)
    (0x0108c650, "VIMatrix44D::RotateX"),  # size=244, subsystem=Engine (VIMatrix44D)
    (0x0108c748, "VIMatrix44D::RotateY"),  # size=244, subsystem=Engine (VIMatrix44D)
    (0x0108c840, "VIMatrix44D::RotateZ"),  # size=236, subsystem=Engine (VIMatrix44D)
    (0x0108c930, "VIMatrix44D::RotateHPR"),  # size=708, subsystem=Engine (VIMatrix44D)
    (0x0108cbf8, "VIMatrix44D::Rotate"),  # size=868, subsystem=Engine (VIMatrix44D)
    (0x0108cf60, "VIMatrix44D::UnitRotate"),  # size=740, subsystem=Engine (VIMatrix44D)
    (0x0108d248, "VIMatrix44D::Transform"),  # size=888, subsystem=Engine (VIMatrix44D)
    (0x0108d5c0, "VIMatrix44D::Transform"),  # size=920, subsystem=Engine (VIMatrix44D)
    (0x0108d958, "VIMatrix44D::Transform"),  # size=900, subsystem=Engine (VIMatrix44D)
    (0x0108dce0, "VIMatrix44D::Transform"),  # size=904, subsystem=Engine (VIMatrix44D)
    (0x0108f158, "VIMatrix44D::Add"),  # size=444, subsystem=Engine (VIMatrix44D)
    (0x0108f318, "VIMatrix44D::Add"),  # size=512, subsystem=Engine (VIMatrix44D)
    (0x0108f518, "VIMatrix44D::Mul"),  # size=444, subsystem=Engine (VIMatrix44D)
    (0x0108f6d8, "VIMatrix44D::Mul"),  # size=2888, subsystem=Engine (VIMatrix44D)
    (0x01091230, "VIMatrix44D::Invert"),  # size=1076, subsystem=Engine (VIMatrix44D)
    (0x01091668, "VIMatrix44D::InvertAffine"),  # size=1844, subsystem=Engine (VIMatrix44D)
    (0x01091da0, "VIMatrix44D::Transpose"),  # size=116, subsystem=Engine (VIMatrix44D)
    (0x01092340, "VIMatrix44D::constructor"),  # size=64, subsystem=Engine (VIMatrix44D)
    (0x01092380, "VIMatrix44D::__as"),  # size=164, subsystem=Engine (VIMatrix44D)
    (0x01092428, "VIMatrix44D::~destructor"),  # size=44, subsystem=Engine (VIMatrix44D)
    (0x01092458, "VIMatrix44D::Identity"),  # size=60, subsystem=Engine (VIMatrix44D)
    (0x01092498, "VIMatrix44D::Zero"),  # size=88, subsystem=Engine (VIMatrix44D)
    (0x010924f0, "VIMatrix44D::Transpose"),  # size=88, subsystem=Engine (VIMatrix44D)
    (0x01092548, "VIMatrix44D::SwapRows"),  # size=92, subsystem=Engine (VIMatrix44D)
    (0x01092600, "VIMatrix44D::Debug"),  # size=8, subsystem=Engine (VIMatrix44D)
    (0x01092608, "VICollide::constructor"),  # size=212, subsystem=Collision
    (0x010926e0, "VICollide::CollideObj"),  # size=340, subsystem=Collision
    (0x01092838, "VICollide::CollideObj"),  # size=316, subsystem=Collision
    (0x01092978, "VICollide::CollideObj"),  # size=340, subsystem=Collision
    (0x01092ad0, "VICollide::QueryObj"),  # size=184, subsystem=Collision
    (0x01092b88, "VICollide::CollideBufferV"),  # size=868, subsystem=Collision
    (0x01092ef0, "VICollide::CollideBufferPackV"),  # size=948, subsystem=Collision
    (0x010932a8, "VICollide::CollideBufferPackVGF"),  # size=1140, subsystem=Collision
    (0x01093720, "VICollide::CollideBufferV"),  # size=868, subsystem=Collision
    (0x01093a88, "VICollide::CollideBufferPackV"),  # size=948, subsystem=Collision
    (0x01093e40, "VICollide::CollideBufferPackVGF"),  # size=1140, subsystem=Collision
    (0x010942b8, "VICollide::Collide"),  # size=880, subsystem=Collision
    (0x01094628, "VICollide::Collide"),  # size=1396, subsystem=Collision
    (0x01094ba0, "VICollide::Collide"),  # size=452, subsystem=Collision
    (0x01094d68, "VICollide::Collide"),  # size=552, subsystem=Collision
    (0x01094f90, "VICollide::Collide"),  # size=476, subsystem=Collision
    (0x01095170, "VICollide::Collide"),  # size=988, subsystem=Collision
    (0x01095550, "VICollide::PointInTriangle"),  # size=716, subsystem=Collision
    (0x01095820, "VICollide::Cull"),  # size=376, subsystem=Collision
    (0x01095998, "VICollide::Cull"),  # size=232, subsystem=Collision
    (0x01095a80, "VICollide::Cull"),  # size=224, subsystem=Collision
    (0x01095b60, "VICollide::Cull"),  # size=224, subsystem=Collision
    (0x01095c40, "VICollide::Collide"),  # size=476, subsystem=Collision
    (0x01095e20, "VICollide::CollideNoCaps"),  # size=964, subsystem=Collision
    (0x010961e8, "VICollide::QueryBufferV"),  # size=728, subsystem=Collision
    (0x010964c0, "VICollide::QueryBufferPackV"),  # size=928, subsystem=Collision
    (0x01096860, "VICollide::QueryBufferPackVGF"),  # size=1096, subsystem=Collision
    (0x01096ca8, "VICollide::DebugResources"),  # size=216, subsystem=Collision
    (0x01096d80, "VICollide::~destructor"),  # size=116, subsystem=Collision
    (0x01096df8, "VICollide::Init"),  # size=52, subsystem=Collision
    (0x01096e30, "VICollide::Close"),  # size=44, subsystem=Collision
    (0x01096e60, "VICollide::Reset"),  # size=76, subsystem=Collision
    (0x01096eb0, "VICollide::Clear"),  # size=144, subsystem=Collision
    (0x01096f40, "VICollide::CreateCollBuffer"),  # size=140, subsystem=Collision
    (0x01096fd0, "VICollide::CollBuffer"),  # size=28, subsystem=Collision
    (0x01096ff0, "VICollide::ShareCollBuffer"),  # size=44, subsystem=Collision
    (0x01097020, "VICollide::ReleaseCollBuffer"),  # size=108, subsystem=Collision
    (0x01097090, "VICollide::SetWorld"),  # size=68, subsystem=Collision
    (0x010970e0, "VICollide::SetPreTranslations"),  # size=48, subsystem=Collision
    (0x01097110, "VICollide::Collide"),  # size=104, subsystem=Collision
    (0x01097178, "VICollide::Collide"),  # size=104, subsystem=Collision
    (0x010971e0, "VICollide::Query"),  # size=104, subsystem=Collision
    (0x01098140, "VIClipStack::Init"),  # size=144, subsystem=Engine (VIClipStack)
    (0x010981d0, "VIClipStack::PushBBox"),  # size=920, subsystem=Engine (VIClipStack)
    (0x01098568, "VIClipStack::PushFrustum"),  # size=452, subsystem=Engine (VIClipStack)
    (0x01098730, "VIClipStack::PushPortal"),  # size=712, subsystem=Engine (VIClipStack)
    (0x010989f8, "VIClipStack::PushPortal"),  # size=776, subsystem=Engine (VIClipStack)
    (0x01098d00, "VIClipStack::PushTranslatedFrustum"),  # size=680, subsystem=Engine (VIClipStack)
    (0x01098fa8, "VIClipStack::PushTranslatedVolume"),  # size=328, subsystem=Engine (VIClipStack)
    (0x010990f0, "VIClipStack::ClipByTop"),  # size=688, subsystem=Engine (VIClipStack)
    (0x010993a0, "VIClipStack::CullByTop"),  # size=268, subsystem=Engine (VIClipStack)
    (0x010994b0, "VIClipStack::Clear"),  # size=128, subsystem=Engine (VIClipStack)
    (0x01099530, "VIClipStack::Reset"),  # size=20, subsystem=Engine (VIClipStack)
    (0x01099548, "VIClipStack::Pop"),  # size=64, subsystem=Engine (VIClipStack)
    (0x01099588, "VIClipStack::CullByTop"),  # size=152, subsystem=Engine (VIClipStack)
    (0x01099620, "VIClipStack::GetEntry"),  # size=84, subsystem=Engine (VIClipStack)
    (0x01099678, "VIClipStack::GetTop"),  # size=92, subsystem=Engine (VIClipStack)
    (0x010996d8, "VIMatrix44::RotateHPR"),  # size=356, subsystem=Engine (VIMatrix44)
    (0x01099840, "VIMatrix44::Rotate"),  # size=236, subsystem=Engine (VIMatrix44)
    (0x01099930, "VIMatrix44::UnitRotate"),  # size=192, subsystem=Engine (VIMatrix44)
    (0x010999f0, "VIMatrix44::Transform"),  # size=436, subsystem=Engine (VIMatrix44)
    (0x01099ba8, "VIMatrix44::Transform"),  # size=480, subsystem=Engine (VIMatrix44)
    (0x01099d88, "VIMatrix44::Transform"),  # size=240, subsystem=Engine (VIMatrix44)
    (0x01099e78, "VIMatrix44::Transform"),  # size=300, subsystem=Engine (VIMatrix44)
    (0x0109a910, "VIMatrix44::Add"),  # size=296, subsystem=Engine (VIMatrix44)
    (0x0109ab58, "VIMatrix44::Transpose"),  # size=108, subsystem=Engine (VIMatrix44)
    (0x0109abc8, "VIMatrix44::__as"),  # size=88, subsystem=Engine (VIMatrix44)
    (0x0109ac20, "VIMatrix44::~destructor"),  # size=44, subsystem=Engine (VIMatrix44)
    (0x0109ac50, "VIMatrix44::Translate"),  # size=72, subsystem=Engine (VIMatrix44)
    (0x0109ac98, "VIMatrix44::Scale"),  # size=60, subsystem=Engine (VIMatrix44)
    (0x0109acd8, "VIMatrix44::Scale"),  # size=72, subsystem=Engine (VIMatrix44)
    (0x0109ad20, "VIMatrix44::RotateX"),  # size=100, subsystem=Engine (VIMatrix44)
    (0x0109ad88, "VIMatrix44::RotateY"),  # size=100, subsystem=Engine (VIMatrix44)
    (0x0109adf0, "VIMatrix44::RotateZ"),  # size=100, subsystem=Engine (VIMatrix44)
    (0x0109aee8, "VIMatrix44::Add"),  # size=220, subsystem=Engine (VIMatrix44)
    (0x0109afc8, "VIMatrix44::Mul"),  # size=112, subsystem=Engine (VIMatrix44)
    (0x0109b180, "VIMatrix44::Transpose"),  # size=88, subsystem=Engine (VIMatrix44)
    (0x0109b1d8, "VIMatrix44::SwapRows"),  # size=92, subsystem=Engine (VIMatrix44)
    (0x0109b348, "VIMatrix44::Debug"),  # size=8, subsystem=Engine (VIMatrix44)
    (0x0109b350, "VIWindowManager::Update"),  # size=680, subsystem=Engine (VIWindowManager)
    (0x0109b5f8, "VIWindowManager::constructor"),  # size=48, subsystem=Engine (VIWindowManager)
    (0x0109b628, "VIWindowManager::~destructor"),  # size=100, subsystem=Engine (VIWindowManager)
    (0x0109b690, "VIWindowManager::Init"),  # size=48, subsystem=Engine (VIWindowManager)
    (0x0109b6c0, "VIWindowManager::Free"),  # size=8, subsystem=Engine (VIWindowManager)
    (0x0109b6d0, "VIWindowManager::SetRoot"),  # size=8, subsystem=Engine (VIWindowManager)
    (0x0109bf88, "VICollRay::constructor"),  # size=100, subsystem=Engine (VICollRay)
    (0x0109bff0, "VICollRay::Init"),  # size=468, subsystem=Engine (VICollRay)
    (0x0109c1c8, "VICollRay::GetHitPoint"),  # size=84, subsystem=Engine (VICollRay)
    (0x0109c220, "VICollRay::Skitter"),  # size=776, subsystem=Engine (VICollRay)
    (0x0109c528, "VICollRay::Precalc"),  # size=232, subsystem=Engine (VICollRay)
    (0x0109c610, "VICollRay::Init"),  # size=164, subsystem=Engine (VICollRay)
    (0x0109c6b8, "VICollRay::GetHitNormal"),  # size=8, subsystem=Engine (VICollRay)
    (0x0109c6c0, "VICollRay::GetHitDistance"),  # size=16, subsystem=Engine (VICollRay)
    (0x0109c6d0, "VICollRay::GetHitTime"),  # size=8, subsystem=Engine (VICollRay)
    (0x0109c6d8, "VIWndMcErr::OnMessage"),  # size=260, subsystem=Engine (VIWndMcErr)
    (0x0109c7e0, "VIWndMcErr::ProcessScreen"),  # size=676, subsystem=Engine (VIWndMcErr)
    (0x0109ca88, "VIWndMcErr::ProcessScreen04"),  # size=648, subsystem=Engine (VIWndMcErr)
    (0x0109cd10, "VIWndMcErr::ProcessScreen10"),  # size=460, subsystem=Engine (VIWndMcErr)
    (0x0109cee0, "VIWndMcErr::ProcessScreen11"),  # size=652, subsystem=Engine (VIWndMcErr)
    (0x0109d170, "VIWndMcErr::ProcessScreen12"),  # size=672, subsystem=Engine (VIWndMcErr)
    (0x0109d410, "VIWndMcErr::ProcessScreen15"),  # size=628, subsystem=Engine (VIWndMcErr)
    (0x0109d688, "VIWndMcErr::ProcessScreen16"),  # size=628, subsystem=Engine (VIWndMcErr)
    (0x0109d900, "VIWndMcErr::ProcessScreen17"),  # size=672, subsystem=Engine (VIWndMcErr)
    (0x0109dba0, "VIWndMcErr::ProcessScreen20"),  # size=432, subsystem=Engine (VIWndMcErr)
    (0x0109dd50, "VIWndMcErr::ProcessScreen25"),  # size=388, subsystem=Engine (VIWndMcErr)
    (0x0109ded8, "VIWndMcErr::ProcessScreen30"),  # size=496, subsystem=Engine (VIWndMcErr)
    (0x0109e0c8, "VIWndMcErr::ProcessScreen50"),  # size=496, subsystem=Engine (VIWndMcErr)
    (0x0109e2b8, "VIWndMcErr::ProcessScreen52"),  # size=460, subsystem=Engine (VIWndMcErr)
    (0x0109e488, "VIWndMcErr::ProcessScreen54"),  # size=432, subsystem=Engine (VIWndMcErr)
    (0x0109e638, "VIWndMcErr::ProcessScreen60"),  # size=524, subsystem=Engine (VIWndMcErr)
    (0x0109e848, "VIWndMcErr::ProcessScreen61"),  # size=620, subsystem=Engine (VIWndMcErr)
    (0x0109eab8, "VIWndMcErr::ProcessScreen62"),  # size=860, subsystem=Engine (VIWndMcErr)
    (0x0109ee18, "VIWndMcErr::ProcessScreen63"),  # size=676, subsystem=Engine (VIWndMcErr)
    (0x0109f0c0, "VIWndMcErr::ProcessScreen64"),  # size=588, subsystem=Engine (VIWndMcErr)
    (0x0109f310, "VIWndMcErr::DrawPrompt"),  # size=516, subsystem=Engine (VIWndMcErr)
    (0x0109f838, "VIWndMcErr::constructor"),  # size=76, subsystem=Engine (VIWndMcErr)
    (0x0109f888, "VIWndMcErr::~destructor"),  # size=124, subsystem=Engine (VIWndMcErr)
    (0x0109f908, "VIWndMcErr::Init"),  # size=52, subsystem=Engine (VIWndMcErr)
    (0x0109f940, "VIWndMcErr::Free"),  # size=32, subsystem=Engine (VIWndMcErr)
    (0x0109f960, "VIWndMcErr::OnDrawSelf"),  # size=112, subsystem=Engine (VIWndMcErr)
    (0x0109f9d0, "VIWndMcErr::OnKeyDown"),  # size=76, subsystem=Engine (VIWndMcErr)
    (0x0109fa20, "VIWndMcErr::OnKeyUp"),  # size=76, subsystem=Engine (VIWndMcErr)
    (0x0109fa70, "VIWndMcErr::GotoScreen"),  # size=68, subsystem=Engine (VIWndMcErr)
    (0x0109fab8, "VIWndMcErr::ExitMcErr"),  # size=160, subsystem=Engine (VIWndMcErr)
    (0x0109fe10, "VIWndCombo::OnKeyDown"),  # size=280, subsystem=Engine (VIWndCombo)
    (0x0109ff28, "VIWndCombo::constructor"),  # size=48, subsystem=Engine (VIWndCombo)
    (0x0109ff58, "VIWndCombo::~destructor"),  # size=100, subsystem=Engine (VIWndCombo)
    (0x0109ffc0, "VIWndCombo::Init"),  # size=72, subsystem=Engine (VIWndCombo)
    (0x010a0008, "VIWndCombo::Free"),  # size=8, subsystem=Engine (VIWndCombo)
    (0x010a0010, "VIWndCombo::OnDrawSelf"),  # size=76, subsystem=Engine (VIWndCombo)
    (0x010a0060, "VIWndCombo::OnKeyUp"),  # size=8, subsystem=Engine (VIWndCombo)
    (0x010a0068, "VIWndCombo::OnMessage"),  # size=96, subsystem=Engine (VIWndCombo)
    (0x010a00c8, "VIWndCombo::Widget"),  # size=8, subsystem=Engine (VIWndCombo)
    (0x010a00d0, "VIWndCombo::OnSelect"),  # size=8, subsystem=Engine (VIWndCombo)
    (0x010a0538, "VICollSphere::Init"),  # size=548, subsystem=Engine (VICollSphere)
    (0x010a0760, "VICollSphere::Precalc"),  # size=280, subsystem=Engine (VICollSphere)
    (0x010a0878, "VICollSphere::constructor"),  # size=20, subsystem=Engine (VICollSphere)
    (0x010a0890, "VICollSphere::Init"),  # size=168, subsystem=Engine (VICollSphere)
    (0x010a0938, "VINameSprite::Raster"),  # size=548, subsystem=Engine (VINameSprite)
    (0x010a0b60, "VINameSprite::Copy"),  # size=328, subsystem=Engine (VINameSprite)
    (0x010a0ca8, "VINameSprite::RasterDeferred"),  # size=568, subsystem=Engine (VINameSprite)
    (0x010a1000, "VINameSprite::constructor"),  # size=80, subsystem=Engine (VINameSprite)
    (0x010a1050, "VINameSprite::~destructor"),  # size=108, subsystem=Engine (VINameSprite)
    (0x010a10c0, "VINameSprite::Init"),  # size=160, subsystem=Engine (VINameSprite)
    (0x010a1160, "VINameSprite::Clear"),  # size=68, subsystem=Engine (VINameSprite)
    (0x010a11a8, "VINameSprite::SetName"),  # size=52, subsystem=Engine (VINameSprite)
    (0x010a11e0, "VINameSprite::SetColor"),  # size=40, subsystem=Engine (VINameSprite)
    (0x010a1208, "VINameSprite::Collide"),  # size=8, subsystem=Engine (VINameSprite)
    (0x010a1210, "VINameSprite::Collide"),  # size=8, subsystem=Engine (VINameSprite)
    (0x010a1218, "VINameSprite::Pick"),  # size=8, subsystem=Engine (VINameSprite)
    (0x010a1220, "VINameSprite::Release"),  # size=132, subsystem=Engine (VINameSprite)
    (0x010a1318, "VIWndConnect::OnDrawSelf"),  # size=2828, subsystem=Engine (VIWndConnect)
    (0x010a1e28, "VIWndConnect::OnKeyDown"),  # size=608, subsystem=Engine (VIWndConnect)
    (0x010a2088, "VIWndConnect::OnMessage"),  # size=544, subsystem=Engine (VIWndConnect)
    (0x010a22a8, "VIWndConnect::BeginConnect"),  # size=824, subsystem=Engine (VIWndConnect)
    (0x010a25e0, "VIWndConnect::BringUpNetwork"),  # size=1056, subsystem=Engine (VIWndConnect)
    (0x010a2a00, "VIWndConnect::constructor"),  # size=120, subsystem=Engine (VIWndConnect)
    (0x010a2a78, "VIWndConnect::~destructor"),  # size=164, subsystem=Engine (VIWndConnect)
    (0x010a2b20, "VIWndConnect::Init"),  # size=100, subsystem=Engine (VIWndConnect)
    (0x010a2b88, "VIWndConnect::Free"),  # size=48, subsystem=Engine (VIWndConnect)
    (0x010a2bb8, "VIWndConnect::OnKeyUp"),  # size=8, subsystem=Engine (VIWndConnect)
    (0x010a2bc0, "VIWndConnect::EndConnect"),  # size=48, subsystem=Engine (VIWndConnect)
    (0x010a3788, "VINetworkStatus::Initialize"),  # size=204, subsystem=Engine (VINetworkStatus)
    (0x010a3858, "VINetworkStatus::constructor"),  # size=68, subsystem=Engine (VINetworkStatus)
    (0x010a38a0, "VINetworkStatus::~destructor"),  # size=172, subsystem=Engine (VINetworkStatus)
    (0x010a3950, "VINetworkStatus::CheckNetwork"),  # size=184, subsystem=Engine (VINetworkStatus)
    (0x010a4378, "VICSFFile::Compress"),  # size=1136, subsystem=Engine (VICSFFile)
    (0x010a47e8, "VICSFFile::Parse"),  # size=384, subsystem=Engine (VICSFFile)
    (0x010a4968, "VICSFFile::Decompress"),  # size=628, subsystem=Engine (VICSFFile)
    (0x010a4be0, "VICSFFile::constructor"),  # size=12, subsystem=Engine (VICSFFile)
    (0x010a4bf0, "VICSFFile::Parse"),  # size=192, subsystem=Engine (VICSFFile)
    (0x010a4cb0, "VICSFFile::Parse"),  # size=212, subsystem=Engine (VICSFFile)
    (0x010a4d88, "VICSFFile::SetProgressCallback"),  # size=12, subsystem=Engine (VICSFFile)
    (0x010a4d98, "VIObjFile::PostOpen"),  # size=320, subsystem=Asset Loading
    (0x010a4ed8, "VIObjFile::Append"),  # size=1028, subsystem=Asset Loading
    (0x010a52e0, "VIObjFile::WriteFileHeader"),  # size=308, subsystem=Asset Loading
    (0x010a5418, "VIObjFile::ReadFileHeader"),  # size=216, subsystem=Asset Loading
    (0x010a54f0, "VIObjFile::WriteBegin"),  # size=540, subsystem=Asset Loading
    (0x010a5710, "VIObjFile::WriteEnd"),  # size=452, subsystem=Asset Loading
    (0x010a58d8, "VIObjFile::ReadBegin"),  # size=468, subsystem=Asset Loading
    (0x010a5ab0, "VIObjFile::ReadEnd"),  # size=196, subsystem=Asset Loading
    (0x010a5b78, "VIObjFile::Copy"),  # size=684, subsystem=Asset Loading
    (0x010a5e28, "VIObjFile::Copy"),  # size=648, subsystem=Asset Loading
    (0x010a60b0, "VIObjFile::constructor"),  # size=40, subsystem=Asset Loading
    (0x010a60d8, "VIObjFile::~destructor"),  # size=108, subsystem=Asset Loading
    (0x010a6148, "VIObjFile::ResetState"),  # size=48, subsystem=Asset Loading
    (0x010a6178, "VIObjFile::Open"),  # size=156, subsystem=Asset Loading
    (0x010a6218, "VIObjFile::Open"),  # size=196, subsystem=Asset Loading
    (0x010a62e0, "VIObjFile::Open"),  # size=196, subsystem=Asset Loading
    (0x010a63a8, "VIObjFile::OpenObject"),  # size=192, subsystem=Asset Loading
    (0x010a6468, "VIObjFile::AbortOpen"),  # size=60, subsystem=Asset Loading
    (0x010a64a8, "VIObjFile::Close"),  # size=164, subsystem=Asset Loading
    (0x010a6550, "VIObjFile::Flush"),  # size=88, subsystem=Asset Loading
    (0x010a65a8, "VIObjFile::NumObjects"),  # size=8, subsystem=Asset Loading
    (0x010a65b0, "VIObjFile::FileType"),  # size=8, subsystem=Asset Loading
    (0x010a65b8, "VIObjFile::FileType"),  # size=12, subsystem=Asset Loading
    (0x010a65c8, "VIObjFile::NumSubObjects"),  # size=32, subsystem=Asset Loading
    (0x010a65e8, "VIObjFile::ObjectVersion"),  # size=32, subsystem=Asset Loading
    (0x010a6608, "VIObjFile::ObjectType"),  # size=32, subsystem=Asset Loading
    (0x010a6628, "VIObjFile::ObjectSize"),  # size=32, subsystem=Asset Loading
    (0x010a6648, "VIObjFile::WriteBegin"),  # size=52, subsystem=Asset Loading
    (0x010a6680, "VIObjFile::WriteDirBegin"),  # size=88, subsystem=Asset Loading
    (0x010a66d8, "VIObjFile::WriteEnd"),  # size=28, subsystem=Asset Loading
    (0x010a66f8, "VIObjFile::Write"),  # size=100, subsystem=Asset Loading
    (0x010a6760, "VIObjFile::Write"),  # size=100, subsystem=Asset Loading
    (0x010a67c8, "VIObjFile::Write"),  # size=100, subsystem=Asset Loading
    (0x010a6830, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a68b8, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6940, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a69c8, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6a50, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6ad8, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6b60, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6be8, "VIObjFile::Write"),  # size=132, subsystem=Asset Loading
    (0x010a6c70, "VIObjFile::Write"),  # size=104, subsystem=Asset Loading
    (0x010a6cd8, "VIObjFile::WriteString"),  # size=208, subsystem=Asset Loading
    (0x010a6da8, "VIObjFile::ReadBegin"),  # size=32, subsystem=Asset Loading
    (0x010a6dc8, "VIObjFile::ReadBegin"),  # size=136, subsystem=Asset Loading
    (0x010a6e50, "VIObjFile::ReadDirBegin"),  # size=172, subsystem=Asset Loading
    (0x010a6f00, "VIObjFile::Read"),  # size=108, subsystem=Asset Loading
    (0x010a6f70, "VIObjFile::Read"),  # size=108, subsystem=Asset Loading
    (0x010a6fe0, "VIObjFile::Read"),  # size=108, subsystem=Asset Loading
    (0x010a7050, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a70f0, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a7190, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a7230, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a72d0, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a7370, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a7410, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a74b0, "VIObjFile::Read"),  # size=160, subsystem=Asset Loading
    (0x010a7550, "VIObjFile::Read"),  # size=128, subsystem=Asset Loading
    (0x010a75d0, "VIObjFile::ReadString"),  # size=112, subsystem=Asset Loading
    (0x010a7640, "VIObjFile::ReadStringLength"),  # size=164, subsystem=Asset Loading
    (0x010a76e8, "VIObjFile::ReadStringBody"),  # size=148, subsystem=Asset Loading
    (0x010a7780, "VIObjFile::ReadStringBody"),  # size=224, subsystem=Asset Loading
    (0x010a7860, "VIWndDnas::OnDrawSelf"),  # size=1516, subsystem=Engine (VIWndDnas)
    (0x010a7e50, "VIWndDnas::OnMessage"),  # size=452, subsystem=Engine (VIWndDnas)
    (0x010a8018, "VIWndDnas::DrawFakeSplashInterface"),  # size=208, subsystem=Engine (VIWndDnas)
    (0x010a80e8, "VIWndDnas::DnasErrorString"),  # size=832, subsystem=Engine (VIWndDnas)
    (0x010a8428, "VIWndDnas::constructor"),  # size=76, subsystem=Engine (VIWndDnas)
    (0x010a8478, "VIWndDnas::~destructor"),  # size=148, subsystem=Engine (VIWndDnas)
    (0x010a8510, "VIWndDnas::Init"),  # size=84, subsystem=Engine (VIWndDnas)
    (0x010a8568, "VIWndDnas::Free"),  # size=48, subsystem=Engine (VIWndDnas)
    (0x010a8598, "VIWndDnas::OnKeyDown"),  # size=56, subsystem=Engine (VIWndDnas)
    (0x010a85d0, "VIWndDnas::OnKeyUp"),  # size=8, subsystem=Engine (VIWndDnas)
    (0x010a8748, "VICSpriteCust::SetResources"),  # size=4536, subsystem=Engine (VICSpriteCust)
    (0x010a9958, "VICSpriteCust::GetArmorSetTexture"),  # size=48, subsystem=Engine (VICSpriteCust)
    (0x010a9988, "VICSpriteCust::GetHairTexture"),  # size=24, subsystem=Engine (VICSpriteCust)
    (0x010a99a0, "VICSpriteCust::GetFaceTexture"),  # size=76, subsystem=Engine (VICSpriteCust)
    (0x010a99f0, "VICSpriteCust::GetFaceResourceID"),  # size=40, subsystem=Engine (VICSpriteCust)
    (0x010a9a18, "VICSpriteCust::GetRobeTexture"),  # size=80, subsystem=Engine (VICSpriteCust)
    (0x010a9a68, "VICSpriteCust::GetHelm"),  # size=24, subsystem=Engine (VICSpriteCust)
    (0x010a9a80, "VICSpriteCust::GetTintColor"),  # size=24, subsystem=Engine (VICSpriteCust)
    (0x010a9ab8, "VIParticleSprite::Create"),  # size=220, subsystem=Engine (VIParticleSprite)
    (0x010a9b98, "VIParticleSprite::Raster"),  # size=1656, subsystem=Engine (VIParticleSprite)
    (0x010aa210, "VIParticleSprite::Pick"),  # size=708, subsystem=Engine (VIParticleSprite)
    (0x010aa4d8, "VIParticleSprite::Copy"),  # size=388, subsystem=Engine (VIParticleSprite)
    (0x010aa660, "VIParticleSprite::constructor"),  # size=76, subsystem=Engine (VIParticleSprite)
    (0x010aa6b0, "VIParticleSprite::~destructor"),  # size=116, subsystem=Engine (VIParticleSprite)
    (0x010aa730, "VIParticleSprite::Collide"),  # size=8, subsystem=Engine (VIParticleSprite)
    (0x010aa738, "VIParticleSprite::Collide"),  # size=8, subsystem=Engine (VIParticleSprite)
    (0x010aa740, "VIParticleSprite::Release"),  # size=132, subsystem=Engine (VIParticleSprite)
    (0x010aa7c8, "VIWndEdit::constructor"),  # size=364, subsystem=UI
    (0x010aa938, "VIWndEdit::SetMaxTextLen"),  # size=188, subsystem=UI
    (0x010aa9f8, "VIWndEdit::OnDrawSelf"),  # size=6588, subsystem=UI
    (0x010ac3b8, "VIWndEdit::Insert"),  # size=268, subsystem=UI
    (0x010ac4c8, "VIWndEdit::Backspace"),  # size=180, subsystem=UI
    (0x010ac580, "VIWndEdit::OnKeyDown"),  # size=1612, subsystem=UI
    (0x010acbd0, "VIWndEdit::ComputeTextRows"),  # size=564, subsystem=UI
    (0x010ace08, "VIWndEdit::MoveCaretUp"),  # size=612, subsystem=UI
    (0x010ad070, "VIWndEdit::MoveCaretDown"),  # size=652, subsystem=UI
    (0x010ad300, "VIWndEdit::MoveCursor"),  # size=456, subsystem=UI
    (0x010ad4c8, "VIWndEdit::~destructor"),  # size=140, subsystem=UI
    (0x010ad558, "VIWndEdit::SetDisplayRows"),  # size=8, subsystem=UI
    (0x010ad560, "VIWndEdit::EnableCr"),  # size=40, subsystem=UI
    (0x010ad588, "VIWndEdit::IsCrEnabled"),  # size=8, subsystem=UI
    (0x010ad590, "VIWndEdit::EnableSp"),  # size=8, subsystem=UI
    (0x010ad598, "VIWndEdit::IsSpEnabled"),  # size=8, subsystem=UI
    (0x010ad5a0, "VIWndEdit::SetTitle"),  # size=40, subsystem=UI
    (0x010ad5c8, "VIWndEdit::SetTitle"),  # size=40, subsystem=UI
    (0x010ad5f0, "VIWndEdit::ClearText"),  # size=36, subsystem=UI
    (0x010ad618, "VIWndEdit::SetCenter"),  # size=48, subsystem=UI
    (0x010ad648, "VIWndEdit::SetText"),  # size=72, subsystem=UI
    (0x010ad690, "VIWndEdit::SetText"),  # size=72, subsystem=UI
    (0x010ad6d8, "VIWndEdit::Next"),  # size=56, subsystem=UI
    (0x010ad710, "VIWndEdit::Prev"),  # size=56, subsystem=UI
    (0x010ad748, "VIWndEdit::PlayActionSound"),  # size=48, subsystem=UI
    (0x010ad778, "VIWndEdit::OnKeyUp"),  # size=88, subsystem=UI
    (0x010ad7d0, "VIWndEdit::OnMessage"),  # size=184, subsystem=UI
    (0x010ad888, "VIWndEdit::CaretOffset"),  # size=8, subsystem=UI
    (0x010ad890, "VIWndEdit::SetCaretOffset"),  # size=120, subsystem=UI
    (0x010ad908, "VIWndEdit::GetCaretPos"),  # size=136, subsystem=UI
    (0x010ad990, "IPAddress::constructor"),  # size=76, subsystem=C++ Runtime
    (0x010ada18, "VICSprite::constructor"),  # size=772, subsystem=Engine (VICSprite)
    (0x010add20, "VICSprite::Clear"),  # size=472, subsystem=Engine (VICSprite)
    (0x010adef8, "VICSprite::SetDeath"),  # size=460, subsystem=Engine (VICSprite)
    (0x010ae0c8, "VICSprite::SetAttackAction"),  # size=464, subsystem=Engine (VICSprite)
    (0x010ae298, "VICSprite::SetAttackAltAction"),  # size=464, subsystem=Engine (VICSprite)
    (0x010ae468, "VICSprite::AttachItem"),  # size=672, subsystem=Engine (VICSprite)
    (0x010ae708, "VICSprite::SetName"),  # size=576, subsystem=Engine (VICSprite)
    (0x010ae948, "VICSprite::SetFace"),  # size=172, subsystem=Engine (VICSprite)
    (0x010ae9f8, "VICSprite::SetRobe"),  # size=396, subsystem=Engine (VICSprite)
    (0x010aeb88, "VICSprite::SetArmorSlot"),  # size=440, subsystem=Engine (VICSprite)
    (0x010aed40, "VICSprite::SetHair"),  # size=936, subsystem=Engine (VICSprite)
    (0x010af0e8, "VICSprite::SetHelm"),  # size=536, subsystem=Engine (VICSprite)
    (0x010af300, "VICSprite::SetAnimation"),  # size=1960, subsystem=Engine (VICSprite)
    (0x010afaa8, "VICSprite::SetItemAction"),  # size=316, subsystem=Engine (VICSprite)
    (0x010afbe8, "VICSprite::ProcessWeaponTrails"),  # size=1484, subsystem=Engine (VICSprite)
    (0x010b01b8, "VICSprite::CreateParticleEmitters"),  # size=200, subsystem=Engine (VICSprite)
    (0x010b0280, "VICSprite::UpdateParticleEmitters"),  # size=968, subsystem=Engine (VICSprite)
    (0x010b0648, "VICSprite::Process"),  # size=1336, subsystem=Engine (VICSprite)
    (0x010b0b80, "VICSprite::Copy"),  # size=2076, subsystem=Engine (VICSprite)
    (0x010b13a0, "VICSprite::Release"),  # size=748, subsystem=Engine (VICSprite)
    (0x010b1690, "VICSprite::SetDefaults"),  # size=424, subsystem=Engine (VICSprite)
    (0x010b1838, "VICSprite::SetDefaultEntries"),  # size=1576, subsystem=Engine (VICSprite)
    (0x010b1e60, "VICSprite::Share"),  # size=620, subsystem=Engine (VICSprite)
    (0x010b20d0, "VICSprite::SetAnimPriorities"),  # size=488, subsystem=Engine (VICSprite)
    (0x010b22b8, "VICSprite::SetAnimSoundChannels"),  # size=320, subsystem=Engine (VICSprite)
    (0x010b23f8, "VICSprite::CalcVolumeAndPan"),  # size=312, subsystem=Engine (VICSprite)
    (0x010b2748, "VICSprite::~destructor"),  # size=116, subsystem=Engine (VICSprite)
    (0x010b27c0, "VICSprite::Init"),  # size=180, subsystem=Engine (VICSprite)
    (0x010b2878, "VICSprite::SetAction"),  # size=160, subsystem=Engine (VICSprite)
    (0x010b2918, "VICSprite::SetLocomotion"),  # size=164, subsystem=Engine (VICSprite)
    (0x010b29c0, "VICSprite::IsActionComplete"),  # size=72, subsystem=Engine (VICSprite)
    (0x010b2a08, "VICSprite::DetachItem"),  # size=196, subsystem=Engine (VICSprite)
    (0x010b2ad0, "VICSprite::SetSkinsVisible"),  # size=240, subsystem=Engine (VICSprite)
    (0x010b2bc0, "VICSprite::SetIsPlayer"),  # size=36, subsystem=Engine (VICSprite)
    (0x010b2be8, "VICSprite::SetArmorSet"),  # size=128, subsystem=Engine (VICSprite)
    (0x010b2c68, "VICSprite::SetWeaponTrail"),  # size=44, subsystem=Engine (VICSprite)
    (0x010b2c98, "VICSprite::CalcSlotWorldTransform"),  # size=236, subsystem=Engine (VICSprite)
    (0x010b2d90, "VICSprite::Raster"),  # size=260, subsystem=Engine (VICSprite)
    (0x010b2e98, "VICSprite::Collide"),  # size=60, subsystem=Engine (VICSprite)
    (0x010b2ed8, "VICSprite::Collide"),  # size=8, subsystem=Engine (VICSprite)
    (0x010b2ee0, "VICSprite::QueryIntersection"),  # size=8, subsystem=Engine (VICSprite)
    (0x010b2ee8, "VICSprite::InitTextSlots"),  # size=168, subsystem=Engine (VICSprite)
    (0x010b2f90, "VICSprite::CalcLODOffDist"),  # size=128, subsystem=Engine (VICSprite)
    (0x010b3030, "VIParticleAttributes::constructor"),  # size=728, subsystem=Engine (VIParticleAttributes)
    (0x010b3308, "VIParticleAttributes::SetPattern"),  # size=260, subsystem=Engine (VIParticleAttributes)
    (0x010b3410, "VIParticleDefinitionEx::BlendMotifs"),  # size=2648, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4550, "VIParticleAttributes::~destructor"),  # size=44, subsystem=Engine (VIParticleAttributes)
    (0x010b4588, "VIParticleAttributes::SetFriction"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b45a8, "VIParticleAttributes::SetBirthrate"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b45c8, "VIParticleAttributes::SetBirthrateVar"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b45e8, "VIParticleAttributes::SetLifespan"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4608, "VIParticleAttributes::SetLifespanVar"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4628, "VIParticleAttributes::SetVelocity"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4648, "VIParticleAttributes::SetVelocityVar"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4668, "VIParticleAttributes::SetStartSize"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4688, "VIParticleAttributes::SetStartSizeVar"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b46a8, "VIParticleAttributes::SetEndSize"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b46c8, "VIParticleAttributes::SetEndSizeVar"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b46e8, "VIParticleAttributes::SetInheritVelocity"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4708, "VIParticleAttributes::SetDeltaSpawn"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4728, "VIParticleAttributes::SetStartColorVar"),  # size=48, subsystem=Engine (VIParticleAttributes)
    (0x010b4760, "VIParticleAttributes::SetEndColorVar"),  # size=48, subsystem=Engine (VIParticleAttributes)
    (0x010b47a0, "VIParticleAttributes::SetGradientColor"),  # size=56, subsystem=Engine (VIParticleAttributes)
    (0x010b47e0, "VIParticleAttributes::SetGradientRepeat"),  # size=20, subsystem=Engine (VIParticleAttributes)
    (0x010b4800, "VIParticleAttributes::SetInnerOffset"),  # size=96, subsystem=Engine (VIParticleAttributes)
    (0x010b4868, "VIParticleAttributes::SetInnerHprVar"),  # size=96, subsystem=Engine (VIParticleAttributes)
    (0x010b48d0, "VIParticleAttributes::SetOuterOffset"),  # size=96, subsystem=Engine (VIParticleAttributes)
    (0x010b4938, "VIParticleAttributes::SetOuterHprVar"),  # size=96, subsystem=Engine (VIParticleAttributes)
    (0x010b49a0, "VIParticleAttributes::SetNozzleAxis"),  # size=80, subsystem=Engine (VIParticleAttributes)
    (0x010b49f8, "VIParticleAttributes::SetNozzleHprVar"),  # size=96, subsystem=Engine (VIParticleAttributes)
    (0x010b4a78, "VIParticleAttributes::SetGravityOn"),  # size=36, subsystem=Engine (VIParticleAttributes)
    (0x010b4ad0, "VIParticleAttributes::ClearPattern"),  # size=72, subsystem=Engine (VIParticleAttributes)
    (0x010b4b18, "VIParticleMotif::constructor"),  # size=48, subsystem=Engine (VIParticleMotif)
    (0x010b4b48, "VIParticleMotif::~destructor"),  # size=44, subsystem=Engine (VIParticleMotif)
    (0x010b4b80, "VIParticleMotif::SetName"),  # size=64, subsystem=Engine (VIParticleMotif)
    (0x010b4bc8, "VIParticleDefinitionEx::constructor"),  # size=64, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4c08, "VIParticleDefinitionEx::~destructor"),  # size=92, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4c70, "VIParticleDefinitionEx::SetBlendModeEx"),  # size=8, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4c80, "VIParticleDefinitionEx::SetZWriteEx"),  # size=8, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4c90, "VIParticleDefinitionEx::SetZTestEx"),  # size=8, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4ca0, "VIParticleDefinitionEx::SetTextureConfigurationEx"),  # size=8, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4ca8, "VIParticleDefinitionEx::CreateMotif"),  # size=120, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4d20, "VIParticleDefinitionEx::DestroyMotif"),  # size=180, subsystem=Engine (VIParticleDefinitionEx)
    (0x010b4fe8, "VIWndEula::OnDrawSelf"),  # size=564, subsystem=Engine (VIWndEula)
    (0x010b5220, "VIWndEula::OnKeyDown"),  # size=348, subsystem=Engine (VIWndEula)
    (0x010b5380, "VIWndEula::OnMessage"),  # size=200, subsystem=Engine (VIWndEula)
    (0x010b5448, "VIWndEula::ComputeTextRows"),  # size=652, subsystem=Engine (VIWndEula)
    (0x010b56d8, "VIWndEula::constructor"),  # size=68, subsystem=Engine (VIWndEula)
    (0x010b5720, "VIWndEula::~destructor"),  # size=132, subsystem=Engine (VIWndEula)
    (0x010b57a8, "VIWndEula::Init"),  # size=68, subsystem=Engine (VIWndEula)
    (0x010b57f0, "VIWndEula::SetText"),  # size=184, subsystem=Engine (VIWndEula)
    (0x010b58a8, "VIWndEula::Free"),  # size=56, subsystem=Engine (VIWndEula)
    (0x010b58e0, "VIWndEula::OnKeyUp"),  # size=8, subsystem=Engine (VIWndEula)
    (0x010b58e8, "VIWndEula::Down"),  # size=88, subsystem=Engine (VIWndEula)
    (0x010b5940, "VIWndEula::Up"),  # size=76, subsystem=Engine (VIWndEula)
    (0x010b5e08, "VICylinder::PointInSolid"),  # size=320, subsystem=Engine (VICylinder)
    (0x010b5f48, "VIParticleDefinition::Create"),  # size=200, subsystem=Engine (VIParticleDefinition)
    (0x010b6010, "VIParticleEmitter::constructor"),  # size=440, subsystem=Engine (VIParticleEmitter)
    (0x010b61c8, "VIParticleEmitter::Create"),  # size=796, subsystem=Engine (VIParticleEmitter)
    (0x010b64e8, "VIParticleEmitter::SetDirection"),  # size=516, subsystem=Engine (VIParticleEmitter)
    (0x010b66f0, "VIParticleEmitter::Update"),  # size=2856, subsystem=Engine (VIParticleEmitter)
    (0x010b7218, "VIParticleEmitter::BlendMotifs"),  # size=236, subsystem=Engine (VIParticleEmitter)
    (0x010b7530, "VIParticleEmitter::RecomputeStaticBBox"),  # size=1928, subsystem=Engine (VIParticleEmitter)
    (0x010b7cb8, "VIParticleSystem::Init"),  # size=376, subsystem=Engine (VIParticleSystem)
    (0x010b7e30, "VIParticleSystem::Clear"),  # size=256, subsystem=Engine (VIParticleSystem)
    (0x010b7f30, "VIParticleSystem::CreateParticleDefinition"),  # size=236, subsystem=Engine (VIParticleSystem)
    (0x010b8020, "VIParticleSystem::ReleaseParticleDefinition"),  # size=308, subsystem=Engine (VIParticleSystem)
    (0x010b8158, "VIParticleSystem::Render"),  # size=1280, subsystem=Engine (VIParticleSystem)
    (0x010b8658, "VIMotifBlender::constructor"),  # size=52, subsystem=Engine (VIMotifBlender)
    (0x010b8690, "VIMotifBlender::~destructor"),  # size=92, subsystem=Engine (VIMotifBlender)
    (0x010b86f8, "VIMotifBlender::SetFactor"),  # size=32, subsystem=Engine (VIMotifBlender)
    (0x010b8718, "VIMotifBlender::Motif"),  # size=8, subsystem=Engine (VIMotifBlender)
    (0x010b8720, "VIParticleDefinition::constructor"),  # size=84, subsystem=Engine (VIParticleDefinition)
    (0x010b8778, "VIParticleDefinition::~destructor"),  # size=84, subsystem=Engine (VIParticleDefinition)
    (0x010b87d0, "VIParticleDefinition::Destroy"),  # size=160, subsystem=Engine (VIParticleDefinition)
    (0x010b8870, "VIParticleDefinition::SetBlendMode"),  # size=204, subsystem=Engine (VIParticleDefinition)
    (0x010b8940, "VIParticleDefinition::SetZWrite"),  # size=64, subsystem=Engine (VIParticleDefinition)
    (0x010b8980, "VIParticleDefinition::SetZTest"),  # size=64, subsystem=Engine (VIParticleDefinition)
    (0x010b89c8, "VIParticleDefinition::SetTexture"),  # size=96, subsystem=Engine (VIParticleDefinition)
    (0x010b8a28, "VIParticleDefinition::SetTextureConfiguration"),  # size=8, subsystem=Engine (VIParticleDefinition)
    (0x010b8a30, "VIParticleEmitter::~destructor"),  # size=140, subsystem=Engine (VIParticleEmitter)
    (0x010b8ac0, "VIParticleEmitter::Destroy"),  # size=124, subsystem=Engine (VIParticleEmitter)
    (0x010b8b48, "VIParticleEmitter::SetSpace"),  # size=28, subsystem=Engine (VIParticleEmitter)
    (0x010b8b78, "VIParticleEmitter::SetLocation"),  # size=100, subsystem=Engine (VIParticleEmitter)
    (0x010b8be8, "VIParticleEmitter::SetDirection"),  # size=28, subsystem=Engine (VIParticleEmitter)
    (0x010b8c08, "VIParticleEmitter::LinkMotifBlender"),  # size=64, subsystem=Engine (VIParticleEmitter)
    (0x010b8c48, "VIParticleEmitter::LinkMotifBlender"),  # size=124, subsystem=Engine (VIParticleEmitter)
    (0x010b8cc8, "VIParticleEmitter::UnlinkAllMotifBlenders"),  # size=48, subsystem=Engine (VIParticleEmitter)
    (0x010b8d00, "VIParticleEmitter::SetAttractor"),  # size=44, subsystem=Engine (VIParticleEmitter)
    (0x010b8d30, "VIParticleEmitter::ClearAttractor"),  # size=8, subsystem=Engine (VIParticleEmitter)
    (0x010b8d38, "VIParticleEmitter::Purge"),  # size=84, subsystem=Engine (VIParticleEmitter)
    (0x010b8df0, "VIParticleSystem::constructor"),  # size=72, subsystem=Engine (VIParticleSystem)
    (0x010b8e38, "VIParticleSystem::~destructor"),  # size=116, subsystem=Engine (VIParticleSystem)
    (0x010b8eb0, "VIParticleSystem::Purge"),  # size=108, subsystem=Engine (VIParticleSystem)
    (0x010b8f20, "VIParticleSystem::ParticleDefinition"),  # size=28, subsystem=Engine (VIParticleSystem)
    (0x010b8f40, "VIParticleSystem::ShareParticleDefinition"),  # size=48, subsystem=Engine (VIParticleSystem)
    (0x010b8f70, "VIParticleSystem::ReleaseAllParticleDefinitions"),  # size=124, subsystem=Engine (VIParticleSystem)
    (0x010b9110, "VIWndGenericRenderer::constructor"),  # size=232, subsystem=Engine (VIWndGenericRenderer)
    (0x010b91f8, "VIWndGenericRenderer::~destructor"),  # size=392, subsystem=Engine (VIWndGenericRenderer)
    (0x010b9380, "VIWndGenericRenderer::PostInit"),  # size=708, subsystem=Engine (VIWndGenericRenderer)
    (0x010b9648, "VIWndGenericRenderer::GoBack"),  # size=196, subsystem=Engine (VIWndGenericRenderer)
    (0x010b9710, "VIWndGenericRenderer::AddPage"),  # size=120, subsystem=Engine (VIWndGenericRenderer)
    (0x010b9e38, "VIWndGenericRenderer::GetValidMonth"),  # size=652, subsystem=Engine (VIWndGenericRenderer)
    (0x010ba0c8, "VIWndGenericRenderer::ActionOccured"),  # size=12968, subsystem=Engine (VIWndGenericRenderer)
    (0x010bd370, "VIWndGenericRenderer::OnDrawSelf"),  # size=628, subsystem=Engine (VIWndGenericRenderer)
    (0x010bd5e8, "VIWndGenericRenderer::ForceDisconnect"),  # size=184, subsystem=Engine (VIWndGenericRenderer)
    (0x010bd6a0, "VIWndGenericRenderer::OnKeyDown"),  # size=1624, subsystem=Engine (VIWndGenericRenderer)
    (0x010bdcf8, "VIWndGenericRenderer::OnMessage"),  # size=548, subsystem=Engine (VIWndGenericRenderer)
    (0x010bdf20, "VIWndGenericRenderer::DrawBackdrop"),  # size=760, subsystem=Engine (VIWndGenericRenderer)
    (0x010be218, "VIWndGenericRenderer::SetStationName"),  # size=36, subsystem=Engine (VIWndGenericRenderer)
    (0x010be240, "VIWndGenericRenderer::SetPassword"),  # size=36, subsystem=Engine (VIWndGenericRenderer)
    (0x010be268, "VIWndGenericRenderer::InitDone"),  # size=56, subsystem=Engine (VIWndGenericRenderer)
    (0x010be2a0, "VIWndGenericRenderer::Init"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x010be2a8, "VIWndGenericRenderer::ParseHostsFile"),  # size=108, subsystem=Engine (VIWndGenericRenderer)
    (0x010be318, "VIWndGenericRenderer::ParseHostsBuffer"),  # size=224, subsystem=Engine (VIWndGenericRenderer)
    (0x010be3f8, "VIWndGenericRenderer::ParseConfigFile"),  # size=108, subsystem=Engine (VIWndGenericRenderer)
    (0x010be468, "VIWndGenericRenderer::ParseConfigBuffer"),  # size=216, subsystem=Engine (VIWndGenericRenderer)
    (0x010be540, "VIWndGenericRenderer::AddPage"),  # size=84, subsystem=Engine (VIWndGenericRenderer)
    (0x010be598, "VIWndGenericRenderer::PopDialog"),  # size=40, subsystem=Engine (VIWndGenericRenderer)
    (0x010be608, "VIWndGenericRenderer::ValidateString"),  # size=220, subsystem=Engine (VIWndGenericRenderer)
    (0x010be990, "VIWndGenericRenderer::Finish"),  # size=60, subsystem=Engine (VIWndGenericRenderer)
    (0x010be9d0, "VIWndGenericRenderer::OnKeyUp"),  # size=192, subsystem=Engine (VIWndGenericRenderer)
    (0x010bea90, "VIWndGenericRenderer::DrawTick"),  # size=188, subsystem=Engine (VIWndGenericRenderer)
    (0x010beb50, "VIWndGenericRenderer::ResetTick"),  # size=40, subsystem=Engine (VIWndGenericRenderer)
    (0x010beb78, "VIWndGenericRenderer::BeginEdit"),  # size=216, subsystem=Engine (VIWndGenericRenderer)
    (0x010bec50, "VIWndGenericRenderer::WndEdit"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x010bec58, "VIWndGenericRenderer::IsInEdit"),  # size=12, subsystem=Engine (VIWndGenericRenderer)
    (0x010bec68, "VIWndGenericRenderer::EndEdit"),  # size=100, subsystem=Engine (VIWndGenericRenderer)
    (0x010bf1c8, "VIDictionary::constructor"),  # size=20, subsystem=Engine (VIDictionary)
    (0x010bf1e0, "VIDictionary::~destructor"),  # size=92, subsystem=Engine (VIDictionary)
    (0x010bf240, "VIDictionary::Init"),  # size=44, subsystem=Engine (VIDictionary)
    (0x010bf270, "VIDictionary::Size"),  # size=20, subsystem=Engine (VIDictionary)
    (0x010bf288, "VIDictionary::Clear"),  # size=20, subsystem=Engine (VIDictionary)
    (0x010bf2a0, "VIDictionary::Add"),  # size=60, subsystem=Engine (VIDictionary)
    (0x010bf2e0, "VIDictionary::Find"),  # size=144, subsystem=Engine (VIDictionary)
    (0x010bf370, "VIDictionary::FindTyped"),  # size=148, subsystem=Engine (VIDictionary)
    (0x010bf408, "VIDictionary::Remove"),  # size=100, subsystem=Engine (VIDictionary)
    (0x010bf470, "VIPickSegment::constructor"),  # size=112, subsystem=Engine (VIPickSegment)
    (0x010bf4e0, "VIPickSegment::Init"),  # size=400, subsystem=Engine (VIPickSegment)
    (0x010bf670, "VIPickSegment::GetHitPoint"),  # size=84, subsystem=Engine (VIPickSegment)
    (0x010bf6c8, "VIPickSegment::Precalc"),  # size=252, subsystem=Engine (VIPickSegment)
    (0x010bf7c8, "VIPickSegment::Init"),  # size=144, subsystem=Engine (VIPickSegment)
    (0x010bf858, "VIPickSegment::GetHitNormal"),  # size=36, subsystem=Engine (VIPickSegment)
    (0x010bf880, "VIPickSegment::GetHitDistance"),  # size=16, subsystem=Engine (VIPickSegment)
    (0x010bf890, "VIPickSegment::GetHitTime"),  # size=8, subsystem=Engine (VIPickSegment)
    (0x010bf898, "VIPickSegment::GetHitMaterial"),  # size=8, subsystem=Engine (VIPickSegment)
    (0x010bf8a0, "VIPickSegment::GetHitColor"),  # size=8, subsystem=Engine (VIPickSegment)
    (0x010bf8a8, "VIWndLegal::OnDrawSelf"),  # size=52, subsystem=Engine (VIWndLegal)
    (0x010bf8e0, "VIWndLegal::constructor"),  # size=48, subsystem=Engine (VIWndLegal)
    (0x010bf910, "VIWndLegal::~destructor"),  # size=100, subsystem=Engine (VIWndLegal)
    (0x010bf978, "VIWndLegal::Init"),  # size=8, subsystem=Engine (VIWndLegal)
    (0x010bf980, "VIWndLegal::Free"),  # size=8, subsystem=Engine (VIWndLegal)
    (0x010bf988, "VIWndLegal::OnKeyDown"),  # size=92, subsystem=Engine (VIWndLegal)
    (0x010bf9e8, "VIWndLegal::OnKeyUp"),  # size=8, subsystem=Engine (VIWndLegal)
    (0x010bf9f0, "VIWndLegal::OnMessage"),  # size=60, subsystem=Engine (VIWndLegal)
    (0x010bffa8, "VIColorBuffer::Color"),  # size=1220, subsystem=Lighting
    (0x010c0470, "VIColorBuffer::CalcDataSize"),  # size=308, subsystem=Lighting
    (0x010c05a8, "VIColorBuffer::constructor"),  # size=36, subsystem=Lighting
    (0x010c05d0, "VIColorBuffer::~destructor"),  # size=84, subsystem=Lighting
    (0x010c0628, "VIColorBuffer::Init"),  # size=176, subsystem=Lighting
    (0x010c06d8, "VIColorBuffer::Clear"),  # size=76, subsystem=Lighting
    (0x010c0728, "VIColorBuffer::Lock"),  # size=152, subsystem=Lighting
    (0x010c07c0, "VIColorBuffer::Unlock"),  # size=100, subsystem=Lighting
    (0x010c0828, "VIColorBuffer::Clear"),  # size=108, subsystem=Lighting
    (0x010c0898, "VIColorBuffer::Allocate"),  # size=72, subsystem=Lighting
    (0x010c0c90, "VIPlaneD::__cl"),  # size=656, subsystem=Engine (VIPlaneD)
    (0x010c0f20, "VIWndMessage::OnDrawSelf"),  # size=628, subsystem=Engine (VIWndMessage)
    (0x010c1198, "VIWndMessage::OnKeyDown"),  # size=336, subsystem=Engine (VIWndMessage)
    (0x010c12e8, "VIWndMessage::OnMessage"),  # size=196, subsystem=Engine (VIWndMessage)
    (0x010c13b0, "VIWndMessage::constructor"),  # size=68, subsystem=Engine (VIWndMessage)
    (0x010c13f8, "VIWndMessage::~destructor"),  # size=116, subsystem=Engine (VIWndMessage)
    (0x010c1470, "VIWndMessage::Init"),  # size=12, subsystem=Engine (VIWndMessage)
    (0x010c1480, "VIWndMessage::Free"),  # size=8, subsystem=Engine (VIWndMessage)
    (0x010c1488, "VIWndMessage::OnKeyUp"),  # size=8, subsystem=Engine (VIWndMessage)
    (0x010c1490, "VIWndMessage::Setup"),  # size=120, subsystem=Engine (VIWndMessage)
    (0x010c1508, "VIWndMessage::Setup"),  # size=128, subsystem=Engine (VIWndMessage)
    (0x010c1588, "VIWndMessage::Setup"),  # size=232, subsystem=Engine (VIWndMessage)
    (0x010c1670, "VIWndMessage::PromptText"),  # size=152, subsystem=Engine (VIWndMessage)
    (0x010c2578, "VIConsole::Init"),  # size=1624, subsystem=Engine (VIConsole)
    (0x010c2bd0, "VIConsole::Close"),  # size=60, subsystem=Engine (VIConsole)
    (0x010c2c10, "VIConsole::Process"),  # size=32, subsystem=Engine (VIConsole)
    (0x010c2c30, "VIConsole::GetInput"),  # size=216, subsystem=Engine (VIConsole)
    (0x010c2f90, "VIPlane::__cl"),  # size=344, subsystem=Engine (VIPlane)
    (0x010c30e8, "VIPlane::__as"),  # size=68, subsystem=Engine (VIPlane)
    (0x010c3130, "VIWnd::OnDraw"),  # size=196, subsystem=UI
    (0x010c31f8, "VIWnd::SetFocus"),  # size=316, subsystem=UI
    (0x010c3350, "VIWnd::constructor"),  # size=64, subsystem=UI
    (0x010c3390, "VIWnd::~destructor"),  # size=236, subsystem=UI
    (0x010c3480, "VIWnd::AddChild"),  # size=52, subsystem=UI
    (0x010c34b8, "VIWnd::RemoveChild"),  # size=64, subsystem=UI
    (0x010c34f8, "VIWnd::SetAppPtr"),  # size=8, subsystem=UI
    (0x010c3500, "VIWnd::GetAppPtr"),  # size=8, subsystem=UI
    (0x010c3508, "VIWnd::OnDrawSelf"),  # size=44, subsystem=UI
    (0x010c3538, "VIWnd::OnKeyUp"),  # size=88, subsystem=UI
    (0x010c3590, "VIWnd::OnKeyDown"),  # size=88, subsystem=UI
    (0x010c35e8, "VIWnd::OnMessage"),  # size=88, subsystem=UI
    (0x010c3790, "VIPointLight::ClampScale"),  # size=444, subsystem=Engine (VIPointLight)
    (0x010c3950, "VIPointLight::constructor"),  # size=80, subsystem=Engine (VIPointLight)
    (0x010c39a0, "VIPointLight::~destructor"),  # size=100, subsystem=Engine (VIPointLight)
    (0x010c3a08, "VIPointLight::Init"),  # size=160, subsystem=Engine (VIPointLight)
    (0x010c3aa8, "VIPointLight::Raster"),  # size=256, subsystem=Engine (VIPointLight)
    (0x010c3ba8, "VIPointLight::Collide"),  # size=8, subsystem=Engine (VIPointLight)
    (0x010c3bb0, "VIPointLight::Pick"),  # size=268, subsystem=Engine (VIPointLight)
    (0x010c3cc0, "VIPointLight::Copy"),  # size=256, subsystem=Engine (VIPointLight)
    (0x010c3dc0, "VIPointLight::Release"),  # size=64, subsystem=Engine (VIPointLight)
    (0x010c3e00, "VIWndOptions::OnDrawSelf"),  # size=1292, subsystem=Engine (VIWndOptions)
    (0x010c4310, "VIWndOptions::OnKeyDown"),  # size=672, subsystem=Engine (VIWndOptions)
    (0x010c45b0, "VIWndOptions::SaveAndExit"),  # size=176, subsystem=Engine (VIWndOptions)
    (0x010c4660, "VIWndOptions::OnMessage"),  # size=848, subsystem=Engine (VIWndOptions)
    (0x010c49b0, "VIWndOptions::Prev"),  # size=172, subsystem=Engine (VIWndOptions)
    (0x010c4a60, "VIWndOptions::Next"),  # size=248, subsystem=Engine (VIWndOptions)
    (0x010c4b58, "VIWndOptions::Decrement"),  # size=724, subsystem=Engine (VIWndOptions)
    (0x010c4e30, "VIWndOptions::Increment"),  # size=744, subsystem=Engine (VIWndOptions)
    (0x010c5118, "VIWndOptions::Select"),  # size=560, subsystem=Engine (VIWndOptions)
    (0x010c5348, "VIWndOptions::DrawMainMenu"),  # size=844, subsystem=Engine (VIWndOptions)
    (0x010c5698, "VIWndOptions::DrawGameOptions"),  # size=784, subsystem=Engine (VIWndOptions)
    (0x010c59a8, "VIWndOptions::DrawInterfaceOptions"),  # size=1192, subsystem=Engine (VIWndOptions)
    (0x010c5e50, "VIWndOptions::DrawSoundOptions"),  # size=856, subsystem=Engine (VIWndOptions)
    (0x010c61a8, "VIWndOptions::constructor"),  # size=92, subsystem=Engine (VIWndOptions)
    (0x010c6208, "VIWndOptions::~destructor"),  # size=188, subsystem=Engine (VIWndOptions)
    (0x010c62c8, "VIWndOptions::Init"),  # size=152, subsystem=Engine (VIWndOptions)
    (0x010c6360, "VIWndOptions::Free"),  # size=104, subsystem=Engine (VIWndOptions)
    (0x010c63c8, "VIWndOptions::OnKeyUp"),  # size=8, subsystem=Engine (VIWndOptions)
    (0x010c63d0, "VIWndOptions::Back"),  # size=80, subsystem=Engine (VIWndOptions)
    (0x010c65d8, "Base::MD5::Decode"),  # size=700, subsystem=Engine Utilities
    (0x010c6898, "Base::MD5::Encode"),  # size=760, subsystem=Engine Utilities
    (0x010c6b90, "Base::MD5::Final"),  # size=1232, subsystem=Engine Utilities
    (0x010c7060, "Base::MD5::Init"),  # size=104, subsystem=Engine Utilities
    (0x010c70c8, "Base::MD5::Transform"),  # size=5520, subsystem=Engine Utilities
    (0x010c8658, "Base::MD5::Update"),  # size=496, subsystem=Engine Utilities
    (0x010c8848, "Base::MD5::Update"),  # size=944, subsystem=Engine Utilities
    (0x010c8bf8, "Base::MD5::Update"),  # size=780, subsystem=Engine Utilities
    (0x010c8f08, "Base::MD5::Update"),  # size=388, subsystem=Engine Utilities
    (0x010c9090, "Base::MD5::Update"),  # size=400, subsystem=Engine Utilities
    (0x010c9220, "Base::MD5::Update"),  # size=412, subsystem=Engine Utilities
    (0x010c93c0, "Base::MD5::asHex"),  # size=1100, subsystem=Engine Utilities
    (0x010c9b50, "Base::MD5::FF"),  # size=112, subsystem=Engine Utilities
    (0x010c9bc0, "Base::MD5::GG"),  # size=116, subsystem=Engine Utilities
    (0x010c9c38, "Base::MD5::HH"),  # size=104, subsystem=Engine Utilities
    (0x010c9ca0, "Base::MD5::II"),  # size=108, subsystem=Engine Utilities
    (0x010c9d10, "Base::MD5::asHex"),  # size=56, subsystem=Engine Utilities
    (0x010c9d48, "Base::MD5::rotate_left"),  # size=24, subsystem=Engine Utilities
    (0x010c9d60, "Base::MD5::uadd"),  # size=40, subsystem=Engine Utilities
    (0x010c9d88, "Base::MD5::uadd"),  # size=64, subsystem=Engine Utilities
    (0x010c9dc8, "Base::MD5::uadd"),  # size=88, subsystem=Engine Utilities
    (0x010c9e60, "VIFile::Open"),  # size=356, subsystem=File I/O
    (0x010c9fc8, "VIFile::Close"),  # size=192, subsystem=File I/O
    (0x010ca088, "VIFile::BufferedRead"),  # size=1352, subsystem=File I/O
    (0x010ca5d0, "VIFile::BufferedWrite"),  # size=768, subsystem=File I/O
    (0x010ca8d0, "VIFile::BufferedSeek"),  # size=292, subsystem=File I/O
    (0x010ca9f8, "VIFile::ReadAsynch"),  # size=356, subsystem=File I/O
    (0x010cab60, "VIFile::WriteAsynch"),  # size=216, subsystem=File I/O
    (0x010cac38, "VIFile::CDSync"),  # size=416, subsystem=File I/O
    (0x010cadd8, "VIFile::EnableIopStreaming"),  # size=12, subsystem=File I/O
    (0x010cade8, "VIFile::IsIopStreamingEnabled"),  # size=12, subsystem=File I/O
    (0x010cadf8, "VIFile::constructor"),  # size=100, subsystem=File I/O
    (0x010cae60, "VIFile::~destructor"),  # size=84, subsystem=File I/O
    (0x010caeb8, "VIFile::Open"),  # size=20, subsystem=File I/O
    (0x010caed0, "VIFile::Open"),  # size=20, subsystem=File I/O
    (0x010caee8, "VIFile::Seek"),  # size=92, subsystem=File I/O
    (0x010caf48, "VIFile::Tell"),  # size=8, subsystem=File I/O
    (0x010caf50, "VIFile::Flush"),  # size=40, subsystem=File I/O
    (0x010caf78, "VIFile::Eof"),  # size=48, subsystem=File I/O
    (0x010cafa8, "VIFile::Read"),  # size=124, subsystem=File I/O
    (0x010cb028, "VIFile::Write"),  # size=124, subsystem=File I/O
    (0x010cb0a8, "VIFile::BufferFlush"),  # size=200, subsystem=File I/O
    (0x010cb170, "VIFile::BufferedReadCopy"),  # size=184, subsystem=File I/O
    (0x010cb228, "VIFile::BufferClear"),  # size=32, subsystem=File I/O
    (0x010cb248, "VIFile::AsynchAlignment"),  # size=8, subsystem=File I/O
    (0x010cb250, "VIFile::IsAsynchComplete"),  # size=64, subsystem=File I/O
    (0x010cb290, "VIFile::CDDiskReady"),  # size=56, subsystem=File I/O
    (0x010cb2c8, "VIFile::CDSearchFile"),  # size=252, subsystem=File I/O
    (0x010cb3c8, "VIFile::CDRead"),  # size=304, subsystem=File I/O
    (0x010cb588, "VIPointSprite::Init"),  # size=156, subsystem=Engine (VIPointSprite)
    (0x010cb628, "VIPointSprite::ClampScale"),  # size=444, subsystem=Engine (VIPointSprite)
    (0x010cb7e8, "VIPointSprite::constructor"),  # size=60, subsystem=Engine (VIPointSprite)
    (0x010cb828, "VIPointSprite::~destructor"),  # size=100, subsystem=Engine (VIPointSprite)
    (0x010cb890, "VIPointSprite::Raster"),  # size=256, subsystem=Engine (VIPointSprite)
    (0x010cb990, "VIPointSprite::Collide"),  # size=8, subsystem=Engine (VIPointSprite)
    (0x010cb998, "VIPointSprite::Collide"),  # size=8, subsystem=Engine (VIPointSprite)
    (0x010cb9a0, "VIPointSprite::Pick"),  # size=268, subsystem=Engine (VIPointSprite)
    (0x010cbab0, "VIPointSprite::Copy"),  # size=224, subsystem=Engine (VIPointSprite)
    (0x010cbb90, "VIPointSprite::Release"),  # size=64, subsystem=Engine (VIPointSprite)
    (0x010cbbd0, "VIWndPatcher::OnDrawSelf"),  # size=1920, subsystem=Engine (VIWndPatcher)
    (0x010cc350, "VIWndPatcher::OnKeyDown"),  # size=660, subsystem=Engine (VIWndPatcher)
    (0x010cc5e8, "VIWndPatcher::OnMessage"),  # size=652, subsystem=Engine (VIWndPatcher)
    (0x010cc878, "VIWndPatcher::DrawFakeSplashInterface"),  # size=568, subsystem=Engine (VIWndPatcher)
    (0x010ccab0, "VIWndPatcher::constructor"),  # size=84, subsystem=Engine (VIWndPatcher)
    (0x010ccb08, "VIWndPatcher::~destructor"),  # size=164, subsystem=Engine (VIWndPatcher)
    (0x010ccbb0, "VIWndPatcher::Init"),  # size=116, subsystem=Engine (VIWndPatcher)
    (0x010ccc28, "VIWndPatcher::Free"),  # size=72, subsystem=Engine (VIWndPatcher)
    (0x010ccc70, "VIWndPatcher::OnKeyUp"),  # size=8, subsystem=Engine (VIWndPatcher)
    (0x010ccc78, "VIWndPatcher::SetProgress"),  # size=8, subsystem=Engine (VIWndPatcher)
    (0x010ccc80, "VIWndPatcher::AppendMessage"),  # size=28, subsystem=Engine (VIWndPatcher)
    (0x010ccca0, "VIWndPatcher::ShowPatchMessage"),  # size=64, subsystem=Engine (VIWndPatcher)
    (0x010cd090, "VIQuatD::Mul"),  # size=576, subsystem=Engine (VIQuatD)
    (0x010cd410, "VIQuatD::Slerp"),  # size=1056, subsystem=Engine (VIQuatD)
    (0x010cd830, "VIQuatD::Normalize"),  # size=312, subsystem=Engine (VIQuatD)
    (0x010cd968, "VIQuatD::ConvertFrom"),  # size=680, subsystem=Engine (VIQuatD)
    (0x010cdc10, "VIQuatD::RotateX"),  # size=108, subsystem=Engine (VIQuatD)
    (0x010cdc80, "VIQuatD::RotateY"),  # size=112, subsystem=Engine (VIQuatD)
    (0x010cdcf0, "VIQuatD::RotateZ"),  # size=108, subsystem=Engine (VIQuatD)
    (0x010cdd60, "VIQuatD::InvertUnit"),  # size=124, subsystem=Engine (VIQuatD)
    (0x010cdde0, "VIQuatD::Invert"),  # size=128, subsystem=Engine (VIQuatD)
    (0x010cde60, "VIQuatD::Conjugate"),  # size=124, subsystem=Engine (VIQuatD)
    (0x010ce470, "VIMaterial::constructor"),  # size=248, subsystem=Engine (VIMaterial)
    (0x010ce568, "VIMaterial::Init"),  # size=240, subsystem=Engine (VIMaterial)
    (0x010ce658, "VIMaterial::InitWireframe"),  # size=176, subsystem=Engine (VIMaterial)
    (0x010ce708, "VIMaterial::InitSolidFill"),  # size=172, subsystem=Engine (VIMaterial)
    (0x010ce7b8, "VIMaterial::SetNumLayers"),  # size=356, subsystem=Engine (VIMaterial)
    (0x010ce920, "VIMaterial::SetLayerWrapMode"),  # size=248, subsystem=Engine (VIMaterial)
    (0x010cea18, "VIMaterial::CopyLayer"),  # size=340, subsystem=Engine (VIMaterial)
    (0x010ceb70, "VIMaterial::Process"),  # size=264, subsystem=Engine (VIMaterial)
    (0x010cec78, "VIMaterial::ConstructDMAPacket"),  # size=380, subsystem=Engine (VIMaterial)
    (0x010cedf8, "VIMaterial::ConstructTextPass"),  # size=1192, subsystem=Engine (VIMaterial)
    (0x010cf2a0, "VIMaterial::ConstructSolidFillPass"),  # size=784, subsystem=Engine (VIMaterial)
    (0x010cf5b0, "VIMaterial::ConstructWirePass"),  # size=368, subsystem=Engine (VIMaterial)
    (0x010cf720, "VIMaterial::SetZWrite"),  # size=44, subsystem=Engine (VIMaterial)
    (0x010cf750, "VIMaterial::SetZTest"),  # size=44, subsystem=Engine (VIMaterial)
    (0x010cf780, "VIMaterial::SetDither"),  # size=36, subsystem=Engine (VIMaterial)
    (0x010cf7a8, "VIMaterial::SetTessellate"),  # size=36, subsystem=Engine (VIMaterial)
    (0x010cf7d0, "VIMaterial::SetEmissiveColor"),  # size=32, subsystem=Engine (VIMaterial)
    (0x010cf7f0, "VIMaterial::SetLayerFillType"),  # size=92, subsystem=Engine (VIMaterial)
    (0x010cf850, "VIMaterial::SetLayerTexture"),  # size=156, subsystem=Engine (VIMaterial)
    (0x010cf8f0, "VIMaterial::GetLayerTexture"),  # size=24, subsystem=Engine (VIMaterial)
    (0x010cf908, "VIMaterial::SetLayerColor"),  # size=48, subsystem=Engine (VIMaterial)
    (0x010cf960, "VIMaterial::SetLayerModulate"),  # size=80, subsystem=Engine (VIMaterial)
    (0x010cf9b0, "VIMaterial::GetLayerWrapMode"),  # size=96, subsystem=Engine (VIMaterial)
    (0x010cfa10, "VIMaterial::SetLayerBlendMode"),  # size=36, subsystem=Engine (VIMaterial)
    (0x010cfa38, "VIMaterial::GetLayerBlendMode"),  # size=24, subsystem=Engine (VIMaterial)
    (0x010cfa50, "VIMaterial::SetLayerUVTransform"),  # size=72, subsystem=Engine (VIMaterial)
    (0x010cfa98, "VIMaterial::SetLayerUVRate"),  # size=100, subsystem=Engine (VIMaterial)
    (0x010cfb00, "VIMaterial::SetLayerTextureLODBias"),  # size=36, subsystem=Engine (VIMaterial)
    (0x010cfb28, "VIMaterial::SetLayerMagFilter"),  # size=76, subsystem=Engine (VIMaterial)
    (0x010cfb78, "VIMaterial::SetLayerUVSet"),  # size=68, subsystem=Engine (VIMaterial)
    (0x010cfdc0, "VIQuat::Slerp"),  # size=492, subsystem=Engine (VIQuat)
    (0x010cffb0, "VIQuat::ConvertFrom"),  # size=312, subsystem=Engine (VIQuat)
    (0x010d0190, "VIQuat::RotateX"),  # size=84, subsystem=Engine (VIQuat)
    (0x010d01e8, "VIQuat::RotateY"),  # size=84, subsystem=Engine (VIQuat)
    (0x010d0240, "VIQuat::RotateZ"),  # size=84, subsystem=Engine (VIQuat)
    (0x010d0298, "VIQuat::InvertUnit"),  # size=48, subsystem=Engine (VIQuat)
    (0x010d02c8, "VIQuat::Invert"),  # size=68, subsystem=Engine (VIQuat)
    (0x010d0310, "VIQuat::Conjugate"),  # size=48, subsystem=Engine (VIQuat)
    (0x010d0340, "VIQuat::Mul"),  # size=260, subsystem=Engine (VIQuat)
    (0x010d0448, "VIQuat::Normalize"),  # size=128, subsystem=Engine (VIQuat)
    (0x010d0558, "VIMatrix44::Invert"),  # size=584, subsystem=Engine (VIMatrix44)
    (0x010d07a0, "VIMatrix44::constructor"),  # size=84, subsystem=Engine (VIMatrix44)
    (0x010d07f8, "VIMatrix44::Zero"),  # size=28, subsystem=Engine (VIMatrix44)
    (0x010d0818, "VIMatrix44::Identity"),  # size=44, subsystem=Engine (VIMatrix44)
    (0x010d0848, "VIMatrix44::Mul"),  # size=120, subsystem=Engine (VIMatrix44)
    (0x010d0ab0, "VIMatrix44::InvertAffine"),  # size=164, subsystem=Engine (VIMatrix44)
    (0x010d0c58, "VIQueryTriList::constructor"),  # size=128, subsystem=Engine (VIQueryTriList)
    (0x010d0cd8, "VIQueryTriList::Intersect"),  # size=580, subsystem=Engine (VIQueryTriList)
    (0x010d0f20, "VIQueryTriList::Allocate"),  # size=176, subsystem=Engine (VIQueryTriList)
    (0x010d0fd0, "VIQueryTriList::~destructor"),  # size=120, subsystem=Engine (VIQueryTriList)
    (0x010d1048, "VIQueryTriList::Init"),  # size=184, subsystem=Engine (VIQueryTriList)
    (0x010d1100, "VIQueryTriList::Reset"),  # size=132, subsystem=Engine (VIQueryTriList)
    (0x010d1188, "VIQueryTriList::Clear"),  # size=68, subsystem=Engine (VIQueryTriList)
    (0x010d11d0, "VIQueryTriList::Volume"),  # size=32, subsystem=Engine (VIQueryTriList)
    (0x010d11f0, "VIWndReadMessage::OnDrawSelf"),  # size=360, subsystem=Engine (VIWndReadMessage)
    (0x010d1358, "VIWndReadMessage::OnMessage"),  # size=200, subsystem=Engine (VIWndReadMessage)
    (0x010d1420, "VIWndReadMessage::constructor"),  # size=68, subsystem=Engine (VIWndReadMessage)
    (0x010d1468, "VIWndReadMessage::~destructor"),  # size=116, subsystem=Engine (VIWndReadMessage)
    (0x010d14e0, "VIWndReadMessage::Init"),  # size=32, subsystem=Engine (VIWndReadMessage)
    (0x010d1500, "VIWndReadMessage::Clear"),  # size=8, subsystem=Engine (VIWndReadMessage)
    (0x010d1508, "VIWndReadMessage::OnKeyDown"),  # size=152, subsystem=Engine (VIWndReadMessage)
    (0x010d15a8, "VIWndReadMessage::SetMessage"),  # size=56, subsystem=Engine (VIWndReadMessage)
    (0x010d15e0, "VIWndReadMessage::AppendMessage"),  # size=36, subsystem=Engine (VIWndReadMessage)
    (0x010d1608, "VIWndReadMessage::Prev"),  # size=76, subsystem=Engine (VIWndReadMessage)
    (0x010d1658, "VIWndReadMessage::Next"),  # size=88, subsystem=Engine (VIWndReadMessage)
    (0x010d4110, "VIRadialFloraSystem::Update"),  # size=1348, subsystem=Engine (VIRadialFloraSystem)
    (0x010d4658, "VIRadialFloraSystem::Render"),  # size=656, subsystem=Engine (VIRadialFloraSystem)
    (0x010d48e8, "VIRadialFloraSystem::DrawSwatch"),  # size=420, subsystem=Engine (VIRadialFloraSystem)
    (0x010d4a90, "VIRadialFloraSystem::CreateSwatch"),  # size=624, subsystem=Engine (VIRadialFloraSystem)
    (0x010d4d00, "VIRadialFloraSystem::CreateFloraInsts"),  # size=2528, subsystem=Engine (VIRadialFloraSystem)
    (0x010d56e0, "VIRadialFloraSystem::CalcRadialLoc"),  # size=444, subsystem=Engine (VIRadialFloraSystem)
    (0x010d58a0, "VIZoneRadialFlora::Precalc"),  # size=672, subsystem=Engine (VIZoneRadialFlora)
    (0x010d5b40, "VIRadialFloraSystem::constructor"),  # size=92, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5ba0, "VIRadialFloraSystem::Init"),  # size=88, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5bf8, "VIRadialFloraSystem::Clear"),  # size=128, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5c78, "VIRadialFloraSystem::ReleaseSwatch"),  # size=88, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5cd0, "VIRadialFloraSystem::CalcZoneIndex"),  # size=120, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5d48, "VIRadialFloraSystem::QSortCompare"),  # size=44, subsystem=Engine (VIRadialFloraSystem)
    (0x010d5d78, "VIRadialFloraFilter::FilterActor"),  # size=8, subsystem=Engine (VIRadialFloraFilter)
    (0x010d5d80, "VIZoneRadialFlora::Init"),  # size=44, subsystem=Engine (VIZoneRadialFlora)
    (0x010d5db0, "VIZoneRadialFlora::Clear"),  # size=96, subsystem=Engine (VIZoneRadialFlora)
    (0x010d5e10, "VIWndSplash::Init"),  # size=196, subsystem=Engine (VIWndSplash)
    (0x010d5ed8, "VIWndSplash::OnDrawSelf"),  # size=1516, subsystem=Engine (VIWndSplash)
    (0x010d64c8, "VIWndSplash::OnKeyDown"),  # size=460, subsystem=Engine (VIWndSplash)
    (0x010d6698, "VIWndSplash::OnMessage"),  # size=632, subsystem=Engine (VIWndSplash)
    (0x010d6910, "VIWndSplash::SelectPlay"),  # size=704, subsystem=Engine (VIWndSplash)
    (0x010d6bd0, "VIWndSplash::ScanNetworkConfigurations"),  # size=584, subsystem=Engine (VIWndSplash)
    (0x010d6e18, "VIWndSplash::constructor"),  # size=76, subsystem=Engine (VIWndSplash)
    (0x010d6e68, "VIWndSplash::~destructor"),  # size=148, subsystem=Engine (VIWndSplash)
    (0x010d6f00, "VIWndSplash::Free"),  # size=124, subsystem=Engine (VIWndSplash)
    (0x010d6f80, "VIWndSplash::OnKeyUp"),  # size=8, subsystem=Engine (VIWndSplash)
    (0x010d6f88, "VIWndSplash::RestartConnect"),  # size=64, subsystem=Engine (VIWndSplash)
    (0x010d6fc8, "VIWndSplash::NetCnfCombination"),  # size=232, subsystem=Engine (VIWndSplash)
    (0x010dcb18, "VIWndStationLogin::OnDrawSelf"),  # size=1312, subsystem=Engine (VIWndStationLogin)
    (0x010dd038, "VIWndStationLogin::OnKeyDown"),  # size=304, subsystem=Engine (VIWndStationLogin)
    (0x010dd168, "VIWndStationLogin::OnMessage"),  # size=312, subsystem=Engine (VIWndStationLogin)
    (0x010dd2a0, "VIWndStationLogin::constructor"),  # size=104, subsystem=Engine (VIWndStationLogin)
    (0x010dd308, "VIWndStationLogin::~destructor"),  # size=116, subsystem=Engine (VIWndStationLogin)
    (0x010dd380, "VIWndStationLogin::Init"),  # size=132, subsystem=Engine (VIWndStationLogin)
    (0x010dd408, "VIWndStationLogin::Free"),  # size=8, subsystem=Engine (VIWndStationLogin)
    (0x010dd410, "VIWndStationLogin::OnKeyUp"),  # size=8, subsystem=Engine (VIWndStationLogin)
    (0x010f9d38, "VIRaster::Cull"),  # size=224, subsystem=Renderer
    (0x010f9e18, "VIRaster::Cull"),  # size=224, subsystem=Renderer
    (0x010f9ef8, "VIRaster::Pick"),  # size=504, subsystem=Renderer
    (0x010fa0f0, "VIRaster::PointInTriangle"),  # size=716, subsystem=Renderer
    (0x010fa3c0, "VIRaster::CalcHitColor"),  # size=1528, subsystem=Renderer
    (0x010fa9b8, "VIWorld::constructor"),  # size=284, subsystem=World
    (0x010faad8, "VIWorld::Init"),  # size=540, subsystem=World
    (0x010facf8, "VIWorld::SetProfiles"),  # size=2020, subsystem=World
    (0x010fb6d8, "VIWorld::CalcProfileBlend"),  # size=568, subsystem=World
    (0x010fb910, "VIWorld::RenderByFrustum"),  # size=188, subsystem=World
    (0x010fb9d0, "VIWorld::RenderByPortals"),  # size=376, subsystem=World
    (0x010fbb48, "VIWorld::RenderByVolume"),  # size=644, subsystem=World
    (0x010fbdd0, "VIWorld::Collide"),  # size=864, subsystem=World
    (0x010fc130, "VIWorld::Collide"),  # size=840, subsystem=World
    (0x010fc478, "VIWorld::InsertActor"),  # size=600, subsystem=World
    (0x010fc6d0, "VIWorld::Pick"),  # size=820, subsystem=World
    (0x010fca08, "VIWorld::Stream"),  # size=492, subsystem=World
    (0x010fcbf8, "VIWorld::StreamLeaf"),  # size=600, subsystem=World
    (0x010fce50, "VIWorld::Stream"),  # size=408, subsystem=World
    (0x010fcfe8, "VIWorld::StreamLeaf"),  # size=604, subsystem=World
    (0x010fd378, "VIWorld::Collide"),  # size=700, subsystem=World
    (0x010fd638, "VIWorld::QueryProximal"),  # size=444, subsystem=World
    (0x010fd7f8, "VIWorld::QueryVisibleBySphere"),  # size=324, subsystem=World
    (0x010fd940, "VIWorld::QueryVisibleWithPortals"),  # size=532, subsystem=World
    (0x010fdb58, "VIWorld::QueryVisible"),  # size=716, subsystem=World
    (0x010fde28, "VIWorld::QueryVolume"),  # size=456, subsystem=World
    (0x010fdff0, "VIWorld::QueryEmitters"),  # size=444, subsystem=World
    (0x010fe1b0, "VIWorld::QueryIntersection"),  # size=592, subsystem=World
    (0x010fe400, "VIWorld::~destructor"),  # size=116, subsystem=World
    (0x010fe478, "VIWorld::Clear"),  # size=96, subsystem=World
    (0x010fe4d8, "VIWorld::IsEmpty"),  # size=36, subsystem=World
    (0x010fe5b0, "VIWorld::RenderByVolume"),  # size=108, subsystem=World
    (0x010fe620, "VIWorld::Collide"),  # size=128, subsystem=World
    (0x010fe6a0, "VIWorld::Collide"),  # size=128, subsystem=World
    (0x010fe720, "VIWorld::InsertActor"),  # size=108, subsystem=World
    (0x010fe790, "VIWorld::Pick"),  # size=128, subsystem=World
    (0x010fe810, "VIWorld::Stream"),  # size=108, subsystem=World
    (0x010fe880, "VIWorld::Stream"),  # size=108, subsystem=World
    (0x010fe8f0, "VIWorld::Collide"),  # size=112, subsystem=World
    (0x010fe960, "VIWorld::QueryProximal"),  # size=108, subsystem=World
    (0x010fe9d0, "VIWorld::QueryVisible"),  # size=124, subsystem=World
    (0x010fea50, "VIWorld::QueryVolume"),  # size=108, subsystem=World
    (0x010feac0, "VIWorld::QueryEmitters"),  # size=108, subsystem=World
    (0x010feb30, "VIWorld::QueryIntersection"),  # size=108, subsystem=World
    (0x010feba0, "Base::strlwr"),  # size=72, subsystem=Networking
    (0x010febe8, "Base::strupr"),  # size=72, subsystem=Networking
    (0x010fec38, "VIPad::Read"),  # size=1128, subsystem=Engine (VIPad)
    (0x010ff0a0, "VIPad::constructor"),  # size=16, subsystem=Engine (VIPad)
    (0x010ff0b0, "VIPad::~destructor"),  # size=84, subsystem=Engine (VIPad)
    (0x010ff108, "VIPad::Init"),  # size=156, subsystem=Engine (VIPad)
    (0x010ff1a8, "VIPad::Close"),  # size=48, subsystem=Engine (VIPad)
    (0x010ff1d8, "VIPad::Process"),  # size=168, subsystem=Engine (VIPad)
    (0x010ff280, "VIPad::VibrateLf"),  # size=60, subsystem=Engine (VIPad)
    (0x010ff2c0, "VIPad::VibrateHf"),  # size=64, subsystem=Engine (VIPad)
    (0x010ff300, "VIPad::ScaleStick"),  # size=92, subsystem=Engine (VIPad)
    (0x010ff360, "VIRasterTess::InitTree"),  # size=528, subsystem=Engine (VIRasterTess)
    (0x010ff570, "VIRasterTess::Tessellate"),  # size=584, subsystem=Engine (VIRasterTess)
    (0x010ff7b8, "VIRasterTess::Split"),  # size=1700, subsystem=Engine (VIRasterTess)
    (0x010ffe60, "VIRasterTess::StoreResult"),  # size=708, subsystem=Engine (VIRasterTess)
    (0x01100128, "VIRasterTess::Init"),  # size=44, subsystem=Engine (VIRasterTess)
    (0x01100158, "VIRasterTess::Tessellate"),  # size=56, subsystem=Engine (VIRasterTess)
    (0x01100190, "VIWorldTree::constructor"),  # size=52, subsystem=Engine (VIWorldTree)
    (0x011001c8, "VIWorldTree::~destructor"),  # size=108, subsystem=Engine (VIWorldTree)
    (0x01100238, "VIWorldTree::Init"),  # size=92, subsystem=Engine (VIWorldTree)
    (0x01100298, "VIWorldTree::Clear"),  # size=80, subsystem=Engine (VIWorldTree)
    (0x011010e8, "VIPrimBuffer::constructor"),  # size=116, subsystem=Engine (VIPrimBuffer)
    (0x01101160, "VIPrimBuffer::Clear"),  # size=348, subsystem=Engine (VIPrimBuffer)
    (0x011012c0, "VIPrimBuffer::Unlock"),  # size=204, subsystem=Engine (VIPrimBuffer)
    (0x01101390, "VIPrimBuffer::Begin"),  # size=288, subsystem=Engine (VIPrimBuffer)
    (0x011014b0, "VIPrimBuffer::Vertex"),  # size=616, subsystem=Engine (VIPrimBuffer)
    (0x01101718, "VIPrimBuffer::Vertex"),  # size=1412, subsystem=Engine (VIPrimBuffer)
    (0x01101ca0, "VIPrimBuffer::End"),  # size=1184, subsystem=Engine (VIPrimBuffer)
    (0x01102140, "VIPrimBuffer::CalcBVolumes"),  # size=1240, subsystem=Engine (VIPrimBuffer)
    (0x01102618, "VIPrimBuffer::CalcDataSize"),  # size=656, subsystem=Engine (VIPrimBuffer)
    (0x011029b8, "VIPrimBuffer::~destructor"),  # size=84, subsystem=Engine (VIPrimBuffer)
    (0x01102a10, "VIPrimBuffer::Init"),  # size=136, subsystem=Engine (VIPrimBuffer)
    (0x01102b68, "VIPrimBuffer::Lock"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102b88, "VIPrimBuffer::SetPacking"),  # size=188, subsystem=Engine (VIPrimBuffer)
    (0x01102c48, "VIPrimBuffer::BeginMaterial"),  # size=80, subsystem=Engine (VIPrimBuffer)
    (0x01102c98, "VIPrimBuffer::EndMaterial"),  # size=52, subsystem=Engine (VIPrimBuffer)
    (0x01102cd0, "VIPrimBuffer::UV0"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102cf0, "VIPrimBuffer::UV0"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102d10, "VIPrimBuffer::UV1"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102d30, "VIPrimBuffer::UV1"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102d50, "VIPrimBuffer::Normal"),  # size=40, subsystem=Engine (VIPrimBuffer)
    (0x01102d78, "VIPrimBuffer::Normal"),  # size=40, subsystem=Engine (VIPrimBuffer)
    (0x01102da0, "VIPrimBuffer::Color"),  # size=32, subsystem=Engine (VIPrimBuffer)
    (0x01102dc0, "VIPrimBuffer::Bones"),  # size=48, subsystem=Engine (VIPrimBuffer)
    (0x01102df0, "VIPrimBuffer::Weights"),  # size=48, subsystem=Engine (VIPrimBuffer)
    (0x01102e20, "VIPrimBuffer::Weights"),  # size=48, subsystem=Engine (VIPrimBuffer)
    (0x01102e50, "VIPrimBuffer::VertexGroup"),  # size=16, subsystem=Engine (VIPrimBuffer)
    (0x01102e60, "VIPrimBuffer::Allocate"),  # size=72, subsystem=Engine (VIPrimBuffer)
    (0x01102ec8, "VIRealmInterface::constructor"),  # size=864, subsystem=Engine (VIRealmInterface)
    (0x01103228, "VIRealmInterface::~destructor"),  # size=416, subsystem=Engine (VIRealmInterface)
    (0x011033c8, "VIRealmInterface::Reset"),  # size=216, subsystem=Engine (VIRealmInterface)
    (0x011034a0, "VIRealmInterface::startGame"),  # size=384, subsystem=Engine (VIRealmInterface)
    (0x01103620, "VIRealmInterface::cancelGame"),  # size=208, subsystem=Engine (VIRealmInterface)
    (0x011036f0, "VIRealmInterface::SetGameCodeByIndex"),  # size=480, subsystem=Engine (VIRealmInterface)
    (0x011038d0, "VIRealmInterface::createPublicGame"),  # size=896, subsystem=Engine (VIRealmInterface)
    (0x01103c50, "VIRealmInterface::createPrivateGame"),  # size=848, subsystem=Engine (VIRealmInterface)
    (0x01103fa0, "VIRealmInterface::onConnect"),  # size=2056, subsystem=Engine (VIRealmInterface)
    (0x011047a8, "VIRealmInterface::UpdateNumPlayers"),  # size=228, subsystem=Engine (VIRealmInterface)
    (0x01104890, "VIRealmInterface::KickPlayer"),  # size=596, subsystem=Engine (VIRealmInterface)
    (0x01104ae8, "VIRealmInterface::process"),  # size=7652, subsystem=Engine (VIRealmInterface)
    (0x011068d0, "VIRealmInterface::onLogin"),  # size=2124, subsystem=Engine (VIRealmInterface)
    (0x01107120, "VIRealmInterface::onCreateAccount"),  # size=548, subsystem=Engine (VIRealmInterface)
    (0x01107348, "VIRealmInterface::onCreatePublicGame"),  # size=564, subsystem=Engine (VIRealmInterface)
    (0x01107580, "VIRealmInterface::onCreatePrivateGame"),  # size=524, subsystem=Engine (VIRealmInterface)
    (0x01107790, "VIRealmInterface::onMatchGame"),  # size=3444, subsystem=Engine (VIRealmInterface)
    (0x01108508, "VIRealmInterface::onGetGame"),  # size=1140, subsystem=Engine (VIRealmInterface)
    (0x01108980, "VIRealmInterface::onCancelGame"),  # size=372, subsystem=Engine (VIRealmInterface)
    (0x01108af8, "VIRealmInterface::onDoClientDiscovery"),  # size=356, subsystem=Engine (VIRealmInterface)
    (0x01108c60, "VIRealmInterface::onGetRules"),  # size=928, subsystem=Engine (VIRealmInterface)
    (0x01109000, "VIRealmInterface::notifyClientDiscovered"),  # size=196, subsystem=Engine (VIRealmInterface)
    (0x011090c8, "VIRealmInterface::notifyClientRequestsConnect"),  # size=304, subsystem=Engine (VIRealmInterface)
    (0x011091f8, "VIRealmInterface::GetSessionId"),  # size=8, subsystem=Engine (VIRealmInterface)
    (0x01109200, "VIRealmInterface::clientLeaveGame"),  # size=28, subsystem=Engine (VIRealmInterface)
    (0x01109220, "VIRealmInterface::SetGameDescription"),  # size=52, subsystem=Engine (VIRealmInterface)
    (0x01109258, "VIRealmInterface::onDisconnect"),  # size=40, subsystem=Engine (VIRealmInterface)
    (0x01109280, "VIRealmInterface::ShowGameDescription"),  # size=56, subsystem=Engine (VIRealmInterface)
    (0x011092b8, "VIRealmInterface::SetGameName"),  # size=36, subsystem=Engine (VIRealmInterface)
    (0x011092e0, "VIRealmInterface::onTouchSession"),  # size=52, subsystem=Engine (VIRealmInterface)
    (0x01109318, "VIRealmInterface::onGetRealmStats"),  # size=124, subsystem=Engine (VIRealmInterface)
    (0x01109398, "VIRealmInterface::onUpdateGameData"),  # size=8, subsystem=Engine (VIRealmInterface)
    (0x011093a0, "VIRealmInterface::notifyGameDiscovered"),  # size=152, subsystem=Engine (VIRealmInterface)
    (0x01109438, "VIXMLCallbackData::constructor"),  # size=92, subsystem=Engine (VIXMLCallbackData)
    (0x01109498, "VIXMLCallbackData::GetXMLHandler"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094a0, "VIXMLCallbackData::SetCallbackType"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094a8, "VIXMLCallbackData::GetCallbackType"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094b0, "VIXMLCallbackData::GetClientData"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094b8, "VIXMLCallbackData::GetTagName"),  # size=24, subsystem=Engine (VIXMLCallbackData)
    (0x011094d0, "VIXMLCallbackData::SetValue"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094d8, "VIXMLCallbackData::GetValue"),  # size=8, subsystem=Engine (VIXMLCallbackData)
    (0x011094e0, "VIXMLCallbackData::GetAttribute"),  # size=56, subsystem=Engine (VIXMLCallbackData)
    (0x01109518, "VIXMLCallbackData::GetIntegerAttribute"),  # size=112, subsystem=Engine (VIXMLCallbackData)
    (0x01109588, "VIXMLHandler::constructor"),  # size=44, subsystem=Engine (VIXMLHandler)
    (0x011095b8, "VIXMLHandler::ParseChild"),  # size=200, subsystem=Engine (VIXMLHandler)
    (0x01109680, "VIXMLHandler::Parse"),  # size=264, subsystem=Engine (VIXMLHandler)
    (0x01109788, "VIXMLHandler::PushXMLCallbackFunction"),  # size=72, subsystem=Engine (VIXMLHandler)
    (0x011097d0, "VIXMLHandler::PopXMLCallbackFunction"),  # size=104, subsystem=Engine (VIXMLHandler)
    (0x01109838, "VIXMLHandler::SetClientData"),  # size=8, subsystem=Engine (VIXMLHandler)
    (0x01109840, "VIXMLHandler::GetClientData"),  # size=8, subsystem=Engine (VIXMLHandler)
    (0x011098e8, "VIRaster::constructor"),  # size=896, subsystem=Renderer
    (0x01109c68, "VIRaster::~destructor"),  # size=212, subsystem=Renderer
    (0x01109d40, "VIRaster::Init"),  # size=816, subsystem=Renderer
    (0x0110a070, "VIRaster::SetClearColor"),  # size=476, subsystem=Renderer
    (0x0110a250, "VIRaster::Init"),  # size=884, subsystem=Renderer
    (0x0110a5c8, "VIRaster::Clear"),  # size=876, subsystem=Renderer
    (0x0110a938, "VIRaster::Frustum"),  # size=192, subsystem=Renderer
    (0x0110a9f8, "VIRaster::Orthographic"),  # size=200, subsystem=Renderer
    (0x0110aac0, "VIRaster::Flip"),  # size=312, subsystem=Renderer
    (0x0110abf8, "VIRaster::SetObjectBlends"),  # size=372, subsystem=Renderer
    (0x0110ad70, "VIRaster::Blit"),  # size=1852, subsystem=Renderer
    (0x0110b4b0, "VIRaster::Blit"),  # size=2648, subsystem=Renderer
    (0x0110bf08, "VIRaster::StretchBlit"),  # size=2680, subsystem=Renderer
    (0x0110c980, "VIRaster::EndTriStrip"),  # size=260, subsystem=Renderer
    (0x0110ca88, "VIRaster::EndTriFan"),  # size=260, subsystem=Renderer
    (0x0110cb90, "VIRaster::BeginBillboards"),  # size=1616, subsystem=Renderer
    (0x0110d1e0, "VIRaster::EndBillboards"),  # size=224, subsystem=Renderer
    (0x0110d2c0, "VIRaster::Begin2D"),  # size=216, subsystem=Renderer
    (0x0110d398, "VIRaster::Vertex"),  # size=296, subsystem=Renderer
    (0x0110d4c0, "VIRaster::Vertex"),  # size=288, subsystem=Renderer
    (0x0110d5e0, "VIRaster::Vertex"),  # size=240, subsystem=Renderer
    (0x0110d6d0, "VIRaster::DrawPrimBuffer"),  # size=412, subsystem=Renderer
    (0x0110d870, "VIRaster::ReleaseColorBuffer"),  # size=284, subsystem=Renderer
    (0x0110d990, "VIRaster::ReleaseSurface"),  # size=224, subsystem=Renderer
    (0x0110da70, "VIRaster::CopyMaterial"),  # size=432, subsystem=Renderer
    (0x0110dc20, "VIRaster::ReleaseMaterial"),  # size=232, subsystem=Renderer
    (0x0110dd08, "VIRaster::AddMaterial"),  # size=768, subsystem=Renderer
    (0x0110e008, "VIRaster::SetOverrideMaterial"),  # size=108, subsystem=Renderer
    (0x0110e078, "VIRaster::CreateMaterialPal"),  # size=340, subsystem=Renderer
    (0x0110e1d0, "VIRaster::CopyMaterialPal"),  # size=360, subsystem=Renderer
    (0x0110e338, "VIRaster::ReleaseMaterialPal"),  # size=292, subsystem=Renderer
    (0x0110e460, "VIRaster::DrawString"),  # size=748, subsystem=Renderer
    (0x0110e750, "VIRaster::DrawString"),  # size=748, subsystem=Renderer
    (0x0110ea40, "VIRaster::DrawCenteredString"),  # size=948, subsystem=Renderer
    (0x0110edf8, "VIRaster::DrawCenteredString"),  # size=948, subsystem=Renderer
    (0x0110f1b0, "VIRaster::DrawCenteredString"),  # size=1504, subsystem=Renderer
    (0x0110f790, "VIRaster::CalcCenteredStringScreenRect"),  # size=500, subsystem=Renderer
    (0x0110f988, "VIRaster::SetDefaultLights"),  # size=296, subsystem=Renderer
    (0x0110fab0, "VIRaster::FlushDMABufferIfFull"),  # size=280, subsystem=Renderer
    (0x0110fbc8, "VIRaster::SetFogRegisters"),  # size=504, subsystem=Renderer
    (0x0110fdc0, "VIRaster::DebugResources"),  # size=1012, subsystem=Renderer
    (0x011101b8, "VIRaster::DrawPrimBufferVUNC"),  # size=416, subsystem=Renderer
    (0x01110358, "VIRaster::DrawPrimBufferPackVUNC"),  # size=628, subsystem=Renderer
    (0x011105d0, "VIRaster::DrawPrimBufferPackVUNCG"),  # size=532, subsystem=Renderer
    (0x011107e8, "VIRaster::DrawPrimBufferTessPackVUNCG"),  # size=2520, subsystem=Renderer
    (0x011111c0, "VIRaster::TessTriangle"),  # size=1116, subsystem=Renderer
    (0x01111620, "VIRaster::DrawPrimBufferPackVUNBW"),  # size=456, subsystem=Renderer
    (0x011117e8, "VIRaster::DrawPrimBufferPackVU"),  # size=476, subsystem=Renderer
    (0x011119c8, "VIRaster::DrawPrimBufferPackVUNC"),  # size=672, subsystem=Renderer
    (0x01111c68, "VIRaster::CalcClipToScreen"),  # size=252, subsystem=Renderer
    (0x01111d68, "VIRaster::BlitBegin"),  # size=252, subsystem=Renderer
    (0x01111e68, "VIRaster::BlitEnd"),  # size=232, subsystem=Renderer
    (0x01111f50, "VIRaster::UploadMatrices"),  # size=804, subsystem=Renderer
    (0x01112278, "VIRaster::UploadPreTrans"),  # size=152, subsystem=Renderer
    (0x01112310, "VIRaster::UploadPerMaterial"),  # size=336, subsystem=Renderer
    (0x01112460, "VIRaster::UploadRasterMicro"),  # size=232, subsystem=Renderer
    (0x01112548, "VIRaster::UploadBillboardMicro"),  # size=196, subsystem=Renderer
    (0x01112610, "VIRaster::CreateDefaultResources"),  # size=624, subsystem=Renderer
    (0x01112880, "VIRaster::ReleaseDeferred"),  # size=308, subsystem=Renderer
    (0x011129b8, "VIRaster::SetGSScissoring"),  # size=324, subsystem=Renderer
    (0x01112cb0, "VIRaster::Init"),  # size=32, subsystem=Renderer
    (0x01112cd0, "VIRaster::Close"),  # size=64, subsystem=Renderer
    (0x01112d10, "VIRaster::Reset"),  # size=88, subsystem=Renderer
    (0x01112d68, "VIRaster::SetScreenResolution"),  # size=36, subsystem=Renderer
    (0x01112d98, "VIRaster::BeginScene"),  # size=196, subsystem=Renderer
    (0x01112e60, "VIRaster::EndScene"),  # size=192, subsystem=Renderer
    (0x01112f20, "VIRaster::SetModelView"),  # size=56, subsystem=Renderer
    (0x01112f60, "VIRaster::SetProjection"),  # size=60, subsystem=Renderer
    (0x01112fb0, "VIRaster::SetPreTranslations"),  # size=84, subsystem=Renderer
    (0x01113008, "VIRaster::Viewport"),  # size=236, subsystem=Renderer
    (0x01113138, "VIRaster::BeginTriStrip"),  # size=128, subsystem=Renderer
    (0x011131b8, "VIRaster::BeginTriFan"),  # size=124, subsystem=Renderer
    (0x01113238, "VIRaster::BeginLines"),  # size=8, subsystem=Renderer
    (0x01113240, "VIRaster::EndLines"),  # size=8, subsystem=Renderer
    (0x01113248, "VIRaster::End2D"),  # size=32, subsystem=Renderer
    (0x01113268, "VIRaster::UV"),  # size=28, subsystem=Renderer
    (0x01113288, "VIRaster::Normal"),  # size=36, subsystem=Renderer
    (0x011132b0, "VIRaster::Color"),  # size=40, subsystem=Renderer
    (0x011132d8, "VIRaster::DrawBBox"),  # size=8, subsystem=Renderer
    (0x011132e0, "VIRaster::CreatePrimBuffer"),  # size=140, subsystem=Renderer
    (0x01113370, "VIRaster::PrimBuffer"),  # size=28, subsystem=Renderer
    (0x01113390, "VIRaster::SharePrimBuffer"),  # size=44, subsystem=Renderer
    (0x011133c0, "VIRaster::ReleasePrimBuffer"),  # size=196, subsystem=Renderer
    (0x01113488, "VIRaster::DrawPrimBuffer"),  # size=212, subsystem=Renderer
    (0x01113560, "VIRaster::DrawPrimBuffer"),  # size=240, subsystem=Renderer
    (0x01113650, "VIRaster::CreateColorBuffer"),  # size=140, subsystem=Renderer
    (0x011136e0, "VIRaster::ColorBuffer"),  # size=28, subsystem=Renderer
    (0x01113700, "VIRaster::ShareColorBuffer"),  # size=44, subsystem=Renderer
    (0x01113730, "VIRaster::CreateSurface"),  # size=152, subsystem=Renderer
    (0x011137c8, "VIRaster::Surface"),  # size=28, subsystem=Renderer
    (0x011137e8, "VIRaster::ShareSurface"),  # size=44, subsystem=Renderer
    (0x01113818, "VIRaster::CreateMaterial"),  # size=104, subsystem=Renderer
    (0x01113880, "VIRaster::Material"),  # size=8, subsystem=Renderer
    (0x01113888, "VIRaster::SetMaterial"),  # size=68, subsystem=Renderer
    (0x011138d0, "VIRaster::ShareMaterial"),  # size=20, subsystem=Renderer
    (0x011138e8, "VIRaster::MaterialHasDepthSort"),  # size=12, subsystem=Renderer
    (0x011138f8, "VIRaster::SetSolidFillMaterial"),  # size=80, subsystem=Renderer
    (0x01113948, "VIRaster::SetSolidFillUIMaterial"),  # size=80, subsystem=Renderer
    (0x01113998, "VIRaster::SetSolidFillUIAVGMaterial"),  # size=80, subsystem=Renderer
    (0x011139e8, "VIRaster::SetWireframeMaterial"),  # size=80, subsystem=Renderer
    (0x01113a38, "VIRaster::SetPortalMaterial"),  # size=80, subsystem=Renderer
    (0x01113a88, "VIRaster::SetWireframe"),  # size=32, subsystem=Renderer
    (0x01113aa8, "VIRaster::SetSolidFill"),  # size=32, subsystem=Renderer
    (0x01113ac8, "VIRaster::MaterialPal"),  # size=28, subsystem=Renderer
    (0x01113ae8, "VIRaster::ShareMaterialPal"),  # size=44, subsystem=Renderer
    (0x01113b18, "VIRaster::MaterialPalHasDepthSort"),  # size=104, subsystem=Renderer
    (0x01113b80, "VIRaster::GetMaterialPalSize"),  # size=32, subsystem=Renderer
    (0x01113ba0, "VIRaster::GetMaterialPalEntry"),  # size=44, subsystem=Renderer
    (0x01113bd0, "VIRaster::CreateFont"),  # size=140, subsystem=Renderer
    (0x01113c60, "VIRaster::ShareFont"),  # size=44, subsystem=Renderer
    (0x01113c90, "VIRaster::Font"),  # size=28, subsystem=Renderer
    (0x01113cb0, "VIRaster::ReleaseFont"),  # size=164, subsystem=Renderer
    (0x01113d58, "VIRaster::GetWidth"),  # size=60, subsystem=Renderer
    (0x01113d98, "VIRaster::GetWidth"),  # size=56, subsystem=Renderer
    (0x01113dd0, "VIRaster::GetStringWidth"),  # size=52, subsystem=Renderer
    (0x01113e08, "VIRaster::GetStringWidth"),  # size=52, subsystem=Renderer
    (0x01113e40, "VIRaster::GetPointSize"),  # size=32, subsystem=Renderer
    (0x01113e60, "VIRaster::SetMultiTexture"),  # size=12, subsystem=Renderer
    (0x01113e70, "VIRaster::SetTime"),  # size=12, subsystem=Renderer
    (0x01113e80, "VIRaster::GetTime"),  # size=8, subsystem=Renderer
    (0x01113e88, "VIRaster::SetAmbient"),  # size=56, subsystem=Renderer
    (0x01113ec0, "VIRaster::EnableAmbient"),  # size=24, subsystem=Renderer
    (0x01113ed8, "VIRaster::SetSunLight"),  # size=148, subsystem=Renderer
    (0x01113f70, "VIRaster::EnableSunLight"),  # size=24, subsystem=Renderer
    (0x01113f88, "VIRaster::SetDirLight"),  # size=188, subsystem=Renderer
    (0x01114048, "VIRaster::EnableDirLight"),  # size=28, subsystem=Renderer
    (0x01114068, "VIRaster::EnableAllDirLights"),  # size=16, subsystem=Renderer
    (0x01114078, "VIRaster::MaxDirLights"),  # size=8, subsystem=Renderer
    (0x01114080, "VIRaster::SetPointLight"),  # size=172, subsystem=Renderer
    (0x01114130, "VIRaster::EnablePointLight"),  # size=28, subsystem=Renderer
    (0x01114150, "VIRaster::EnableAllPointLights"),  # size=24, subsystem=Renderer
    (0x01114168, "VIRaster::MaxPointLights"),  # size=8, subsystem=Renderer
    (0x01114170, "VIRaster::EnableAllLights"),  # size=48, subsystem=Renderer
    (0x011141a0, "VIRaster::SetStaticLighting"),  # size=48, subsystem=Renderer
    (0x011141e0, "VIRaster::EnableTessellation"),  # size=8, subsystem=Renderer
    (0x011141e8, "VIRaster::SetFog"),  # size=216, subsystem=Renderer
    (0x011142c0, "VIRaster::NumTextureSwaps"),  # size=12, subsystem=Renderer
    (0x011142d0, "VIRaster::Flush"),  # size=180, subsystem=Renderer
    (0x01114388, "VIRaster::CalcMatrices"),  # size=176, subsystem=Renderer
    (0x01114438, "VIRaster::SetZBias"),  # size=84, subsystem=Renderer
    (0x01114490, "VIRaster::Store2D"),  # size=112, subsystem=Renderer
    (0x01114500, "VIRaster::Restore2D"),  # size=96, subsystem=Renderer
    (0x01114560, "VIRaster::InitMaterialLRU"),  # size=224, subsystem=Renderer
    (0x01114640, "VIRaster::ClearMaterialLRU"),  # size=84, subsystem=Renderer
    (0x01114698, "VIRaster::InitDMADoubleBuffer"),  # size=128, subsystem=Renderer
    (0x01114718, "VIRaster::ClearDMADoubleBuffer"),  # size=84, subsystem=Renderer
    (0x01114770, "VIRaster::InitSPRDoubleBuffer"),  # size=32, subsystem=Renderer
    (0x01114790, "VIRaster::SwapSPRBuffer"),  # size=32, subsystem=Renderer
    (0x011147b0, "VIRaster::SPRBuffer"),  # size=8, subsystem=Renderer
    (0x011147b8, "VIRaster::InitGSRegisters"),  # size=236, subsystem=Renderer
    (0x011148a8, "VIRaster::DebugEEMicro"),  # size=132, subsystem=Renderer
    (0x01114940, "VIRaster::SetGSDithering"),  # size=128, subsystem=Renderer
    (0x011149c0, "VIRaster::SetGSDitherMatrix"),  # size=216, subsystem=Renderer
    (0x01114a98, "VIRaster::SetClipAndLight"),  # size=8, subsystem=Renderer
    (0x01114aa0, "VIRaster::InitDMACHandler"),  # size=92, subsystem=Renderer
    (0x01114b00, "VIRaster::RemoveDMACHandler"),  # size=84, subsystem=Renderer
    (0x01114be8, "VIRect::Scale"),  # size=112, subsystem=Engine (VIRect)
    (0x01114c58, "VIRect::Scale"),  # size=152, subsystem=Engine (VIRect)
    (0x01114cf0, "VIRect::Union"),  # size=104, subsystem=Engine (VIRect)
    (0x01114d58, "VIRect::Union"),  # size=100, subsystem=Engine (VIRect)
    (0x01114dc0, "VIRect::Intersect"),  # size=140, subsystem=Engine (VIRect)
    (0x01115008, "VIRect::Bound"),  # size=140, subsystem=Engine (VIRect)
    (0x011150c8, "VIRect::Area"),  # size=40, subsystem=Engine (VIRect)
    (0x01115120, "VIZone::constructor"),  # size=304, subsystem=Zone
    (0x01115250, "VIZone::~destructor"),  # size=200, subsystem=Zone
    (0x01115318, "VIZone::Init"),  # size=172, subsystem=Zone
    (0x011153c8, "VIZone::Clear"),  # size=208, subsystem=Zone
    (0x01115498, "VIZone::ResetToProxy"),  # size=276, subsystem=Zone
    (0x011155b0, "VIZone::RenderByVolume"),  # size=628, subsystem=Zone
    (0x01115828, "VIZone::SetPretranslations"),  # size=204, subsystem=Zone
    (0x011158f8, "VIZone::Collide"),  # size=164, subsystem=Zone
    (0x011159a0, "VIZone::Collide"),  # size=816, subsystem=Zone
    (0x01115cd0, "VIZone::CollideRoom"),  # size=248, subsystem=Zone
    (0x01115dc8, "VIZone::Collide"),  # size=164, subsystem=Zone
    (0x01115e70, "VIZone::Collide"),  # size=792, subsystem=Zone
    (0x01116188, "VIZone::CollideRoom"),  # size=248, subsystem=Zone
    (0x01116280, "VIZone::InsertActor"),  # size=600, subsystem=Zone
    (0x011164d8, "VIZone::RenderRoom"),  # size=520, subsystem=Zone
    (0x011166e0, "VIZone::RenderThroughPortals"),  # size=628, subsystem=Zone
    (0x01116a18, "VIZone::Pick"),  # size=188, subsystem=Zone
    (0x01116ad8, "VIZone::Pick"),  # size=780, subsystem=Zone
    (0x01116de8, "VIZone::PickRoom"),  # size=248, subsystem=Zone
    (0x01116ee0, "VIZone::Stream"),  # size=492, subsystem=Zone
    (0x011170d0, "VIZone::StreamLeaf"),  # size=432, subsystem=Zone
    (0x01117280, "VIZone::Stream"),  # size=408, subsystem=Zone
    (0x01117418, "VIZone::StreamLeaf"),  # size=432, subsystem=Zone
    (0x011175c8, "VIZone::StreamRoomIn"),  # size=716, subsystem=Zone
    (0x01117898, "VIZone::StreamRoomHalt"),  # size=320, subsystem=Zone
    (0x011179d8, "VIZone::StreamRoomStaticsIn"),  # size=912, subsystem=Zone
    (0x01117d68, "VIZone::StreamRoomStaticsHalt"),  # size=344, subsystem=Zone
    (0x01117ec0, "VIZone::StreamRoomStaticsOut"),  # size=384, subsystem=Zone
    (0x01118040, "VIZone::Find"),  # size=176, subsystem=Zone
    (0x011180f0, "VIZone::Collide"),  # size=664, subsystem=Zone
    (0x01118388, "VIZone::QueryProximal"),  # size=404, subsystem=Zone
    (0x01118520, "VIZone::QueryProximalRoom"),  # size=172, subsystem=Zone
    (0x011185d0, "VIZone::QueryVisible"),  # size=676, subsystem=Zone
    (0x01118878, "VIZone::QueryThroughPortals"),  # size=712, subsystem=Zone
    (0x01118b40, "VIZone::QueryVolume"),  # size=408, subsystem=Zone
    (0x01118cd8, "VIZone::QueryEmitters"),  # size=404, subsystem=Zone
    (0x01118e70, "VIZone::QueryIntersection"),  # size=136, subsystem=Zone
    (0x01118ef8, "VIZone::QueryIntersection"),  # size=568, subsystem=Zone
    (0x01119130, "VIZone::QueryIntersectionRoom"),  # size=240, subsystem=Zone
    (0x011192b8, "VIZone::RenderByVolume"),  # size=120, subsystem=Zone
    (0x01119330, "VIZone::RenderLeaf"),  # size=128, subsystem=Zone
    (0x011193b0, "VIZone::CollideLeaf"),  # size=160, subsystem=Zone
    (0x01119450, "VIZone::CollideLeaf"),  # size=160, subsystem=Zone
    (0x011194f0, "VIZone::InsertActor"),  # size=68, subsystem=Zone
    (0x01119538, "VIZone::PickLeaf"),  # size=160, subsystem=Zone
    (0x011195d8, "VIZone::Stream"),  # size=68, subsystem=Zone
    (0x01119620, "VIZone::Stream"),  # size=84, subsystem=Zone
    (0x01119678, "VIZone::StreamRoomOut"),  # size=120, subsystem=Zone
    (0x011196f0, "VIZone::Load"),  # size=128, subsystem=Zone
    (0x01119770, "VIZone::Collide"),  # size=112, subsystem=Zone
    (0x011197e0, "VIZone::CollideLeaf"),  # size=248, subsystem=Zone
    (0x011198d8, "VIZone::QueryProximal"),  # size=68, subsystem=Zone
    (0x01119920, "VIZone::QueryProximalLeaf"),  # size=100, subsystem=Zone
    (0x01119988, "VIZone::QueryVisible"),  # size=68, subsystem=Zone
    (0x011199d0, "VIZone::QueryVisibleLeaf"),  # size=128, subsystem=Zone
    (0x01119a50, "VIZone::QueryVisibleRoom"),  # size=164, subsystem=Zone
    (0x01119af8, "VIZone::QueryVolume"),  # size=68, subsystem=Zone
    (0x01119b40, "VIZone::QueryVolumeLeaf"),  # size=100, subsystem=Zone
    (0x01119ba8, "VIZone::QueryVolumeRoom"),  # size=144, subsystem=Zone
    (0x01119c38, "VIZone::QueryEmitters"),  # size=68, subsystem=Zone
    (0x01119c80, "VIZone::QueryEmittersLeaf"),  # size=100, subsystem=Zone
    (0x01119ce8, "VIZone::QueryEmittersRoom"),  # size=152, subsystem=Zone
    (0x01119d80, "VIZone::QueryIntersectionLeaf"),  # size=100, subsystem=Zone
    (0x01119ff8, "RealmService::RealmGatewayAPICore::OnConnect"),  # size=356, subsystem=Networking
    (0x0111a160, "RealmService::RealmGatewayAPICore::OnDisconnect"),  # size=148, subsystem=Networking
    (0x0111a1f8, "RealmService::RealmGatewayAPICore::responseCallback"),  # size=3712, subsystem=Networking
    (0x0111b078, "RealmService::RealmGatewayAPICore::responseCallback"),  # size=7352, subsystem=Networking
    (0x0111cd30, "RealmService::RealmGatewayAPICore::encryptString"),  # size=508, subsystem=Networking
    (0x0111cf30, "RealmService::RealmGatewayAPICore::decryptString"),  # size=508, subsystem=Networking
    (0x0111d130, "RealmService::RealmGatewayAPICore::encryptString"),  # size=296, subsystem=Networking
    (0x0111d258, "RealmService::RealmGatewayAPICore::decryptString"),  # size=296, subsystem=Networking
    (0x0111d380, "VIRaster::PickPrimBuffer"),  # size=532, subsystem=Renderer
    (0x0111d598, "VIRaster::PickPrimBuffer"),  # size=424, subsystem=Renderer
    (0x0111d740, "VIRaster::PickPrimBufferVUNC"),  # size=1816, subsystem=Renderer
    (0x0111de58, "VIRaster::PickPrimBufferPackVUNC"),  # size=1272, subsystem=Renderer
    (0x0111e350, "VIRaster::PickPrimBufferPackVUNCG"),  # size=1512, subsystem=Renderer
    (0x0111e938, "VIRaster::PickPrimBufferPackVUNC"),  # size=1448, subsystem=Renderer
    (0x0111eee0, "VIRaster::PickPrimBufferPackVUNBW"),  # size=8, subsystem=Renderer
    (0x0111ef38, "VIZoneRoom::constructor"),  # size=116, subsystem=Engine (VIZoneRoom)
    (0x0111efb0, "VIZoneRoom::Clear"),  # size=212, subsystem=Engine (VIZoneRoom)
    (0x0111f088, "VIZoneRoom::CalcPortalPlane"),  # size=684, subsystem=Engine (VIZoneRoom)
    (0x0111f338, "VIZoneRoom::~destructor"),  # size=108, subsystem=Engine (VIZoneRoom)
    (0x0111f3a8, "VIZoneRoom::Init"),  # size=204, subsystem=Engine (VIZoneRoom)
    (0x0111f478, "VIZoneRoom::DestRoom"),  # size=12, subsystem=Engine (VIZoneRoom)
    (0x0111f488, "VIZoneRoom::Begin"),  # size=84, subsystem=Engine (VIZoneRoom)
    (0x0111f4e0, "VIZoneRoom::Vertex"),  # size=92, subsystem=Engine (VIZoneRoom)
    (0x0111f540, "VIZoneRoom::End"),  # size=56, subsystem=Engine (VIZoneRoom)
    (0x0111f578, "VIZoneRoom::CalcDataSize"),  # size=48, subsystem=Engine (VIZoneRoom)
    (0x0111f5a8, "VIZoneRoom::Allocate"),  # size=72, subsystem=Engine (VIZoneRoom)
    (0x0111f5f0, "RealmService::RealmGatewayAPI::createAccount"),  # size=1132, subsystem=Networking
    (0x0111fa60, "RealmService::RealmGatewayAPI::consumeKey"),  # size=852, subsystem=Networking
    (0x0111fdb8, "RealmService::RealmGatewayAPI::login"),  # size=640, subsystem=Networking
    (0x01120038, "RealmService::RealmGatewayAPI::logout"),  # size=392, subsystem=Networking
    (0x011201c0, "RealmService::RealmGatewayAPI::touchSession"),  # size=392, subsystem=Networking
    (0x01120348, "RealmService::RealmGatewayAPI::createAvatar"),  # size=392, subsystem=Networking
    (0x011204d0, "RealmService::RealmGatewayAPI::destroyAvatar"),  # size=392, subsystem=Networking
    (0x01120658, "RealmService::RealmGatewayAPI::getPublicRooms"),  # size=392, subsystem=Networking
    (0x011207e0, "RealmService::RealmGatewayAPI::getRoom"),  # size=404, subsystem=Networking
    (0x01120978, "RealmService::RealmGatewayAPI::createPrivateRoom"),  # size=404, subsystem=Networking
    (0x01120b10, "RealmService::RealmGatewayAPI::enterRoom"),  # size=404, subsystem=Networking
    (0x01120ca8, "RealmService::RealmGatewayAPI::leaveRoom"),  # size=404, subsystem=Networking
    (0x01120e40, "RealmService::RealmGatewayAPI::sendRoomMessage"),  # size=416, subsystem=Networking
    (0x01120fe0, "RealmService::RealmGatewayAPI::sendInstantMessage"),  # size=416, subsystem=Networking
    (0x01121180, "RealmService::RealmGatewayAPI::addFriend"),  # size=404, subsystem=Networking
    (0x01121318, "RealmService::RealmGatewayAPI::removeFriend"),  # size=404, subsystem=Networking
    (0x011214b0, "RealmService::RealmGatewayAPI::addIgnore"),  # size=404, subsystem=Networking
    (0x01121648, "RealmService::RealmGatewayAPI::removeIgnore"),  # size=404, subsystem=Networking
    (0x011217e0, "RealmService::RealmGatewayAPI::addRoomModerator"),  # size=416, subsystem=Networking
    (0x01121980, "RealmService::RealmGatewayAPI::removeRoomModerator"),  # size=416, subsystem=Networking
    (0x01121b20, "RealmService::RealmGatewayAPI::addBan"),  # size=416, subsystem=Networking
    (0x01121cc0, "RealmService::RealmGatewayAPI::removeBan"),  # size=416, subsystem=Networking
    (0x01121e60, "RealmService::RealmGatewayAPI::addInvite"),  # size=416, subsystem=Networking
    (0x01122000, "RealmService::RealmGatewayAPI::removeInvite"),  # size=416, subsystem=Networking
    (0x011221a0, "RealmService::RealmGatewayAPI::kickAvatar"),  # size=416, subsystem=Networking
    (0x01122340, "RealmService::RealmGatewayAPI::modifyRoomBanner"),  # size=416, subsystem=Networking
    (0x011224e0, "RealmService::RealmGatewayAPI::createPrivateGame"),  # size=416, subsystem=Networking
    (0x01122680, "RealmService::RealmGatewayAPI::createPublicGame"),  # size=492, subsystem=Networking
    (0x01122870, "RealmService::RealmGatewayAPI::matchGame"),  # size=500, subsystem=Networking
    (0x01122a68, "RealmService::RealmGatewayAPI::cancelGame"),  # size=392, subsystem=Networking
    (0x01122bf0, "RealmService::RealmGatewayAPI::getGame"),  # size=404, subsystem=Networking
    (0x01122d88, "RealmService::RealmGatewayAPI::startGame"),  # size=948, subsystem=Networking
    (0x01123140, "RealmService::RealmGatewayAPI::recordGameOutcome"),  # size=1196, subsystem=Networking
    (0x011235f0, "RealmService::RealmGatewayAPI::doClientDiscovery"),  # size=416, subsystem=Networking
    (0x01123790, "RealmService::RealmGatewayAPI::packDiscoveryPacket"),  # size=432, subsystem=Networking
    (0x01123940, "RealmService::RealmGatewayAPI::changePassword"),  # size=888, subsystem=Networking
    (0x01123cb8, "RealmService::RealmGatewayAPI::changeEmail"),  # size=888, subsystem=Networking
    (0x01124030, "RealmService::RealmGatewayAPI::updateGameData"),  # size=416, subsystem=Networking
    (0x011242d0, "RealmService::RealmGatewayAPI::process"),  # size=28, subsystem=Networking
    (0x011242f0, "RealmService::RealmGatewayAPI::getUserInfo"),  # size=136, subsystem=Networking
    (0x01124378, "RealmService::RealmGatewayAPI::getUserStats"),  # size=136, subsystem=Networking
    (0x01124400, "RealmService::RealmGatewayAPI::getRealmTime"),  # size=124, subsystem=Networking
    (0x01124480, "RealmService::RealmGatewayAPI::getRealmStats"),  # size=128, subsystem=Networking
    (0x01124500, "RealmService::RealmGatewayAPI::roundTrip"),  # size=124, subsystem=Networking
    (0x01124580, "RealmService::RealmGatewayAPI::getRules"),  # size=152, subsystem=Networking
    (0x01124618, "VISoundDevice::constructor"),  # size=332, subsystem=Engine (VISoundDevice)
    (0x01124768, "VISoundDevice::Init"),  # size=320, subsystem=Engine (VISoundDevice)
    (0x011248a8, "VISoundDevice::Reset"),  # size=664, subsystem=Engine (VISoundDevice)
    (0x01124b40, "VISoundDevice::Process"),  # size=8, subsystem=Engine (VISoundDevice)
    (0x01124b48, "VISoundDevice::CreateSound"),  # size=296, subsystem=Engine (VISoundDevice)
    (0x01124c70, "VISoundDevice::StreamBgm"),  # size=476, subsystem=Engine (VISoundDevice)
    (0x01124e50, "VISoundDevice::Play"),  # size=1104, subsystem=Engine (VISoundDevice)
    (0x011252a0, "VISoundDevice::Stop"),  # size=260, subsystem=Engine (VISoundDevice)
    (0x011253a8, "VISoundDevice::SetPitch"),  # size=360, subsystem=Engine (VISoundDevice)
    (0x01125510, "VISoundDevice::SetVolume"),  # size=656, subsystem=Engine (VISoundDevice)
    (0x011257a0, "VISoundDevice::SetPan"),  # size=660, subsystem=Engine (VISoundDevice)
    (0x01125a38, "VISoundDevice::Flush"),  # size=388, subsystem=Engine (VISoundDevice)
    (0x01125bc0, "VISoundDevice::AllocateChannels"),  # size=412, subsystem=Engine (VISoundDevice)
    (0x01125d60, "VISoundDevice::InitSpuMem"),  # size=208, subsystem=Engine (VISoundDevice)
    (0x01125e30, "VISoundDevice::AllocXmMem"),  # size=316, subsystem=Engine (VISoundDevice)
    (0x01125f70, "VISoundDevice::IdleTransfer"),  # size=480, subsystem=Engine (VISoundDevice)
    (0x01126150, "VISoundDevice::DebugResources"),  # size=316, subsystem=Engine (VISoundDevice)
    (0x01126290, "VISoundDevice::~destructor"),  # size=148, subsystem=Engine (VISoundDevice)
    (0x01126328, "VISoundDevice::SetBgmVersion"),  # size=12, subsystem=Engine (VISoundDevice)
    (0x01126338, "VISoundDevice::BgmVersion"),  # size=12, subsystem=Engine (VISoundDevice)
    (0x01126348, "VISoundDevice::Close"),  # size=32, subsystem=Engine (VISoundDevice)
    (0x01126368, "VISoundDevice::Sound"),  # size=32, subsystem=Engine (VISoundDevice)
    (0x01126388, "VISoundDevice::ShareSound"),  # size=44, subsystem=Engine (VISoundDevice)
    (0x011263b8, "VISoundDevice::ReleaseSound"),  # size=260, subsystem=Engine (VISoundDevice)
    (0x011264c0, "VISoundDevice::PlayBgm"),  # size=44, subsystem=Engine (VISoundDevice)
    (0x011264f0, "VISoundDevice::StopBgm"),  # size=112, subsystem=Engine (VISoundDevice)
    (0x01126560, "VISoundDevice::StopAllBgm"),  # size=72, subsystem=Engine (VISoundDevice)
    (0x011265a8, "VISoundDevice::IsBgmPlaying"),  # size=12, subsystem=Engine (VISoundDevice)
    (0x011265b8, "VISoundDevice::SetBgmVolume"),  # size=8, subsystem=Engine (VISoundDevice)
    (0x011265c0, "VISoundDevice::EnableBgmFading"),  # size=8, subsystem=Engine (VISoundDevice)
    (0x011265c8, "VISoundDevice::BgmBufferSize"),  # size=36, subsystem=Engine (VISoundDevice)
    (0x011265f0, "VISoundDevice::IsPlaying"),  # size=32, subsystem=Engine (VISoundDevice)
    (0x01126610, "VISoundDevice::Pitch"),  # size=44, subsystem=Engine (VISoundDevice)
    (0x01126640, "VISoundDevice::Volume"),  # size=40, subsystem=Engine (VISoundDevice)
    (0x01126668, "VISoundDevice::Pan"),  # size=40, subsystem=Engine (VISoundDevice)
    (0x01126690, "VISoundDevice::SetSoundClassVolume"),  # size=136, subsystem=Engine (VISoundDevice)
    (0x01126718, "VISoundDevice::SetOutputMode"),  # size=104, subsystem=Engine (VISoundDevice)
    (0x01126780, "VISoundDevice::CreateDevice"),  # size=8, subsystem=Engine (VISoundDevice)
    (0x01126788, "VISoundDevice::ReleaseDevice"),  # size=8, subsystem=Engine (VISoundDevice)
    (0x01126790, "VISoundDevice::DeallocateChannels"),  # size=20, subsystem=Engine (VISoundDevice)
    (0x011267a8, "VISoundDevice::ChannelCount"),  # size=56, subsystem=Engine (VISoundDevice)
    (0x011267e0, "VISoundDevice::StopChannels"),  # size=140, subsystem=Engine (VISoundDevice)
    (0x01126870, "VISoundDevice::FirstChannel"),  # size=68, subsystem=Engine (VISoundDevice)
    (0x011268b8, "VISoundDevice::NextChannel"),  # size=76, subsystem=Engine (VISoundDevice)
    (0x01126908, "VISoundDevice::NewPlayback"),  # size=76, subsystem=Engine (VISoundDevice)
    (0x01126958, "VISoundDevice::DeletePlayback"),  # size=64, subsystem=Engine (VISoundDevice)
    (0x01126998, "VISoundDevice::Playback"),  # size=72, subsystem=Engine (VISoundDevice)
    (0x011269e0, "VISoundDevice::FirstPlayback"),  # size=16, subsystem=Engine (VISoundDevice)
    (0x011269f0, "VISoundDevice::NextPlayback"),  # size=16, subsystem=Engine (VISoundDevice)
    (0x01126a00, "VISoundDevice::CloseSpuMem"),  # size=68, subsystem=Engine (VISoundDevice)
    (0x01126a48, "VISoundDevice::AllocSpuMem"),  # size=188, subsystem=Engine (VISoundDevice)
    (0x01126b08, "VISoundDevice::FreeSpuMem"),  # size=188, subsystem=Engine (VISoundDevice)
    (0x01126bc8, "VISoundDevice::MergeFreeSpuMem"),  # size=156, subsystem=Engine (VISoundDevice)
    (0x01126c68, "VISoundDevice::InitXmMem"),  # size=252, subsystem=Engine (VISoundDevice)
    (0x01126d68, "VISoundDevice::CloseXmMem"),  # size=72, subsystem=Engine (VISoundDevice)
    (0x01126db0, "VISoundDevice::FreeXmMem"),  # size=220, subsystem=Engine (VISoundDevice)
    (0x01126e90, "VISoundDevice::MergeFreeXmMem"),  # size=156, subsystem=Engine (VISoundDevice)
    (0x01126f30, "VISoundDevice::BeginAdpcmTransfer"),  # size=48, subsystem=Engine (VISoundDevice)
    (0x01126f60, "VISoundDevice::BeginXmTransfer"),  # size=52, subsystem=Engine (VISoundDevice)
    (0x01127128, "VIZoneTree::constructor"),  # size=40, subsystem=Engine (VIZoneTree)
    (0x01127150, "VIZoneTree::~destructor"),  # size=108, subsystem=Engine (VIZoneTree)
    (0x011271c0, "VIZoneTree::Init"),  # size=92, subsystem=Engine (VIZoneTree)
    (0x01127220, "VIZoneTree::Clear"),  # size=80, subsystem=Engine (VIZoneTree)
    (0x01127270, "RealmService::ReqGetEncryptionKey::pack"),  # size=200, subsystem=Networking
    (0x01127338, "RealmService::ReqGetServerAddress::pack"),  # size=152, subsystem=Networking
    (0x01127578, "RealmService::ReqAddBan::pack"),  # size=164, subsystem=Networking
    (0x011279f8, "RealmService::ReqAddInvite::pack"),  # size=164, subsystem=Networking
    (0x01127c48, "RealmService::ReqAddRoomModerator::pack"),  # size=164, subsystem=Networking
    (0x01127e18, "RealmService::ReqConsumeKey::pack"),  # size=208, subsystem=Networking
    (0x01128040, "RealmService::ReqCreateAccount::pack"),  # size=176, subsystem=Networking
    (0x01128298, "RealmService::ReqCreatePrivateGame::pack"),  # size=164, subsystem=Networking
    (0x01128648, "RealmService::ReqCreatePublicGame::pack"),  # size=272, subsystem=Networking
    (0x01128888, "RealmService::ReqDoClientDiscovery::pack"),  # size=176, subsystem=Networking
    (0x01128fd8, "RealmService::ReqKickAvatar::pack"),  # size=164, subsystem=Networking
    (0x01129198, "RealmService::ReqMatchGame::pack"),  # size=312, subsystem=Networking
    (0x01129478, "RealmService::ReqModifyRoomBanner::pack"),  # size=164, subsystem=Networking
    (0x01129688, "RealmService::ReqRecordGameOutcome::pack"),  # size=540, subsystem=Networking
    (0x01129a50, "RealmService::ReqRemoveBan::pack"),  # size=164, subsystem=Networking
    (0x01129ed0, "RealmService::ReqRemoveInvite::pack"),  # size=164, subsystem=Networking
    (0x0112a120, "RealmService::ReqRemoveRoomModerator::pack"),  # size=164, subsystem=Networking
    (0x0112a370, "RealmService::ReqSendInstantMessage::pack"),  # size=164, subsystem=Networking
    (0x0112a5c0, "RealmService::ReqSendRoomMessage::pack"),  # size=164, subsystem=Networking
    (0x0112a7b8, "RealmService::ReqStartGame::pack"),  # size=452, subsystem=Networking
    (0x0112aaa0, "RealmService::ReqChangePassword::pack"),  # size=164, subsystem=Networking
    (0x0112ac68, "RealmService::ReqChangeEmail::pack"),  # size=164, subsystem=Networking
    (0x0112af00, "RealmService::ReqAddFriend::pack"),  # size=152, subsystem=Networking
    (0x0112af98, "RealmService::ReqAddIgnore::pack"),  # size=152, subsystem=Networking
    (0x0112b0b8, "RealmService::ReqCancelGame::pack"),  # size=140, subsystem=Networking
    (0x0112b1d0, "RealmService::ReqCreateAvatar::pack"),  # size=140, subsystem=Networking
    (0x0112b260, "RealmService::ReqCreatePrivateRoom::pack"),  # size=152, subsystem=Networking
    (0x0112b380, "RealmService::ReqDestroyAvatar::pack"),  # size=140, subsystem=Networking
    (0x0112b410, "RealmService::ReqEnterRoom::pack"),  # size=152, subsystem=Networking
    (0x0112b4a8, "RealmService::ReqGetGame::pack"),  # size=152, subsystem=Networking
    (0x0112b5c8, "RealmService::ReqGetPublicRooms::pack"),  # size=140, subsystem=Networking
    (0x0112b6a0, "RealmService::ReqGetRealmStats::pack"),  # size=128, subsystem=Networking
    (0x0112b768, "RealmService::ReqGetRealmTime::pack"),  # size=128, subsystem=Networking
    (0x0112b7e8, "RealmService::ReqGetRoom::pack"),  # size=152, subsystem=Networking
    (0x0112b880, "RealmService::ReqGetUserInfo::pack"),  # size=140, subsystem=Networking
    (0x0112b910, "RealmService::ReqGetUserStats::pack"),  # size=140, subsystem=Networking
    (0x0112b9a0, "RealmService::ReqLeaveRoom::pack"),  # size=152, subsystem=Networking
    (0x0112bb10, "RealmService::ReqLogin::pack"),  # size=152, subsystem=Networking
    (0x0112bc30, "RealmService::ReqLogout::pack"),  # size=140, subsystem=Networking
    (0x0112bdc0, "RealmService::ReqRemoveFriend::pack"),  # size=152, subsystem=Networking
    (0x0112be58, "RealmService::ReqRemoveIgnore::pack"),  # size=152, subsystem=Networking
    (0x0112bf38, "RealmService::ReqRoundTrip::pack"),  # size=128, subsystem=Networking
    (0x0112c040, "RealmService::ReqTouchSession::pack"),  # size=140, subsystem=Networking
    (0x0112c0d0, "RealmService::ReqGetRules::pack"),  # size=152, subsystem=Networking
    (0x0112c218, "RealmService::ReqUpdateGameData::pack"),  # size=152, subsystem=Networking
    (0x0112c2b0, "VISurface::CalcSurfaceOffsets"),  # size=592, subsystem=Engine (VISurface)
    (0x0112c500, "VISurface::SetDMAHeaders"),  # size=336, subsystem=Engine (VISurface)
    (0x0112c650, "VISurface::ReorderPalette"),  # size=256, subsystem=Engine (VISurface)
    (0x0112c750, "VISurface::constructor"),  # size=116, subsystem=Engine (VISurface)
    (0x0112c7c8, "VISurface::~destructor"),  # size=84, subsystem=Engine (VISurface)
    (0x0112c820, "VISurface::Init"),  # size=304, subsystem=Engine (VISurface)
    (0x0112c950, "VISurface::LockMipLevel"),  # size=100, subsystem=Engine (VISurface)
    (0x0112c9b8, "VISurface::UnlockMipLevel"),  # size=32, subsystem=Engine (VISurface)
    (0x0112c9d8, "VISurface::LockPalette"),  # size=168, subsystem=Engine (VISurface)
    (0x0112ca80, "VISurface::UnlockPalette"),  # size=68, subsystem=Engine (VISurface)
    (0x0112cac8, "VISurface::Allocate"),  # size=72, subsystem=Engine (VISurface)
    (0x0112cb10, "VISurface::Deallocate"),  # size=108, subsystem=Engine (VISurface)
    (0x0112cb80, "VISurface::CalcMipLevelStride"),  # size=120, subsystem=Engine (VISurface)
    (0x0112d1c0, "RealmService::RealmResponse::populatePtrVector"),  # size=212, subsystem=Networking
    (0x0112d298, "RealmService::ResGetEncryptionKey::unpack"),  # size=312, subsystem=Networking
    (0x0112d3d0, "RealmService::ResGetServerAddress::unpack"),  # size=228, subsystem=Networking
    (0x0112d4b8, "RealmService::ResTouchSession::unpack"),  # size=164, subsystem=Networking
    (0x0112d560, "RealmService::ResAddBan::unpack"),  # size=164, subsystem=Networking
    (0x0112d608, "RealmService::ResAddFriend::unpack"),  # size=164, subsystem=Networking
    (0x0112d6b0, "RealmService::ResAddIgnore::unpack"),  # size=164, subsystem=Networking
    (0x0112d758, "RealmService::ResAddInvite::unpack"),  # size=164, subsystem=Networking
    (0x0112d800, "RealmService::ResAddRoomModerator::unpack"),  # size=164, subsystem=Networking
    (0x0112d8a8, "RealmService::ResCancelGame::unpack"),  # size=164, subsystem=Networking
    (0x0112d950, "RealmService::ResConsumeKey::unpack"),  # size=184, subsystem=Networking
    (0x0112da08, "RealmService::ResCreateAccount::unpack"),  # size=184, subsystem=Networking
    (0x0112db40, "RealmService::ResCreateAvatar::unpack"),  # size=988, subsystem=Networking
    (0x0112df20, "RealmService::ResCreatePrivateGame::unpack"),  # size=228, subsystem=Networking
    (0x0112e108, "RealmService::ResCreatePrivateRoom::unpack"),  # size=1012, subsystem=Networking
    (0x0112e500, "RealmService::ResCreatePublicGame::unpack"),  # size=228, subsystem=Networking
    (0x0112e5e8, "RealmService::ResDestroyAvatar::unpack"),  # size=164, subsystem=Networking
    (0x0112e690, "RealmService::ResDoClientDiscovery::unpack"),  # size=228, subsystem=Networking
    (0x0112e878, "RealmService::ResEnterRoom::unpack"),  # size=1012, subsystem=Networking
    (0x0112ed38, "RealmService::ResGetGame::unpack"),  # size=240, subsystem=Networking
    (0x0112ef08, "RealmService::ResGetPublicRooms::unpack"),  # size=1388, subsystem=Networking
    (0x0112f478, "RealmService::ResGetRealmStats::unpack"),  # size=504, subsystem=Networking
    (0x0112f670, "RealmService::ResGetRealmTime::unpack"),  # size=208, subsystem=Networking
    (0x0112f840, "RealmService::ResGetRoom::unpack"),  # size=1012, subsystem=Networking
    (0x0112fc38, "RealmService::ResGetUserInfo::unpack"),  # size=336, subsystem=Networking
    (0x0112fd88, "RealmService::ResGetUserStats::unpack"),  # size=472, subsystem=Networking
    (0x0112ff60, "RealmService::ResKickAvatar::unpack"),  # size=164, subsystem=Networking
    (0x01130008, "RealmService::ResLeaveRoom::unpack"),  # size=164, subsystem=Networking
    (0x011300b0, "RealmService::ResLogin::unpack"),  # size=184, subsystem=Networking
    (0x01130168, "RealmService::ResLogout::unpack"),  # size=164, subsystem=Networking
    (0x011302d0, "RealmService::ResMatchGame::unpack"),  # size=1760, subsystem=Networking
    (0x011309b0, "RealmService::ResModifyRoomBanner::unpack"),  # size=164, subsystem=Networking
    (0x01130a58, "RealmService::ResRecordGameOutcome::unpack"),  # size=164, subsystem=Networking
    (0x01130b00, "RealmService::ResRemoveBan::unpack"),  # size=164, subsystem=Networking
    (0x01130ba8, "RealmService::ResRemoveFriend::unpack"),  # size=164, subsystem=Networking
    (0x01130c50, "RealmService::ResRemoveIgnore::unpack"),  # size=164, subsystem=Networking
    (0x01130cf8, "RealmService::ResRemoveInvite::unpack"),  # size=164, subsystem=Networking
    (0x01130da0, "RealmService::ResRemoveRoomModerator::unpack"),  # size=164, subsystem=Networking
    (0x01130e48, "RealmService::ResRoundTrip::unpack"),  # size=164, subsystem=Networking
    (0x01130ef0, "RealmService::ResSendInstantMessage::unpack"),  # size=164, subsystem=Networking
    (0x01130f98, "RealmService::ResSendRoomMessage::unpack"),  # size=164, subsystem=Networking
    (0x01131040, "RealmService::ResStartGame::unpack"),  # size=208, subsystem=Networking
    (0x01131110, "RealmService::ResChangePassword::unpack"),  # size=164, subsystem=Networking
    (0x011311b8, "RealmService::ResChangeEmail::unpack"),  # size=164, subsystem=Networking
    (0x01131260, "RealmService::ResGetRules::unpack"),  # size=184, subsystem=Networking
    (0x01131318, "RealmService::ResUpdateGameData::unpack"),  # size=164, subsystem=Networking
    (0x01131ff0, "VIEESurfCache::Clear"),  # size=252, subsystem=Engine (VIEESurfCache)
    (0x011320f0, "VIEESurfCache::Cache"),  # size=804, subsystem=Engine (VIEESurfCache)
    (0x01132418, "VIEESurfCache::Decache"),  # size=240, subsystem=Engine (VIEESurfCache)
    (0x01132508, "VIEESurfCache::CalcCacheInfo"),  # size=756, subsystem=Engine (VIEESurfCache)
    (0x01132800, "VIEESurfCache::Set"),  # size=800, subsystem=Engine (VIEESurfCache)
    (0x01132b20, "VIEESurfCache::AddToFreeMap"),  # size=148, subsystem=Engine (VIEESurfCache)
    (0x01132bb8, "VIEESurfCache::FindLRU"),  # size=320, subsystem=Engine (VIEESurfCache)
    (0x01132cf8, "VIEESurfCache::FindFree"),  # size=252, subsystem=Engine (VIEESurfCache)
    (0x01132df8, "VIEESurfCache::Allocate"),  # size=596, subsystem=Engine (VIEESurfCache)
    (0x01133050, "VIEESurfCache::Deallocate"),  # size=1436, subsystem=Engine (VIEESurfCache)
    (0x011335f0, "VIEESurfCache::MoveToLRUEnd"),  # size=380, subsystem=Engine (VIEESurfCache)
    (0x01133770, "VIEESurfCache::RemoveFromLRU"),  # size=284, subsystem=Engine (VIEESurfCache)
    (0x01133890, "VIEESurfCache::ConstructDMAPacket"),  # size=912, subsystem=Engine (VIEESurfCache)
    (0x01133c20, "VIEESurfCache::Init"),  # size=56, subsystem=Engine (VIEESurfCache)
    (0x01133c58, "VIEESurfCache::EnableDownloads"),  # size=16, subsystem=Engine (VIEESurfCache)
    (0x01133c68, "VIEESurfCache::Log2"),  # size=44, subsystem=Engine (VIEESurfCache)
    (0x01133c98, "VIEESurfCache::RemoveFromFreeMap"),  # size=124, subsystem=Engine (VIEESurfCache)
    (0x01133d18, "VIEESurfCache::Download"),  # size=100, subsystem=Engine (VIEESurfCache)
    (0x01133d80, "VIEESurfCache::DebugVerify"),  # size=8, subsystem=Engine (VIEESurfCache)
    (0x011341d8, "VITimeOfDay::GetLocalTime"),  # size=364, subsystem=Engine (VITimeOfDay)
    (0x01134348, "VITimeOfDay::GetDayOfWeek"),  # size=432, subsystem=Engine (VITimeOfDay)
    (0x011344f8, "VITimer::Init"),  # size=124, subsystem=Engine (VITimer)
    (0x01134578, "VITimer::Close"),  # size=60, subsystem=Engine (VITimer)
    (0x011345b8, "VITimer::Handler"),  # size=56, subsystem=Engine (VITimer)
    (0x011345f0, "VITimer::GetTime"),  # size=12, subsystem=Engine (VITimer)
    (0x01134600, "VITimeOfDay::GetLocalTime"),  # size=76, subsystem=Engine (VITimeOfDay)
    (0x01134650, "VITimeOfDay::GetMonth"),  # size=240, subsystem=Engine (VITimeOfDay)
    (0x01134740, "VITimeOfDay::GetDayOfWeek"),  # size=192, subsystem=Engine (VITimeOfDay)
    (0x01134800, "VIRFont::CreateResources"),  # size=532, subsystem=Font
    (0x01134a18, "VIRFont::Cache"),  # size=972, subsystem=Font
    (0x01134de8, "VIRFont::Cache"),  # size=972, subsystem=Font
    (0x011351b8, "VIRFont::GetWidth"),  # size=384, subsystem=Font
    (0x01135338, "VIRFont::GetWidth"),  # size=376, subsystem=Font
    (0x011354b0, "VIRFont::GetStringWidth"),  # size=396, subsystem=Font
    (0x01135640, "VIRFont::GetStringWidth"),  # size=396, subsystem=Font
    (0x011357d0, "VIRFont::InitSlots"),  # size=548, subsystem=Font
    (0x011359f8, "VIRFont::InitChars"),  # size=288, subsystem=Font
    (0x01135b18, "VIRFont::ResetCache"),  # size=356, subsystem=Font
    (0x01135c80, "VIRFont::CalcDataSize"),  # size=320, subsystem=Font
    (0x01135dc0, "VIRFont::constructor"),  # size=36, subsystem=Font
    (0x01135de8, "VIRFont::~destructor"),  # size=84, subsystem=Font
    (0x01135e40, "VIRFont::Init"),  # size=304, subsystem=Font
    (0x01135f70, "VIRFont::Clear"),  # size=148, subsystem=Font
    (0x01136008, "VIRFont::IsPalettized"),  # size=12, subsystem=Font
    (0x01136018, "VIRFont::PixelStore"),  # size=8, subsystem=Font
    (0x01136020, "VIRFont::PalettePixelStore"),  # size=8, subsystem=Font
    (0x01136028, "VIRFont::Lock"),  # size=32, subsystem=Font
    (0x01136048, "VIRFont::Unlock"),  # size=60, subsystem=Font
    (0x01136088, "VIRFont::Palette"),  # size=48, subsystem=Font
    (0x011360b8, "VIRFont::BeginChar"),  # size=60, subsystem=Font
    (0x011360f8, "VIRFont::EndChar"),  # size=20, subsystem=Font
    (0x01136110, "VIRFont::ReleaseResources"),  # size=112, subsystem=Font
    (0x01136180, "VIRFont::FindChar"),  # size=132, subsystem=Font
    (0x01136208, "VIRFont::CalcMaxWidth"),  # size=68, subsystem=Font
    (0x01136250, "VIRFont::Allocate"),  # size=72, subsystem=Font
    (0x01137fd8, "VIWave::constructor"),  # size=32, subsystem=Audio
    (0x01137ff8, "VIWave::~destructor"),  # size=108, subsystem=Audio
    (0x01138068, "VIWave::Create"),  # size=200, subsystem=Audio
    (0x01138130, "VIWave::Destroy"),  # size=44, subsystem=Audio
    (0x01138180, "VIWave::LockBuffer"),  # size=28, subsystem=Audio
    (0x011381a0, "VIWave::UnlockBuffer"),  # size=28, subsystem=Audio
    (0x011381c8, "VIWave::SetVolume"),  # size=8, subsystem=Audio
    (0x011381d8, "VIWave::SetPan"),  # size=8, subsystem=Audio
    (0x011381e0, "VIWave::IsCached"),  # size=12, subsystem=Audio
    (0x011381f8, "VIWave::SetSampleRate"),  # size=8, subsystem=Audio
    (0x01138200, "VIWave::Allocate"),  # size=152, subsystem=Audio
    (0x01138298, "VIWave::Deallocate"),  # size=84, subsystem=Audio
    (0x011382f0, "VISceneFilter::constructor"),  # size=32, subsystem=Engine (VISceneFilter)
    (0x01138310, "VISceneFilter::Init"),  # size=28, subsystem=Engine (VISceneFilter)
    (0x01138330, "VISceneFilter::Init"),  # size=28, subsystem=Engine (VISceneFilter)
    (0x01138350, "VISceneFilter::FilterActor"),  # size=16, subsystem=Engine (VISceneFilter)
    (0x0113a680, "VIXm::constructor"),  # size=52, subsystem=Engine (VIXm)
    (0x0113a6b8, "VIXm::~destructor"),  # size=108, subsystem=Engine (VIXm)
    (0x0113a728, "VIXm::Create"),  # size=136, subsystem=Engine (VIXm)
    (0x0113a7b0, "VIXm::Destroy"),  # size=120, subsystem=Engine (VIXm)
    (0x0113a830, "VIXm::SetVolume"),  # size=8, subsystem=Engine (VIXm)
    (0x0113a840, "VIXm::SetPan"),  # size=8, subsystem=Engine (VIXm)
    (0x0113a848, "VIXm::IsCached"),  # size=36, subsystem=Engine (VIXm)
    (0x0113a870, "VIXm::SetRepeat"),  # size=8, subsystem=Engine (VIXm)
    (0x0113a890, "VIScene::constructor"),  # size=588, subsystem=Scene
    (0x0113aae0, "VIScene::~destructor"),  # size=324, subsystem=Scene
    (0x0113ac28, "VIScene::Init"),  # size=924, subsystem=Scene
    (0x0113afc8, "VIScene::Clear"),  # size=836, subsystem=Scene
    (0x0113b310, "VIScene::SetSky"),  # size=284, subsystem=Scene
    (0x0113b430, "VIScene::SetSoundTrack"),  # size=1592, subsystem=Scene
    (0x0113ba68, "VIScene::StopSoundTrack"),  # size=224, subsystem=Scene
    (0x0113bb48, "VIScene::Render"),  # size=912, subsystem=Scene
    (0x0113bed8, "VIScene::RenderShadow"),  # size=2300, subsystem=Scene
    (0x0113c7d8, "VIScene::QueryProximalActors"),  # size=180, subsystem=Scene
    (0x0113c890, "VIScene::QueryVisibleActors"),  # size=248, subsystem=Scene
    (0x0113c988, "VIScene::QueryActorsInVolume"),  # size=268, subsystem=Scene
    (0x0113ca98, "VIScene::CreateSprite"),  # size=688, subsystem=Scene
    (0x0113cd48, "VIScene::ReleaseSprite"),  # size=272, subsystem=Scene
    (0x0113ce58, "VIScene::ReleaseRefMap"),  # size=180, subsystem=Scene
    (0x0113cf10, "VIScene::ReleaseStaticLighting"),  # size=216, subsystem=Scene
    (0x0113cfe8, "VIScene::SetPersonalLight"),  # size=288, subsystem=Scene
    (0x0113d108, "VIScene::SetSky"),  # size=368, subsystem=Scene
    (0x0113d4a8, "VIScene::UpdateSoundEmitters"),  # size=1500, subsystem=Scene
    (0x0113da88, "VIScene::DebugResources"),  # size=1168, subsystem=Scene
    (0x0113df18, "VIScene::Collide"),  # size=180, subsystem=Scene
    (0x0113dfd0, "VIScene::Collide"),  # size=172, subsystem=Scene
    (0x0113e080, "VIScene::Pick"),  # size=172, subsystem=Scene
    (0x0113e130, "VIScene::StreamFillCache"),  # size=312, subsystem=Scene
    (0x0113e268, "VIScene::StreamFillCache"),  # size=1008, subsystem=Scene
    (0x0113e658, "VIScene::Stream"),  # size=616, subsystem=Scene
    (0x0113e8c0, "VIScene::StreamClearCache"),  # size=256, subsystem=Scene
    (0x0113e9c0, "VIScene::ShareResource"),  # size=360, subsystem=Scene
    (0x0113eb28, "VIScene::ReleaseResource"),  # size=480, subsystem=Scene
    (0x0113ed08, "VIScene::CreateActor"),  # size=500, subsystem=Scene
    (0x0113ef00, "VIScene::CreateStaticProxyActor"),  # size=344, subsystem=Scene
    (0x0113f058, "VIScene::ReleaseActor"),  # size=148, subsystem=Scene
    (0x0113f230, "VIScene::SetActorSprite"),  # size=340, subsystem=Scene
    (0x0113f388, "VIScene::InitTimeOfDay"),  # size=3780, subsystem=Scene
    (0x01140250, "VIScene::SetupTimeOfDayLights"),  # size=3056, subsystem=Scene
    (0x01140e40, "VIScene::SetupTimeOfDayFog"),  # size=2088, subsystem=Scene
    (0x01141668, "VIScene::CalcTimeOfDayClipPlanes"),  # size=280, subsystem=Scene
    (0x01141780, "VIScene::SetupTimeOfDaySky"),  # size=1780, subsystem=Scene
    (0x01141e78, "VIScene::CollideActor"),  # size=296, subsystem=Scene
    (0x01141fa0, "VIScene::CollideActor"),  # size=288, subsystem=Scene
    (0x011420c0, "VIScene::RasterActor"),  # size=492, subsystem=Scene
    (0x011422b0, "VIScene::RasterActorBBox"),  # size=3024, subsystem=Scene
    (0x01142e80, "VIScene::RenderDeferredList"),  # size=692, subsystem=Scene
    (0x01143138, "VIScene::PickActor"),  # size=328, subsystem=Scene
    (0x01143280, "VIScene::QueryProximalActor"),  # size=304, subsystem=Scene
    (0x011433b0, "VIScene::QueryVisibleActor"),  # size=356, subsystem=Scene
    (0x01143518, "VIScene::QueryEmittersAtLocation"),  # size=252, subsystem=Scene
    (0x01143618, "VIScene::QueryEmittersAtLocationActor"),  # size=236, subsystem=Scene
    (0x01143708, "VIScene::QueryEmittersActor"),  # size=236, subsystem=Scene
    (0x011437f8, "VIScene::QueryIntersection"),  # size=328, subsystem=Scene
    (0x01143940, "VIScene::CalcOutdoorsIntensity"),  # size=408, subsystem=Scene
    (0x01143ad8, "VIScene::UpdateActor"),  # size=436, subsystem=Scene
    (0x01143c90, "VIScene::UpdateProxyActor"),  # size=192, subsystem=Scene
    (0x01143d50, "VIScene::InsertActor"),  # size=260, subsystem=Scene
    (0x01143e58, "VIScene::RemoveActor"),  # size=304, subsystem=Scene
    (0x01143f88, "VIScene::RemoveActorsFromZone"),  # size=428, subsystem=Scene
    (0x01144138, "VIScene::ReplaceProxyRooms"),  # size=224, subsystem=Scene
    (0x01144218, "VIScene::ReplaceStaticProxyActors"),  # size=304, subsystem=Scene
    (0x01144348, "VIScene::ReplaceProxyActor"),  # size=344, subsystem=Scene
    (0x011444a0, "VIScene::ReleaseStatic"),  # size=712, subsystem=Scene
    (0x01144768, "VIScene::StreamInStaticActor"),  # size=448, subsystem=Scene
    (0x01144928, "VIScene::StreamOutStaticActor"),  # size=208, subsystem=Scene
    (0x011449f8, "VIScene::SetTime"),  # size=12, subsystem=Scene
    (0x01144a08, "VIScene::GetTime"),  # size=8, subsystem=Scene
    (0x01144a10, "VIScene::SetFarPlane"),  # size=84, subsystem=Scene
    (0x01144a68, "VIScene::CalcFarPlane"),  # size=80, subsystem=Scene
    (0x01144ab8, "VIScene::ClearShadowQueue"),  # size=8, subsystem=Scene
    (0x01144ac0, "VIScene::RenderShadows"),  # size=108, subsystem=Scene
    (0x01144b30, "VIScene::CopySprite"),  # size=88, subsystem=Scene
    (0x01144b88, "VIScene::GetSpriteType"),  # size=32, subsystem=Scene
    (0x01144ba8, "VIScene::Sprite"),  # size=28, subsystem=Scene
    (0x01144bc8, "VIScene::ShareSprite"),  # size=44, subsystem=Scene
    (0x01144bf8, "VIScene::RasterSprite"),  # size=100, subsystem=Scene
    (0x01144c60, "VIScene::RasterUISprite"),  # size=152, subsystem=Scene
    (0x01144cf8, "VIScene::GetNullSprite"),  # size=8, subsystem=Scene
    (0x01144d00, "VIScene::SetLightUISprite"),  # size=12, subsystem=Scene
    (0x01144d10, "VIScene::GetLightUISprite"),  # size=8, subsystem=Scene
    (0x01144d18, "VIScene::SetSoundUISprite"),  # size=12, subsystem=Scene
    (0x01144d28, "VIScene::GetSoundUISprite"),  # size=8, subsystem=Scene
    (0x01144d30, "VIScene::SetParticleUISprite"),  # size=12, subsystem=Scene
    (0x01144d40, "VIScene::GetParticleUISprite"),  # size=8, subsystem=Scene
    (0x01144d48, "VIScene::SetPointUISprite"),  # size=12, subsystem=Scene
    (0x01144d58, "VIScene::GetPointUISprite"),  # size=8, subsystem=Scene
    (0x01144d60, "VIScene::SetStreamAudioUISprite"),  # size=12, subsystem=Scene
    (0x01144d70, "VIScene::GetStreamAudioUISprite"),  # size=8, subsystem=Scene
    (0x01144d78, "VIScene::CreateAnimation"),  # size=132, subsystem=Scene
    (0x01144e00, "VIScene::Animation"),  # size=28, subsystem=Scene
    (0x01144e20, "VIScene::ShareAnimation"),  # size=44, subsystem=Scene
    (0x01144e50, "VIScene::ReleaseAnimation"),  # size=172, subsystem=Scene
    (0x01144f00, "VIScene::CreateRefMap"),  # size=164, subsystem=Scene
    (0x01144fa8, "VIScene::RefMap"),  # size=28, subsystem=Scene
    (0x01144fc8, "VIScene::ShareRefMap"),  # size=44, subsystem=Scene
    (0x01144ff8, "VIScene::CreateStaticLighting"),  # size=156, subsystem=Scene
    (0x01145098, "VIScene::StaticLighting"),  # size=28, subsystem=Scene
    (0x011450b8, "VIScene::ShareStaticLighting"),  # size=44, subsystem=Scene
    (0x011450e8, "VIScene::SetPersonalLightMode"),  # size=12, subsystem=Scene
    (0x011450f8, "VIScene::SetPersonalLight"),  # size=72, subsystem=Scene
    (0x01145140, "VIScene::SetRadialFloraMode"),  # size=12, subsystem=Scene
    (0x01145158, "VIScene::GetNextColorBuffer"),  # size=112, subsystem=Scene
    (0x011451c8, "VIScene::GetEnvFlags"),  # size=112, subsystem=Scene
    (0x01145238, "VIScene::SetPortals"),  # size=36, subsystem=Scene
    (0x01145260, "VIScene::GetWorldGridNumRows"),  # size=8, subsystem=Scene
    (0x01145268, "VIScene::GetWorldGridNumCols"),  # size=8, subsystem=Scene
    (0x01145270, "VIScene::GetWorldGridSize"),  # size=8, subsystem=Scene
    (0x01145278, "VIScene::GetWorldBBox"),  # size=8, subsystem=Scene
    (0x01145388, "VIScene::SetTimeOfDay"),  # size=36, subsystem=Scene
    (0x011453b0, "VIScene::Collide"),  # size=196, subsystem=Scene
    (0x01145478, "VIScene::Collide"),  # size=60, subsystem=Scene
    (0x011454b8, "VIScene::SetActorLighting"),  # size=136, subsystem=Scene
    (0x01145630, "VIScene::IsActorProxy"),  # size=16, subsystem=Scene
    (0x01145640, "VIScene::IsActorStatic"),  # size=16, subsystem=Scene
    (0x01145650, "VIScene::SetActorTransform"),  # size=104, subsystem=Scene
    (0x011456b8, "VIScene::GetActorTransform"),  # size=44, subsystem=Scene
    (0x011456e8, "VIScene::SetActorLocation"),  # size=68, subsystem=Scene
    (0x01145738, "VIScene::SetActorHPR"),  # size=68, subsystem=Scene
    (0x01145788, "VIScene::SetActorScale"),  # size=44, subsystem=Scene
    (0x01145810, "VIScene::SetActorVisibility"),  # size=44, subsystem=Scene
    (0x01145840, "VIScene::IsActorVisible"),  # size=16, subsystem=Scene
    (0x01145850, "VIScene::SetActorBBoxVisibility"),  # size=36, subsystem=Scene
    (0x01145878, "VIScene::IsActorBBoxVisible"),  # size=16, subsystem=Scene
    (0x01145888, "VIScene::SetActorCollideable"),  # size=44, subsystem=Scene
    (0x011458b8, "VIScene::IsActorCollideable"),  # size=20, subsystem=Scene
    (0x011458d0, "VIScene::SetActorAudible"),  # size=44, subsystem=Scene
    (0x01145900, "VIScene::IsActorAudible"),  # size=20, subsystem=Scene
    (0x01145918, "VIScene::SetActorID"),  # size=12, subsystem=Scene
    (0x01145928, "VIScene::GetActorID"),  # size=8, subsystem=Scene
    (0x01145930, "VIScene::SetActorBBoxDrawStyle"),  # size=12, subsystem=Scene
    (0x01145948, "VIScene::SetupTimeOfDay"),  # size=92, subsystem=Scene
    (0x011459a8, "VIScene::CollideSprite"),  # size=120, subsystem=Scene
    (0x01145a20, "VIScene::CollideSprite"),  # size=120, subsystem=Scene
    (0x01145a98, "VISceneDisplayElem::Compare"),  # size=116, subsystem=Engine (VISceneDisplayElem)
    (0x01145b10, "VIScene::PickSprite"),  # size=120, subsystem=Scene
    (0x01145b88, "VIScene::QueryVolumeActor"),  # size=176, subsystem=Scene
    (0x01145c38, "VIScene::QueryIntersectionActor"),  # size=244, subsystem=Scene
    (0x01145d30, "VIScene::QueryIntersectionSprite"),  # size=80, subsystem=Scene
    (0x01145d80, "VIScene::RemoveAllActors"),  # size=120, subsystem=Scene
    (0x01145df8, "VIScene::UpdateAllActors"),  # size=132, subsystem=Scene
    (0x01145e80, "VIScene::UpdateActors"),  # size=160, subsystem=Scene
    (0x01145f20, "VIScene::UpdateActors"),  # size=132, subsystem=Scene
    (0x01145fa8, "VIScene::StreamInCompleteActor"),  # size=56, subsystem=Scene
    (0x01145fe0, "VIScene::StreamHaltStaticActor"),  # size=96, subsystem=Scene
    (0x011466f8, "VIEffectVolume::GlobalInit"),  # size=2108, subsystem=Engine (VIEffectVolume)
    (0x01146f38, "VIEffectVolume::constructor"),  # size=148, subsystem=Engine (VIEffectVolume)
    (0x01146fd0, "VIEffectVolume::AttachSurface"),  # size=428, subsystem=Engine (VIEffectVolume)
    (0x01147180, "VIEffectVolume::DetachSurface"),  # size=192, subsystem=Engine (VIEffectVolume)
    (0x01147240, "VIEffectVolume::Process"),  # size=296, subsystem=Engine (VIEffectVolume)
    (0x01147368, "VIEffectVolume::Render"),  # size=1528, subsystem=Engine (VIEffectVolume)
    (0x01147960, "VIEffectVolume::AllocParticles"),  # size=476, subsystem=Engine (VIEffectVolume)
    (0x01147b40, "VIEffectVolume::ProcessFallingLeaves"),  # size=812, subsystem=Engine (VIEffectVolume)
    (0x01147e70, "VIEffectVolume::RenderFallingLeaves"),  # size=968, subsystem=Engine (VIEffectVolume)
    (0x01148238, "VIEffectVolume::ProcessLightShafts"),  # size=668, subsystem=Engine (VIEffectVolume)
    (0x011484d8, "VIEffectVolume::RenderLightShafts"),  # size=1992, subsystem=Engine (VIEffectVolume)
    (0x01148ca0, "VIEffectVolume::ProcessGroundFog"),  # size=656, subsystem=Engine (VIEffectVolume)
    (0x01148f30, "VIEffectVolume::RenderGroundFog"),  # size=1260, subsystem=Engine (VIEffectVolume)
    (0x01149420, "VIEffectVolume::ProcessDustStorm"),  # size=988, subsystem=Engine (VIEffectVolume)
    (0x01149800, "VIEffectVolume::RenderDustStorm"),  # size=1432, subsystem=Engine (VIEffectVolume)
    (0x01149d98, "VIEffectVolume::PrepareBillboardTransform"),  # size=572, subsystem=Engine (VIEffectVolume)
    (0x0114a110, "VIEffectVolume::GlobalFree"),  # size=12, subsystem=Engine (VIEffectVolume)
    (0x0114a120, "VIEffectVolume::~destructor"),  # size=44, subsystem=Engine (VIEffectVolume)
    (0x0114a150, "VIEffectVolume::Init"),  # size=180, subsystem=Engine (VIEffectVolume)
    (0x0114a208, "VIEffectVolume::Free"),  # size=44, subsystem=Engine (VIEffectVolume)
    (0x0114a240, "VIEffectVolume::SetType"),  # size=96, subsystem=Engine (VIEffectVolume)
    (0x0114a2a8, "VIEffectVolume::SetDensity"),  # size=16, subsystem=Engine (VIEffectVolume)
    (0x0114a2c0, "VIEffectVolume::SetFlags"),  # size=8, subsystem=Engine (VIEffectVolume)
    (0x0114a2c8, "VIEffectVolume::OnResize"),  # size=76, subsystem=Engine (VIEffectVolume)
    (0x0114a328, "VIEffectVolume::DetachAllResources"),  # size=52, subsystem=Engine (VIEffectVolume)
    (0x0114a360, "VIEffectVolume::FreeParticles"),  # size=56, subsystem=Engine (VIEffectVolume)
    (0x0114a3b8, "VISceneQuery::Init"),  # size=12, subsystem=Engine (VISceneQuery)
    (0x0114a3c8, "VISceneQuery::Init"),  # size=92, subsystem=Engine (VISceneQuery)
    (0x0114a428, "VISceneQuery::Clear"),  # size=80, subsystem=Engine (VISceneQuery)
    (0x0114a478, "VISceneQuery::FilterActor"),  # size=8, subsystem=Engine (VISceneQuery)
    (0x0114a480, "VISceneQuery::EndQuery"),  # size=136, subsystem=Engine (VISceneQuery)
    (0x0114df60, "VIEffectVolumeSprite::constructor"),  # size=124, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114dfe0, "VIEffectVolumeSprite::Init"),  # size=196, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e0a8, "VIEffectVolumeSprite::Raster"),  # size=1280, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e5a8, "VIEffectVolumeSprite::Copy"),  # size=324, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e6f0, "VIEffectVolumeSprite::~destructor"),  # size=116, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e770, "VIEffectVolumeSprite::Collide"),  # size=8, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e778, "VIEffectVolumeSprite::Collide"),  # size=8, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e780, "VIEffectVolumeSprite::Pick"),  # size=248, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e878, "VIEffectVolumeSprite::Release"),  # size=96, subsystem=Engine (VIEffectVolumeSprite)
    (0x0114e8d8, "VISceneSoundTrack::Clear"),  # size=140, subsystem=Engine (VISceneSoundTrack)
    (0x0114e968, "VISceneSoundTrackState::Init"),  # size=20, subsystem=Engine (VISceneSoundTrackState)
    (0x0114e980, "VISceneSoundTrackState::Clear"),  # size=44, subsystem=Engine (VISceneSoundTrackState)
    (0x0114e9b0, "VISceneSoundTrack::Init"),  # size=64, subsystem=Engine (VISceneSoundTrack)
    (0x0114e9f0, "VISceneSoundTrack::SetTracks"),  # size=320, subsystem=Engine (VISceneSoundTrack)
    (0x0114f330, "VIEmitterQuery::Init"),  # size=72, subsystem=Engine (VIEmitterQuery)
    (0x0114f378, "VIEmitterQuery::Clear"),  # size=64, subsystem=Engine (VIEmitterQuery)
    (0x0114f3b8, "VISetup::constructor"),  # size=656, subsystem=Setup/Config
    (0x0114f648, "VISetup::~destructor"),  # size=340, subsystem=Setup/Config
    (0x0114f7a0, "VISetup::Init"),  # size=964, subsystem=Setup/Config
    (0x0114fb68, "VISetup::Free"),  # size=224, subsystem=Setup/Config
    (0x0114fc48, "VISetup::Process"),  # size=1116, subsystem=Setup/Config
    (0x011500a8, "VISetup::MainLoopBegin"),  # size=628, subsystem=Setup/Config
    (0x01150320, "VISetup::MainLoopEnd"),  # size=216, subsystem=Setup/Config
    (0x011503f8, "VISetup::RunPatcher"),  # size=1408, subsystem=Setup/Config
    (0x01150978, "VISetup::OnTick"),  # size=336, subsystem=Setup/Config
    (0x01150b48, "VISetup::MainLoop"),  # size=72, subsystem=Setup/Config
    (0x01150bb8, "VISetup::RestartConnect"),  # size=124, subsystem=Setup/Config
    (0x01150c38, "VISetup::OnFile"),  # size=128, subsystem=Setup/Config
    (0x01150cb8, "VISetup::OnError"),  # size=40, subsystem=Setup/Config
    (0x01150ce0, "VISetup::HandleMemCardAbnormal"),  # size=168, subsystem=Setup/Config
    (0x01150d88, "VISetup::StartAmbientSoundtrack"),  # size=8, subsystem=Setup/Config
    (0x01150d90, "VISetup::StopAmbientSoundtrack"),  # size=8, subsystem=Setup/Config
    (0x01166de8, "VISimpleSprite::Copy"),  # size=340, subsystem=Engine (VISimpleSprite)
    (0x01166f40, "VISimpleSprite::constructor"),  # size=72, subsystem=Engine (VISimpleSprite)
    (0x01166f88, "VISimpleSprite::~destructor"),  # size=100, subsystem=Engine (VISimpleSprite)
    (0x01166ff0, "VISimpleSprite::Raster"),  # size=132, subsystem=Engine (VISimpleSprite)
    (0x01167078, "VISimpleSprite::Collide"),  # size=28, subsystem=Engine (VISimpleSprite)
    (0x01167098, "VISimpleSprite::Collide"),  # size=28, subsystem=Engine (VISimpleSprite)
    (0x011670b8, "VISimpleSprite::Pick"),  # size=128, subsystem=Engine (VISimpleSprite)
    (0x01167138, "VISimpleSprite::QueryIntersection"),  # size=96, subsystem=Engine (VISimpleSprite)
    (0x01167198, "VISimpleSprite::Release"),  # size=156, subsystem=Engine (VISimpleSprite)
    (0x01167248, "VISimpleSprite::SetMaterialPal"),  # size=88, subsystem=Engine (VISimpleSprite)
    (0x011672a0, "VISimpleSprite::SetMaterialPalDither"),  # size=132, subsystem=Engine (VISimpleSprite)
    (0x0116d118, "VIEnvRay::Init"),  # size=240, subsystem=Engine (VIEnvRay)
    (0x0116d268, "VIEnvRay::constructor"),  # size=84, subsystem=Engine (VIEnvRay)
    (0x0116d2c0, "VIEnvRay::Collide"),  # size=16, subsystem=Engine (VIEnvRay)
    (0x0116d2d8, "VITransEnvRay::Collide"),  # size=12, subsystem=Engine (VITransEnvRay)
    (0x0116d2e8, "VISkinSprite::Copy"),  # size=304, subsystem=Engine (VISkinSprite)
    (0x0116d418, "VISkinSprite::constructor"),  # size=60, subsystem=Engine (VISkinSprite)
    (0x0116d458, "VISkinSprite::~destructor"),  # size=100, subsystem=Engine (VISkinSprite)
    (0x0116d4c0, "VISkinSprite::SetVisible"),  # size=44, subsystem=Engine (VISkinSprite)
    (0x0116d4f0, "VISkinSprite::Raster"),  # size=72, subsystem=Engine (VISkinSprite)
    (0x0116d538, "VISkinSprite::Collide"),  # size=8, subsystem=Engine (VISkinSprite)
    (0x0116d540, "VISkinSprite::Collide"),  # size=8, subsystem=Engine (VISkinSprite)
    (0x0116d548, "VISkinSprite::Pick"),  # size=36, subsystem=Engine (VISkinSprite)
    (0x0116d570, "VISkinSprite::Release"),  # size=132, subsystem=Engine (VISkinSprite)
    (0x0116d600, "VISkinSprite::SetMaterialPal"),  # size=120, subsystem=Engine (VISkinSprite)
    (0x0116d738, "Base::CStatisticTimer::GetTime"),  # size=116, subsystem=Engine Utilities
    (0x0116d7b0, "Base::CStatisticTimer::GetFraction"),  # size=144, subsystem=Engine Utilities
    (0x0116d840, "VIESFParse::Parse"),  # size=288, subsystem=Engine (VIESFParse)
    (0x0116d960, "VIESFParse::Parse"),  # size=212, subsystem=Engine (VIESFParse)
    (0x0116da38, "VIESFParse::ParseZoneResource"),  # size=236, subsystem=Engine (VIESFParse)
    (0x0116db28, "VIESFParse::ParseSprite"),  # size=272, subsystem=Engine (VIESFParse)
    (0x0116dc38, "VIESFParse::ParseSound"),  # size=272, subsystem=Engine (VIESFParse)
    (0x0116dd48, "VIESFParse::ParseWorld"),  # size=284, subsystem=Engine (VIESFParse)
    (0x0116de68, "VIESFParse::ParseResourceFile"),  # size=288, subsystem=Engine (VIESFParse)
    (0x0116df88, "VIESFParse::ParseObject"),  # size=920, subsystem=Engine (VIESFParse)
    (0x0116e320, "VIESFParse::ParseSprite"),  # size=484, subsystem=Engine (VIESFParse)
    (0x0116e508, "VIESFParse::ParseSound"),  # size=156, subsystem=Engine (VIESFParse)
    (0x0116e5a8, "VIESFParse::ParsePrimBuffer"),  # size=3376, subsystem=Engine (VIESFParse)
    (0x0116f2d8, "VIESFParse::ParsePrimBufferObjV0"),  # size=800, subsystem=Engine (VIESFParse)
    (0x0116f5f8, "VIESFParse::ParseSkinPrimBuffer"),  # size=3192, subsystem=Engine (VIESFParse)
    (0x01170270, "VIESFParse::ParseSkinPrimBufferObjV0"),  # size=980, subsystem=Engine (VIESFParse)
    (0x01170648, "VIESFParse::ParseFloraPrimBuffer"),  # size=1544, subsystem=Engine (VIESFParse)
    (0x01170c50, "VIESFParse::ParseCollBuffer"),  # size=1884, subsystem=Engine (VIESFParse)
    (0x011713b0, "VIESFParse::ParseColorBuffer"),  # size=444, subsystem=Engine (VIESFParse)
    (0x01171570, "VIESFParse::ParseSurfaces"),  # size=208, subsystem=Engine (VIESFParse)
    (0x01171640, "VIESFParse::ParseSurfaceObj"),  # size=996, subsystem=Engine (VIESFParse)
    (0x01171a28, "VIESFParse::ParseMaterialPalObj"),  # size=644, subsystem=Engine (VIESFParse)
    (0x01171cb0, "VIESFParse::ParseMaterial"),  # size=164, subsystem=Engine (VIESFParse)
    (0x01171d58, "VIESFParse::ParseMaterial"),  # size=972, subsystem=Engine (VIESFParse)
    (0x01172128, "VIESFParse::ParseSimpleSpriteObj"),  # size=1032, subsystem=Engine (VIESFParse)
    (0x01172530, "VIESFParse::ParseHSpriteObj"),  # size=1016, subsystem=Engine (VIESFParse)
    (0x01172928, "VIESFParse::ParseHSpriteHierarchy"),  # size=740, subsystem=Engine (VIESFParse)
    (0x01172c10, "VIESFParse::ParseHSpriteTriggers"),  # size=212, subsystem=Engine (VIESFParse)
    (0x01172ce8, "VIESFParse::ParseHSpriteAttachments"),  # size=368, subsystem=Engine (VIESFParse)
    (0x01172e58, "VIESFParse::ParseHSpriteAnimArray"),  # size=264, subsystem=Engine (VIESFParse)
    (0x01172f60, "VIESFParse::ParseHSpriteAnimObj"),  # size=1856, subsystem=Engine (VIESFParse)
    (0x011736a0, "VIESFParse::ParseAdpcmObj"),  # size=420, subsystem=Engine (VIESFParse)
    (0x01173848, "VIESFParse::ParseXmObj"),  # size=472, subsystem=Engine (VIESFParse)
    (0x01173a20, "VIESFParse::ParseRefMap"),  # size=420, subsystem=Engine (VIESFParse)
    (0x01173bc8, "VIESFParse::ParseCSpriteObj"),  # size=1676, subsystem=Engine (VIESFParse)
    (0x01174258, "VIESFParse::ParseCSpriteSkinList"),  # size=292, subsystem=Engine (VIESFParse)
    (0x01174380, "VIESFParse::ParseCSpritePlayList"),  # size=776, subsystem=Engine (VIESFParse)
    (0x01174688, "VIESFParse::ParseCSpriteNodeIDList"),  # size=268, subsystem=Engine (VIESFParse)
    (0x01174798, "VIESFParse::ParseCSpriteASlotList"),  # size=256, subsystem=Engine (VIESFParse)
    (0x01174898, "VIESFParse::ParseCSpriteTSlotList"),  # size=308, subsystem=Engine (VIESFParse)
    (0x011749d0, "VIESFParse::ParseCSpriteContSound"),  # size=188, subsystem=Engine (VIESFParse)
    (0x01174a90, "VIESFParse::ParseCSpritePartDefinitions"),  # size=248, subsystem=Engine (VIESFParse)
    (0x01174b88, "VIESFParse::ParseCSpritePartEmitters"),  # size=508, subsystem=Engine (VIESFParse)
    (0x01174d88, "VIESFParse::ParseZoneResource"),  # size=880, subsystem=Engine (VIESFParse)
    (0x011750f8, "VIESFParse::ParseZoneBaseObj"),  # size=284, subsystem=Engine (VIESFParse)
    (0x01175218, "VIESFParse::ParseZoneTree"),  # size=428, subsystem=Engine (VIESFParse)
    (0x011753c8, "VIESFParse::ParseZonePreTranslations"),  # size=336, subsystem=Engine (VIESFParse)
    (0x01175518, "VIESFParse::ParseZoneRooms"),  # size=220, subsystem=Engine (VIESFParse)
    (0x011755f8, "VIESFParse::ParseZoneRoom"),  # size=676, subsystem=Engine (VIESFParse)
    (0x011758a0, "VIESFParse::ParseZoneRoomActorsObj"),  # size=324, subsystem=Engine (VIESFParse)
    (0x011759e8, "VIESFParse::ParseZoneActor"),  # size=384, subsystem=Engine (VIESFParse)
    (0x01175b68, "VIESFParse::ParseZoneRoomStaticLightingsObj"),  # size=332, subsystem=Engine (VIESFParse)
    (0x01175cb8, "VIESFParse::ParseZoneStaticTable"),  # size=276, subsystem=Engine (VIESFParse)
    (0x01175dd0, "VIESFParse::ParseZoneFloraSpriteArray"),  # size=224, subsystem=Engine (VIESFParse)
    (0x01175eb0, "VIESFParse::ParseZoneFloraSets"),  # size=552, subsystem=Engine (VIESFParse)
    (0x011760d8, "VIESFParse::ParseWorldObj"),  # size=168, subsystem=Engine (VIESFParse)
    (0x01176180, "VIESFParse::ParseWorldZones"),  # size=776, subsystem=Engine (VIESFParse)
    (0x01176488, "VIESFParse::ParseWorldBase"),  # size=248, subsystem=Engine (VIESFParse)
    (0x01176580, "VIESFParse::ParseWorldBaseHeader"),  # size=480, subsystem=Engine (VIESFParse)
    (0x01176760, "VIESFParse::ParseWorldZoneProxies"),  # size=480, subsystem=Engine (VIESFParse)
    (0x01176940, "VIESFParse::ParseWorldTree"),  # size=392, subsystem=Engine (VIESFParse)
    (0x01176ac8, "VIESFParse::ParseActorObj"),  # size=408, subsystem=Engine (VIESFParse)
    (0x01176c60, "VIESFParse::ParseResourceDirObj"),  # size=228, subsystem=Engine (VIESFParse)
    (0x01176d48, "VIESFParse::ParseResourceTable"),  # size=256, subsystem=Engine (VIESFParse)
    (0x01176e48, "VIESFParse::ParseFontObj"),  # size=1180, subsystem=Engine (VIESFParse)
    (0x011772e8, "VIESFParse::ParseLODSpriteObj"),  # size=648, subsystem=Engine (VIESFParse)
    (0x01177570, "VIESFParse::ParseLODSpriteSpriteArray"),  # size=244, subsystem=Engine (VIESFParse)
    (0x01177668, "VIESFParse::ParseLODSpriteLevels"),  # size=312, subsystem=Engine (VIESFParse)
    (0x011777a0, "VIESFParse::ParseSkinLODSpriteObj"),  # size=536, subsystem=Engine (VIESFParse)
    (0x011779b8, "VIESFParse::ParseSkinLODSpriteLevels"),  # size=312, subsystem=Engine (VIESFParse)
    (0x01177af0, "VIESFParse::ParseGroupSpriteObj"),  # size=536, subsystem=Engine (VIESFParse)
    (0x01177d08, "VIESFParse::ParseGroupSpriteMembers"),  # size=368, subsystem=Engine (VIESFParse)
    (0x01177e78, "VIESFParse::ParsePointLightObj"),  # size=492, subsystem=Engine (VIESFParse)
    (0x01178068, "VIESFParse::ParseSoundSpriteObj"),  # size=580, subsystem=Engine (VIESFParse)
    (0x011782b0, "VIESFParse::ParseParticleSpriteObj"),  # size=796, subsystem=Engine (VIESFParse)
    (0x011785d0, "VIESFParse::ParsePointSpriteObj"),  # size=276, subsystem=Engine (VIESFParse)
    (0x011786e8, "VIESFParse::ParseStreamAudioSpriteObj"),  # size=440, subsystem=Engine (VIESFParse)
    (0x011788a0, "VIESFParse::ParseFloraSpriteObj"),  # size=688, subsystem=Engine (VIESFParse)
    (0x01178b50, "VIESFParse::ParseEffectVolumeSpriteObj"),  # size=948, subsystem=Engine (VIESFParse)
    (0x01178f08, "VIESFParse::ParseParticleDefinitionObj"),  # size=480, subsystem=Engine (VIESFParse)
    (0x011790e8, "VIESFParse::ParseParticleDefinition"),  # size=1148, subsystem=Engine (VIESFParse)
    (0x01179568, "VIESFParse::ParseSpellEffectObj"),  # size=1140, subsystem=Engine (VIESFParse)
    (0x011799e0, "VIESFParse::ParseStaticLightingObj"),  # size=424, subsystem=Engine (VIESFParse)
    (0x01179b88, "VIESFParse::ParseSubSprite"),  # size=220, subsystem=Engine (VIESFParse)
    (0x01179c68, "VIESFParse::ParseSimpleSubSpriteObj"),  # size=696, subsystem=Engine (VIESFParse)
    (0x01179f20, "VIESFParse::ParseSkinSubSpriteObj"),  # size=656, subsystem=Engine (VIESFParse)
    (0x0117a1b0, "VIESFParse::Convert32"),  # size=376, subsystem=Engine (VIESFParse)
    (0x0117a328, "VIESFParse::Convert24"),  # size=424, subsystem=Engine (VIESFParse)
    (0x0117a4d0, "VIESFParse::Convert16"),  # size=400, subsystem=Engine (VIESFParse)
    (0x0117a660, "VIESFParse::Convert4"),  # size=416, subsystem=Engine (VIESFParse)
    (0x0117a800, "VIESFParse::AdpcmToPcm"),  # size=548, subsystem=Engine (VIESFParse)
    (0x0117aa28, "VIESFParse::constructor"),  # size=88, subsystem=Engine (VIESFParse)
    (0x0117aa80, "VIESFParse::~destructor"),  # size=44, subsystem=Engine (VIESFParse)
    (0x0117aab0, "VIESFParse::SetPermResource"),  # size=12, subsystem=Engine (VIESFParse)
    (0x0117aac0, "VIESFParse::SetProgressCallback"),  # size=12, subsystem=Engine (VIESFParse)
    (0x0117aad0, "VIESFParse::ParseParticleDefinition"),  # size=120, subsystem=Engine (VIESFParse)
    (0x0117ab48, "VIESFParse::ParseSurfaceArray"),  # size=148, subsystem=Engine (VIESFParse)
    (0x0117abe0, "VIESFParse::ParseSurfaceArrayObj"),  # size=124, subsystem=Engine (VIESFParse)
    (0x0117ac60, "VIESFParse::ParseSurface"),  # size=96, subsystem=Engine (VIESFParse)
    (0x0117acc0, "VIESFParse::ParseMaterialPal"),  # size=84, subsystem=Engine (VIESFParse)
    (0x0117ad18, "VIESFParse::ParseHSpriteSpriteArray"),  # size=172, subsystem=Engine (VIESFParse)
    (0x0117adc8, "VIESFParse::ParseHSpriteAnim"),  # size=96, subsystem=Engine (VIESFParse)
    (0x0117ae28, "VIESFParse::ParseCSpriteSpriteArray"),  # size=172, subsystem=Engine (VIESFParse)
    (0x0117aed8, "VIESFParse::ParseZoneResources"),  # size=148, subsystem=Engine (VIESFParse)
    (0x0117af70, "VIESFParse::ParseZoneBase"),  # size=84, subsystem=Engine (VIESFParse)
    (0x0117afc8, "VIESFParse::ParseZoneActors"),  # size=148, subsystem=Engine (VIESFParse)
    (0x0117b060, "VIESFParse::ParseZoneRoomActors"),  # size=84, subsystem=Engine (VIESFParse)
    (0x0117b0b8, "VIESFParse::ParseZoneStaticLightings"),  # size=148, subsystem=Engine (VIESFParse)
    (0x0117b150, "VIESFParse::ParseZoneRoomStaticLightings"),  # size=84, subsystem=Engine (VIESFParse)
    (0x0117b1a8, "VIESFParse::ParseStaticLighting"),  # size=112, subsystem=Engine (VIESFParse)
    (0x0117b218, "VIESFParse::ParseZoneFlora"),  # size=144, subsystem=Engine (VIESFParse)
    (0x0117b2a8, "VIESFParse::ParseWorld"),  # size=116, subsystem=Engine (VIESFParse)
    (0x0117b320, "VIESFParse::ParseWorldRegions"),  # size=184, subsystem=Engine (VIESFParse)
    (0x0117b3d8, "VIESFParse::ParseActor"),  # size=84, subsystem=Engine (VIESFParse)
    (0x0117b430, "VIESFParse::ParseResourceDir"),  # size=132, subsystem=Engine (VIESFParse)
    (0x0117b4b8, "VIESFParse::ParseSoundArray"),  # size=164, subsystem=Engine (VIESFParse)
    (0x0117b560, "VIESFParse::ParseSkinLODSpriteSpriteArray"),  # size=172, subsystem=Engine (VIESFParse)
    (0x0117b610, "VIESFParse::ParseGroupSpriteSpriteArray"),  # size=172, subsystem=Engine (VIESFParse)
    (0x0117b6c0, "VIESFParse::Convert8"),  # size=196, subsystem=Engine (VIESFParse)
    (0x0117b788, "VISound::~destructor"),  # size=52, subsystem=Engine (VISound)
    (0x0117b7c8, "VISound::AsWave"),  # size=16, subsystem=Engine (VISound)
    (0x0117b7d8, "VISound::AsXm"),  # size=20, subsystem=Engine (VISound)
    (0x0117bc58, "VISoundSprite::Raster"),  # size=692, subsystem=Engine (VISoundSprite)
    (0x0117bf10, "VISoundSprite::Pick"),  # size=708, subsystem=Engine (VISoundSprite)
    (0x0117c1d8, "VISoundSprite::constructor"),  # size=100, subsystem=Engine (VISoundSprite)
    (0x0117c240, "VISoundSprite::~destructor"),  # size=100, subsystem=Engine (VISoundSprite)
    (0x0117c2b0, "VISoundSprite::Collide"),  # size=8, subsystem=Engine (VISoundSprite)
    (0x0117c2b8, "VISoundSprite::Collide"),  # size=8, subsystem=Engine (VISoundSprite)
    (0x0117c2c0, "VISoundSprite::Copy"),  # size=264, subsystem=Engine (VISoundSprite)
    (0x0117c3c8, "VISoundSprite::Release"),  # size=176, subsystem=Engine (VISoundSprite)
    (0x0117c480, "VISoundSprite::SetAttenuationMode"),  # size=8, subsystem=Engine (VISoundSprite)
    (0x0117c490, "VISoundSprite::EnablePan"),  # size=8, subsystem=Engine (VISoundSprite)
    (0x0117c5b8, "StringConv::constructor"),  # size=332, subsystem=C++ Runtime
    (0x0117c708, "StringConv::~destructor"),  # size=172, subsystem=C++ Runtime
    (0x0117caa8, "VIFader::Update"),  # size=372, subsystem=Engine (VIFader)
    (0x0117cc20, "VIFader::constructor"),  # size=12, subsystem=Engine (VIFader)
    (0x0117cc30, "VIFader::~destructor"),  # size=84, subsystem=Engine (VIFader)
    (0x0117cc88, "VIFader::Init"),  # size=140, subsystem=Engine (VIFader)
    (0x0117cd18, "VIFader::Free"),  # size=76, subsystem=Engine (VIFader)
    (0x0117cd68, "VIFader::Begin"),  # size=60, subsystem=Engine (VIFader)
    (0x0117cda8, "VIFader::End"),  # size=16, subsystem=Engine (VIFader)
    (0x0117cdb8, "VISpellActiveEvent::constructor"),  # size=368, subsystem=Engine (VISpellActiveEvent)
    (0x0117cf28, "VISpellEventDriver::~destructor"),  # size=700, subsystem=Engine (VISpellEventDriver)
    (0x0117d1e8, "VISpellEventDriver::NewSetAction"),  # size=408, subsystem=Engine (VISpellEventDriver)
    (0x0117d380, "VISpellEventDriver::NewPlayAttack"),  # size=592, subsystem=Engine (VISpellEventDriver)
    (0x0117d5d0, "VISpellEventDriver::NewShakeCamera"),  # size=300, subsystem=Engine (VISpellEventDriver)
    (0x0117d700, "VISpellEventDriver::NewCreateEmitter"),  # size=208, subsystem=Engine (VISpellEventDriver)
    (0x0117d7d0, "VISpellEventDriver::NewSetEmitterMotif"),  # size=452, subsystem=Engine (VISpellEventDriver)
    (0x0117d998, "VISpellEventDriver::NewFadeSprite"),  # size=692, subsystem=Engine (VISpellEventDriver)
    (0x0117dc50, "VISpellEventDriver::NewPlayTargetProjectile"),  # size=2452, subsystem=Engine (VISpellEventDriver)
    (0x0117e5e8, "VISpellEventDriver::NewCreateSound"),  # size=340, subsystem=Engine (VISpellEventDriver)
    (0x0117e740, "VISpellEventDriver::NewDestroySound"),  # size=240, subsystem=Engine (VISpellEventDriver)
    (0x0117e830, "VISpellEventDriver::NewCreateSprite"),  # size=468, subsystem=Engine (VISpellEventDriver)
    (0x0117ea08, "VISpellEventDriver::NewDestroySprite"),  # size=240, subsystem=Engine (VISpellEventDriver)
    (0x0117eaf8, "VISpellEventDriver::NewPlayTargetLightning"),  # size=380, subsystem=Engine (VISpellEventDriver)
    (0x0117ec78, "VISpellEventDriver::ProcessCreateEmitter"),  # size=1716, subsystem=Engine (VISpellEventDriver)
    (0x0117f330, "VISpellEventDriver::ProcessCreateSound"),  # size=692, subsystem=Engine (VISpellEventDriver)
    (0x0117f5e8, "VISpellEventDriver::ProcessCreateSprite"),  # size=620, subsystem=Engine (VISpellEventDriver)
    (0x0117f858, "VISpellEventDriver::ProcessSetEmitterMotif"),  # size=368, subsystem=Engine (VISpellEventDriver)
    (0x0117f9c8, "VISpellEventDriver::ProcessFadeSprite"),  # size=732, subsystem=Engine (VISpellEventDriver)
    (0x0117fca8, "VISpellEventDriver::ProcessLightningEvent"),  # size=1992, subsystem=Engine (VISpellEventDriver)
    (0x01180470, "VISpellEventDriver::ProcessProjectileEvent"),  # size=5376, subsystem=Engine (VISpellEventDriver)
    (0x01181970, "VISpellEventDriver::ProcessWaitEvent"),  # size=852, subsystem=Engine (VISpellEventDriver)
    (0x01181cc8, "VISpellEventDriver::ProcessInactiveEvents"),  # size=296, subsystem=Engine (VISpellEventDriver)
    (0x01181df0, "VISpellEventDriver::Process"),  # size=1356, subsystem=Engine (VISpellEventDriver)
    (0x01182470, "VISpellActiveEvent::~destructor"),  # size=192, subsystem=Engine (VISpellActiveEvent)
    (0x01182590, "VISpellEventDriver::constructor"),  # size=164, subsystem=Engine (VISpellEventDriver)
    (0x01182638, "VISpellEventDriver::FindCreateEmitter"),  # size=80, subsystem=Engine (VISpellEventDriver)
    (0x01182688, "VISpellEventDriver::FindCreateSound"),  # size=80, subsystem=Engine (VISpellEventDriver)
    (0x011826d8, "VISpellEventDriver::FindCreateSprite"),  # size=80, subsystem=Engine (VISpellEventDriver)
    (0x01182728, "VISpellEventDriver::FindSetEmitterMotif"),  # size=160, subsystem=Engine (VISpellEventDriver)
    (0x011827c8, "VISpellEventDriver::NewWait"),  # size=108, subsystem=Engine (VISpellEventDriver)
    (0x01182838, "VISpellEventDriver::NewVibrateController"),  # size=168, subsystem=Engine (VISpellEventDriver)
    (0x011828e0, "VISpellEventDriver::NewSetEmitterAttractor"),  # size=108, subsystem=Engine (VISpellEventDriver)
    (0x01182950, "VISpellEventDriver::NewDestroyEmitter"),  # size=148, subsystem=Engine (VISpellEventDriver)
    (0x011829e8, "VISpellEventDriver::NewPlayTargetInstant"),  # size=176, subsystem=Engine (VISpellEventDriver)
    (0x01182a98, "VISpellEventDriver::GetNodeTransform"),  # size=164, subsystem=Engine (VISpellEventDriver)
    (0x01182b40, "VISpellEffectDriver::constructor"),  # size=116, subsystem=Engine (VISpellEffectDriver)
    (0x01182bb8, "VISpellEffectDriver::~destructor"),  # size=92, subsystem=Engine (VISpellEffectDriver)
    (0x01182c18, "VISpellEffectDriver::Create"),  # size=32, subsystem=Engine (VISpellEffectDriver)
    (0x01182c38, "VISpellEffectDriver::Destroy"),  # size=200, subsystem=Engine (VISpellEffectDriver)
    (0x01182d00, "VISpellEffectDriver::SetCaster"),  # size=12, subsystem=Engine (VISpellEffectDriver)
    (0x01182d10, "VISpellEffectDriver::SetTarget"),  # size=12, subsystem=Engine (VISpellEffectDriver)
    (0x01182d20, "VISpellEffectDriver::AddSecondaryTarget"),  # size=60, subsystem=Engine (VISpellEffectDriver)
    (0x01182d60, "VISpellEffectDriver::SetVibrateCallback"),  # size=12, subsystem=Engine (VISpellEffectDriver)
    (0x01182d70, "VISpellEffectDriver::SetCameraEffect"),  # size=8, subsystem=Engine (VISpellEffectDriver)
    (0x01182d78, "VISpellEffectDriver::SetPlayerActor"),  # size=8, subsystem=Engine (VISpellEffectDriver)
    (0x01182d80, "VISpellEffectDriver::NotifyActorWasDestroyed"),  # size=232, subsystem=Engine (VISpellEffectDriver)
    (0x01182e68, "VISpellEffectDriver::Trigger"),  # size=132, subsystem=Engine (VISpellEffectDriver)
    (0x01182ef0, "VISpellEffectDriver::AddSpellEventDriver"),  # size=216, subsystem=Engine (VISpellEffectDriver)
    (0x01182fc8, "VISpellEffectDriver::Process"),  # size=128, subsystem=Engine (VISpellEffectDriver)
    (0x01186518, "Encryptor::constructor"),  # size=368, subsystem=Networking
    (0x01186688, "Encryptor::~destructor"),  # size=372, subsystem=Networking
    (0x01186800, "Encryptor::setPublicKey"),  # size=196, subsystem=Networking
    (0x011868c8, "Encryptor::setPrivateKey"),  # size=196, subsystem=Networking
    (0x01186990, "Encryptor::generateSymmetricKey"),  # size=196, subsystem=Networking
    (0x01186a58, "Encryptor::setSymmetricKey"),  # size=196, subsystem=Networking
    (0x01187440, "Encryptor::test"),  # size=1212, subsystem=Networking
    (0x01187900, "Encryptor::generateAsymmetricKey"),  # size=92, subsystem=Networking
    (0x011f2950, "vector::_M_insert_aux"),  # size=484, subsystem=Networking
    (0x011f2c00, "Base::ByteStream::clear"),  # size=8, subsystem=Engine Utilities
    (0x011f2c20, "Base::ByteStream::growToAtLeast"),  # size=180, subsystem=Engine Utilities
    (0x011f2d58, "__default_alloc_template::_S_refill"),  # size=148, subsystem=C++ Stdlib
    (0x011f2df0, "__malloc_alloc_template::_S_oom_malloc"),  # size=148, subsystem=C++ Stdlib
    (0x011f2e88, "basic_string::replace"),  # size=676, subsystem=C++ Stdlib
    (0x011f3130, "vector::_M_insert_aux"),  # size=484, subsystem=Networking
    (0x011f3318, "__default_alloc_template::_S_chunk_alloc"),  # size=444, subsystem=C++ Stdlib
    (0x011f34d8, "VIPool::Erase"),  # size=228, subsystem=Engine (VIPool)
    (0x011f3600, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x011f3668, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x011f3770, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x011f3918, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x011f3938, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x011f39d8, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x011f3aa8, "VIFlatFile::__typeinfo"),  # size=64, subsystem=Engine (VIFlatFile)
    (0x011f3ae8, "VIFlatFileDirectory::__typeinfo"),  # size=116, subsystem=Engine (VIFlatFileDirectory)
    (0x011f3b60, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x011f3c00, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x011f3c88, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x011f3d30, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x011f3df8, "VIFloraSprite::__typeinfo"),  # size=80, subsystem=Engine (VIFloraSprite)
    (0x011f3e48, "VIMultiMap::Insert"),  # size=796, subsystem=Engine (VIMultiMap)
    (0x011f4168, "VIMultiMap::Erase"),  # size=512, subsystem=Engine (VIMultiMap)
    (0x011f4368, "VIMultiMap::AddNode"),  # size=252, subsystem=Engine (VIMultiMap)
    (0x011f4468, "VIMultiMap::LeftRotate"),  # size=204, subsystem=Engine (VIMultiMap)
    (0x011f4538, "VIMultiMap::RightRotate"),  # size=208, subsystem=Engine (VIMultiMap)
    (0x011f4608, "VIMultiMap::EraseFixup"),  # size=1020, subsystem=Engine (VIMultiMap)
    (0x011f4a08, "VIMultiMap::Allocate"),  # size=376, subsystem=Engine (VIMultiMap)
    (0x011f4b80, "VIMultiMap::DestroyPool"),  # size=132, subsystem=Engine (VIMultiMap)
    (0x011f4d70, "VISprite::__typeinfo"),  # size=80, subsystem=Engine (VISprite)
    (0x011f4dc0, "VISprite::GetType"),  # size=8, subsystem=Engine (VISprite)
    (0x011f4dc8, "VISprite::GetBBox"),  # size=8, subsystem=Engine (VISprite)
    (0x011f4dd0, "VISprite::GetBSphere"),  # size=8, subsystem=Engine (VISprite)
    (0x011f4dd8, "VISprite::GetOffDist"),  # size=8, subsystem=Engine (VISprite)
    (0x011f4f20, "VIMultiMap::FreeNode"),  # size=136, subsystem=Engine (VIMultiMap)
    (0x011f4fa8, "VIMultiMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMultiMap)
    (0x011f5060, "VIResource::__typeinfo"),  # size=64, subsystem=Engine (VIResource)
    (0x011f50a0, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x011f5100, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x011f5168, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x011f51e0, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x011f5290, "VIStreamAudioSprite::__typeinfo"),  # size=80, subsystem=Engine (VIStreamAudioSprite)
    (0x011f61b8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x011f6240, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x011f62a0, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x011f6308, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x011f6358, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x011f6430, "VIGroupSprite::__typeinfo"),  # size=80, subsystem=Engine (VIGroupSprite)
    (0x011f6480, "VIGroupSprite::GetNumMembers"),  # size=8, subsystem=Engine (VIGroupSprite)
    (0x011f6488, "VIGroupSprite::GetMemberSprite"),  # size=16, subsystem=Engine (VIGroupSprite)
    (0x011f6498, "vector::__as"),  # size=960, subsystem=Networking
    (0x011f6858, "_Rb_tree::_M_erase"),  # size=604, subsystem=C++ Stdlib
    (0x011f6ab8, "_Rb_tree::_M_erase"),  # size=508, subsystem=C++ Stdlib
    (0x011f6eb8, "_Rb_tree::insert_unique"),  # size=448, subsystem=C++ Stdlib
    (0x011f7288, "_Rb_tree::lower_bound"),  # size=124, subsystem=C++ Stdlib
    (0x011f73a8, "_Rb_tree::insert_unique"),  # size=552, subsystem=C++ Stdlib
    (0x011f75d0, "_Rb_tree::insert_unique"),  # size=372, subsystem=C++ Stdlib
    (0x011f7748, "_Rb_tree::erase"),  # size=408, subsystem=C++ Stdlib
    (0x011f78e0, "basic_string::replace"),  # size=304, subsystem=C++ Stdlib
    (0x011f7a10, "vector::_M_insert_aux"),  # size=832, subsystem=Networking
    (0x011f7d50, "vector::_M_insert_aux"),  # size=2288, subsystem=Networking
    (0x011f8640, "vector::__as"),  # size=1000, subsystem=Networking
    (0x011f8a28, "_Rb_tree::_M_insert"),  # size=2084, subsystem=C++ Stdlib
    (0x011f9250, "_Rb_tree::insert_unique"),  # size=372, subsystem=C++ Stdlib
    (0x011f93c8, "_Rb_tree::_M_insert"),  # size=2204, subsystem=C++ Stdlib
    (0x011f9c68, "_Rb_tree::insert_unique"),  # size=428, subsystem=C++ Stdlib
    (0x011f9e18, "_Rb_tree::_M_insert"),  # size=1080, subsystem=C++ Stdlib
    (0x011fa250, "_Rb_tree::erase"),  # size=1700, subsystem=C++ Stdlib
    (0x011fab38, "_Rb_tree::_M_erase"),  # size=108, subsystem=C++ Stdlib
    (0x011faba8, "_Rb_tree::lower_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011facf0, "_Rb_tree::lower_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011fad38, "_Rb_tree::upper_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011fae20, "VIGUIButton::__typeinfo"),  # size=80, subsystem=Engine (VIGUIButton)
    (0x011fae70, "_Rb_tree::_M_erase"),  # size=108, subsystem=C++ Stdlib
    (0x011faee0, "_Rb_tree::_M_erase"),  # size=108, subsystem=C++ Stdlib
    (0x011faf50, "_Rb_tree::_M_erase"),  # size=212, subsystem=C++ Stdlib
    (0x011fb028, "_Rb_tree::lower_bound"),  # size=124, subsystem=C++ Stdlib
    (0x011fb0a8, "_Rb_tree::insert_unique"),  # size=552, subsystem=C++ Stdlib
    (0x011fb3f0, "_Rb_tree::insert_unique"),  # size=448, subsystem=C++ Stdlib
    (0x011fb5b0, "_Rb_tree::_M_insert"),  # size=1208, subsystem=C++ Stdlib
    (0x011fba68, "_Rb_tree::insert_unique"),  # size=428, subsystem=C++ Stdlib
    (0x011fbc18, "_Rb_tree::_M_insert"),  # size=1104, subsystem=C++ Stdlib
    (0x011fc068, "_Rb_tree::insert_unique"),  # size=372, subsystem=C++ Stdlib
    (0x011fc1e0, "_Rb_tree::lower_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011fc228, "_Rb_tree::insert_unique"),  # size=372, subsystem=C++ Stdlib
    (0x011fc3a0, "_Rb_tree::erase"),  # size=408, subsystem=C++ Stdlib
    (0x011fc538, "_Rb_tree::_M_insert"),  # size=896, subsystem=C++ Stdlib
    (0x011fc8b8, "_Rb_tree::erase"),  # size=1700, subsystem=C++ Stdlib
    (0x011fcf60, "_Rb_tree::lower_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011fcfa8, "_Rb_tree::upper_bound"),  # size=72, subsystem=C++ Stdlib
    (0x011fd050, "VIGUIComboBox::__typeinfo"),  # size=80, subsystem=Engine (VIGUIComboBox)
    (0x011fd0a0, "VIGUIComboBox::GetSelectedIndex"),  # size=8, subsystem=Engine (VIGUIComboBox)
    (0x011fd138, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x011fd1e0, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x011fd1f0, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x011fd280, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x011fd440, "basic_string::replace"),  # size=956, subsystem=C++ Stdlib
    (0x011fd8d0, "vector::_M_insert_aux"),  # size=620, subsystem=Networking
    (0x011fdee8, "RealmService::MatchGameAttrsImp::setNodeList"),  # size=28, subsystem=DMA/GIF Pipeline
    (0x011fe048, "RealmService::GameAttrsImp::setNodeList"),  # size=28, subsystem=Networking
    (0x011fe158, "RealmService::GameStatsImp::setNodeList"),  # size=28, subsystem=Networking
    (0x011fe3f0, "vector::__as"),  # size=712, subsystem=Networking
    (0x011fe6b8, "vector::__as"),  # size=712, subsystem=Networking
    (0x011fe980, "vector::__as"),  # size=792, subsystem=Networking
    (0x011fec98, "vector::_M_insert_aux"),  # size=620, subsystem=Networking
    (0x011fef08, "vector::_M_insert_aux"),  # size=696, subsystem=Networking
    (0x011ff298, "VIGUIDataModel::__typeinfo"),  # size=64, subsystem=Engine (VIGUIDataModel)
    (0x011ff2d8, "VIGUIDataModel::~destructor"),  # size=52, subsystem=Engine (VIGUIDataModel)
    (0x011ff448, "VIGUIDialog::__typeinfo"),  # size=80, subsystem=Engine (VIGUIDialog)
    (0x011ff4f8, "VIGUIObject::__typeinfo"),  # size=64, subsystem=Engine (VIGUIObject)
    (0x011ff538, "VIGUIObject::OnKeyUp"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x011ff540, "VIGUIObject::OnKeyDown"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x011ff548, "VIGUIObject::HandleEvent"),  # size=8, subsystem=Engine (VIGUIObject)
    (0x011ff550, "basic_string::alloc"),  # size=488, subsystem=C++ Stdlib
    (0x011ff738, "basic_string::alloc"),  # size=536, subsystem=C++ Stdlib
    (0x011ff950, "basic_string::replace"),  # size=308, subsystem=C++ Stdlib
    (0x011ffa88, "basic_string::replace"),  # size=976, subsystem=C++ Stdlib
    (0x012005f8, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x012006a8, "VIGUISelectionGrid::__typeinfo"),  # size=64, subsystem=Engine (VIGUISelectionGrid)
    (0x012006e8, "VIGUIPage::__typeinfo"),  # size=64, subsystem=Engine (VIGUIPage)
    (0x012007b8, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x01200860, "VIList::Insert"),  # size=192, subsystem=Engine (VIList)
    (0x01200920, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01200930, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x01200998, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x01200a40, "VIGUIStringDataModel::__typeinfo"),  # size=80, subsystem=Engine (VIGUIStringDataModel)
    (0x01200af0, "VIGUIText::~destructor"),  # size=116, subsystem=Engine (VIGUIText)
    (0x01200b68, "VIGUIText::__typeinfo"),  # size=80, subsystem=Engine (VIGUIText)
    (0x01200bb8, "VIGUIText::SetEllipses"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01200bc0, "VIGUIText::SetPasswordMode"),  # size=8, subsystem=Engine (VIGUIText)
    (0x01200c30, "VIGUIToggleButton::~destructor"),  # size=100, subsystem=Engine (VIGUIToggleButton)
    (0x01200c98, "VIGUIToggleButton::__typeinfo"),  # size=80, subsystem=Engine (VIGUIToggleButton)
    (0x01200d00, "VIGUIToggleDataModel::~destructor"),  # size=52, subsystem=Engine (VIGUIToggleDataModel)
    (0x01200d38, "VIGUIToggleDataModel::__typeinfo"),  # size=80, subsystem=Engine (VIGUIToggleDataModel)
    (0x012018f8, "VIActorFilter::__typeinfo"),  # size=64, subsystem=Engine (VIActorFilter)
    (0x01201938, "VIPool::Add"),  # size=268, subsystem=Engine (VIPool)
    (0x01201a48, "VIPool::Add"),  # size=348, subsystem=Engine (VIPool)
    (0x01201ba8, "VIPool::Erase"),  # size=252, subsystem=Engine (VIPool)
    (0x01201ca8, "VIPool::Erase"),  # size=252, subsystem=Engine (VIPool)
    (0x01201da8, "VIVector::Init"),  # size=504, subsystem=Engine (VIVector)
    (0x01201fd8, "VIVector::Init"),  # size=168, subsystem=Engine (VIVector)
    (0x012020b8, "VIArray::Init"),  # size=168, subsystem=Engine (VIArray)
    (0x01202190, "VIPool::Init"),  # size=316, subsystem=Engine (VIPool)
    (0x01202328, "VIPool::Init"),  # size=372, subsystem=Engine (VIPool)
    (0x01202510, "VIPool::Init"),  # size=428, subsystem=Engine (VIPool)
    (0x01202710, "VIVector::Add"),  # size=540, subsystem=Engine (VIVector)
    (0x01202930, "VIVector::Add"),  # size=180, subsystem=Engine (VIVector)
    (0x012029e8, "VIVector::DestroyPool"),  # size=172, subsystem=Engine (VIVector)
    (0x01202a98, "VIPool::DestroyPool"),  # size=96, subsystem=Engine (VIPool)
    (0x01202af8, "VIPool::DestroyPool"),  # size=112, subsystem=Engine (VIPool)
    (0x01202b68, "VIPool::Allocate"),  # size=264, subsystem=Engine (VIPool)
    (0x01202c70, "VIPool::Allocate"),  # size=316, subsystem=Engine (VIPool)
    (0x01202db0, "VIPool::Allocate"),  # size=368, subsystem=Engine (VIPool)
    (0x01202f78, "VIVector::Allocate"),  # size=560, subsystem=Engine (VIVector)
    (0x012031a8, "VIVector::Allocate"),  # size=224, subsystem=Engine (VIVector)
    (0x01203348, "VIHSprite::__typeinfo"),  # size=80, subsystem=Sprites
    (0x01203398, "VIHSprite::GetDefaultAnim"),  # size=8, subsystem=Sprites
    (0x01203430, "VIVector::constructor"),  # size=16, subsystem=Engine (VIVector)
    (0x01203440, "VIVector::constructor"),  # size=16, subsystem=Engine (VIVector)
    (0x01203450, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01203460, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01203480, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012034a0, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012034c0, "VIVector::Clear"),  # size=104, subsystem=Engine (VIVector)
    (0x01203528, "VIVector::Clear"),  # size=104, subsystem=Engine (VIVector)
    (0x01203590, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x012035f8, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01203660, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x012036c8, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01203880, "VIVector::DestroyPool"),  # size=152, subsystem=Engine (VIVector)
    (0x01203918, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01203968, "VIPool::DestroyPool"),  # size=112, subsystem=Engine (VIPool)
    (0x01203a00, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x01203a90, "VIPool::LinkFreeChain"),  # size=152, subsystem=Engine (VIPool)
    (0x01203b28, "VIPool::LinkFreeChain"),  # size=176, subsystem=Engine (VIPool)
    (0x01203bd8, "VIPool::LinkFreeChain"),  # size=176, subsystem=Engine (VIPool)
    (0x01203c88, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01203d90, "VIPool::Erase"),  # size=196, subsystem=Engine (VIPool)
    (0x01204198, "WeatherFilter::__typeinfo"),  # size=80, subsystem=C++ Runtime
    (0x012041e8, "_Rb_tree::_M_erase"),  # size=108, subsystem=C++ Stdlib
    (0x01204258, "_Deque_base::_M_initialize_map"),  # size=516, subsystem=C++ Stdlib
    (0x01204460, "vector::_M_insert_aux"),  # size=608, subsystem=Networking
    (0x012046c0, "deque::_M_pop_front_aux"),  # size=104, subsystem=C++ Stdlib
    (0x01204728, "deque::_M_push_back_aux"),  # size=228, subsystem=C++ Stdlib
    (0x01204810, "_Rb_tree::insert_unique"),  # size=372, subsystem=C++ Stdlib
    (0x01204988, "_Deque_base::_M_create_nodes"),  # size=124, subsystem=C++ Stdlib
    (0x01204a08, "deque::_M_reallocate_map"),  # size=740, subsystem=C++ Stdlib
    (0x01204cf0, "_Rb_tree::_M_insert"),  # size=1104, subsystem=C++ Stdlib
    (0x012051b8, "GenericAPI::GenericAPICore::suspendProcessing"),  # size=12, subsystem=Networking
    (0x012051c8, "GenericAPI::GenericAPICore::resumeProcessing"),  # size=8, subsystem=Networking
    (0x01205288, "_Deque_base::_M_destroy_nodes"),  # size=96, subsystem=C++ Stdlib
    (0x012052e8, "_Rb_tree::find"),  # size=116, subsystem=C++ Stdlib
    (0x012053d8, "GenericAPI::GenericConnection::isConnected"),  # size=8, subsystem=Networking
    (0x012053e0, "TcpConnectionHandler::__typeinfo"),  # size=64, subsystem=Networking
    (0x01205650, "VIPool::Add"),  # size=328, subsystem=Engine (VIPool)
    (0x01205798, "VIMap::Insert"),  # size=772, subsystem=Engine (VIMap)
    (0x01205aa0, "VIMap::Erase"),  # size=512, subsystem=Engine (VIMap)
    (0x01205ca0, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01205d70, "VIPool::Allocate"),  # size=288, subsystem=Engine (VIPool)
    (0x01205e90, "VIMap::AddNode"),  # size=252, subsystem=Engine (VIMap)
    (0x01205f90, "VIMap::LeftRotate"),  # size=204, subsystem=Engine (VIMap)
    (0x01206060, "VIMap::RightRotate"),  # size=208, subsystem=Engine (VIMap)
    (0x01206130, "VIMap::EraseFixup"),  # size=1020, subsystem=Engine (VIMap)
    (0x01206530, "VIMap::Allocate"),  # size=340, subsystem=Engine (VIMap)
    (0x01206688, "VIMap::DestroyPool"),  # size=320, subsystem=Engine (VIMap)
    (0x01206850, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x012068b8, "VIMap::Clear"),  # size=116, subsystem=Engine (VIMap)
    (0x012069e8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x012069f8, "VIPool::DestroyPool"),  # size=116, subsystem=Engine (VIPool)
    (0x01206b50, "VIMap::FreeNode"),  # size=68, subsystem=Engine (VIMap)
    (0x01206be0, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01206c80, "VIMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMap)
    (0x01206d30, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01206dc8, "VIMap::constructor"),  # size=28, subsystem=Engine (VIMap)
    (0x01206e60, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x01206ef0, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01206fa0, "VILODSprite::__typeinfo"),  # size=80, subsystem=Engine (VILODSprite)
    (0x01206ff0, "VILODSprite::GetNumLevels"),  # size=8, subsystem=Engine (VILODSprite)
    (0x01206ff8, "VILODSprite::GetLevelSprite"),  # size=16, subsystem=Engine (VILODSprite)
    (0x01207020, "VIWalkCameraFilter::__typeinfo"),  # size=80, subsystem=Engine (VIWalkCameraFilter)
    (0x01207070, "VIWalkCameraFilter::FilterActor"),  # size=84, subsystem=Engine (VIWalkCameraFilter)
    (0x012070e0, "VIWalkFloorFilter::__typeinfo"),  # size=80, subsystem=Engine (VIWalkFloorFilter)
    (0x01207130, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01207190, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x012071f8, "VIArray::Allocate"),  # size=136, subsystem=Engine (VIArray)
    (0x01207280, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x012072d0, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01207368, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01207470, "VIPool::Erase"),  # size=228, subsystem=Engine (VIPool)
    (0x01207558, "VIPool::Allocate"),  # size=256, subsystem=Engine (VIPool)
    (0x012076d0, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01207738, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x012077d8, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01207830, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01207890, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x012078f0, "VIArray::Allocate"),  # size=128, subsystem=Engine (VIArray)
    (0x01207970, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x012079d8, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01207a40, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x01207ab8, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01207b08, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01207b98, "VIWindowManager::__typeinfo"),  # size=80, subsystem=Engine (VIWindowManager)
    (0x01207c28, "VIWndMcErr::__typeinfo"),  # size=80, subsystem=Engine (VIWndMcErr)
    (0x01207cb8, "VIWndCombo::__typeinfo"),  # size=80, subsystem=Engine (VIWndCombo)
    (0x01207d68, "VINameSprite::__typeinfo"),  # size=80, subsystem=Engine (VINameSprite)
    (0x01207df8, "VIWndConnect::__typeinfo"),  # size=80, subsystem=Engine (VIWndConnect)
    (0x01207e48, "VIWndConnect::SetNetConfig"),  # size=16, subsystem=Engine (VIWndConnect)
    (0x01207e68, "VIWndConnect::SetRestartRequired"),  # size=8, subsystem=Engine (VIWndConnect)
    (0x01207eb0, "VIWndDnas::__typeinfo"),  # size=80, subsystem=Engine (VIWndDnas)
    (0x01207f00, "VIWndDnas::Status"),  # size=44, subsystem=Engine (VIWndDnas)
    (0x01207f30, "VIWndDnas::SetStatus"),  # size=76, subsystem=Engine (VIWndDnas)
    (0x01207fe0, "VIParticleSprite::__typeinfo"),  # size=80, subsystem=Engine (VIParticleSprite)
    (0x01208030, "VIParticleSprite::ParticleDefinition"),  # size=8, subsystem=Engine (VIParticleSprite)
    (0x01208038, "VIParticleSprite::ParticleEmitter"),  # size=8, subsystem=Engine (VIParticleSprite)
    (0x01208080, "VIWndEdit::__typeinfo"),  # size=80, subsystem=UI
    (0x012080d8, "VIWndEdit::SetLeftTop"),  # size=24, subsystem=UI
    (0x012080f0, "VIWndEdit::GetText"),  # size=8, subsystem=UI
    (0x012080f8, "VIWndEdit::SetParam1"),  # size=8, subsystem=UI
    (0x01208100, "VIWndEdit::SetParam2"),  # size=8, subsystem=UI
    (0x01208108, "VIWndEdit::SetMode"),  # size=8, subsystem=UI
    (0x01208110, "VIWndEdit::ClearParams"),  # size=12, subsystem=UI
    (0x01208170, "VIWndEdit::ResetBlink"),  # size=40, subsystem=UI
    (0x012081f8, "VICSprite::__typeinfo"),  # size=80, subsystem=Engine (VICSprite)
    (0x01208248, "VICSprite::GetSkeletonType"),  # size=8, subsystem=Engine (VICSprite)
    (0x01208250, "VICSprite::GetRace"),  # size=8, subsystem=Engine (VICSprite)
    (0x01208258, "VICSprite::GetSex"),  # size=8, subsystem=Engine (VICSprite)
    (0x01208260, "VICSprite::GetItemAttackType"),  # size=24, subsystem=Engine (VICSprite)
    (0x01208278, "VICSprite::ItemHasProjectile"),  # size=32, subsystem=Engine (VICSprite)
    (0x01208298, "VICSprite::GetItemProjectile"),  # size=24, subsystem=Engine (VICSprite)
    (0x012082b0, "VICSprite::IsDead"),  # size=8, subsystem=Engine (VICSprite)
    (0x012082b8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x012082c8, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01208328, "VIArray::Allocate"),  # size=212, subsystem=Engine (VIArray)
    (0x01208478, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x012084e0, "VIArray::DestroyPool"),  # size=164, subsystem=Engine (VIArray)
    (0x01208588, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01208690, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01208760, "VIPool::Allocate"),  # size=256, subsystem=Engine (VIPool)
    (0x01208860, "VIPool::DestroyPool"),  # size=104, subsystem=Engine (VIPool)
    (0x01208940, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x012089e0, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01208ab8, "VIWndEula::__typeinfo"),  # size=80, subsystem=Engine (VIWndEula)
    (0x01208b08, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01208c10, "VIPool::Erase"),  # size=228, subsystem=Engine (VIPool)
    (0x01208cf8, "VIPool::Allocate"),  # size=256, subsystem=Engine (VIPool)
    (0x01208e08, "VIPool::DestroyPool"),  # size=92, subsystem=Engine (VIPool)
    (0x01208e68, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01208f08, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01208fd0, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01209080, "basic_string::resize"),  # size=88, subsystem=C++ Stdlib
    (0x012090d8, "basic_string::resize"),  # size=88, subsystem=C++ Stdlib
    (0x01209130, "basic_string::replace"),  # size=888, subsystem=C++ Stdlib
    (0x012094e8, "VIWndGenericRenderer::__typeinfo"),  # size=80, subsystem=Engine (VIWndGenericRenderer)
    (0x01209538, "VIWndGenericRenderer::GetWndEdit"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209540, "VIWndGenericRenderer::GetDialog"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209548, "VIWndGenericRenderer::GetStationName"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209550, "VIWndGenericRenderer::GetPassword"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209558, "VIWndGenericRenderer::GetReturnCode"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209560, "VIWndGenericRenderer::SetReturnCode"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209568, "VIWndGenericRenderer::GetCurrentPage"),  # size=8, subsystem=Engine (VIWndGenericRenderer)
    (0x01209570, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01209628, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x012096b8, "VIList::Insert"),  # size=192, subsystem=Engine (VIList)
    (0x01209778, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x012097e0, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x01209870, "VIMap::Insert"),  # size=780, subsystem=Engine (VIMap)
    (0x01209b80, "VIMap::Erase"),  # size=512, subsystem=Engine (VIMap)
    (0x01209d80, "VIMap::AddNode"),  # size=252, subsystem=Engine (VIMap)
    (0x01209e80, "VIMap::LeftRotate"),  # size=204, subsystem=Engine (VIMap)
    (0x01209f50, "VIMap::RightRotate"),  # size=208, subsystem=Engine (VIMap)
    (0x0120a020, "VIMap::EraseFixup"),  # size=1020, subsystem=Engine (VIMap)
    (0x0120a420, "VIMap::constructor"),  # size=28, subsystem=Engine (VIMap)
    (0x0120a4b8, "VIMap::Init"),  # size=92, subsystem=Engine (VIMap)
    (0x0120a530, "VIMap::Clear"),  # size=116, subsystem=Engine (VIMap)
    (0x0120a710, "VIMap::FreeNode"),  # size=68, subsystem=Engine (VIMap)
    (0x0120a758, "VIMap::Allocate"),  # size=396, subsystem=Engine (VIMap)
    (0x0120a8e8, "VIMap::DestroyPool"),  # size=88, subsystem=Engine (VIMap)
    (0x0120a988, "VIMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMap)
    (0x0120aa78, "VIWndLegal::__typeinfo"),  # size=80, subsystem=Engine (VIWndLegal)
    (0x0120ab08, "VIWndMessage::__typeinfo"),  # size=80, subsystem=Engine (VIWndMessage)
    (0x0120aba0, "VIWnd::__typeinfo"),  # size=64, subsystem=UI
    (0x0120abe0, "VIWnd::GetParent"),  # size=8, subsystem=UI
    (0x0120abe8, "VIWnd::SetVisible"),  # size=8, subsystem=UI
    (0x0120abf0, "VIWnd::GetVisible"),  # size=8, subsystem=UI
    (0x0120abf8, "VIWnd::UI"),  # size=12, subsystem=UI
    (0x0120ad38, "VISet::Insert"),  # size=748, subsystem=Engine (VISet)
    (0x0120b028, "VISet::Erase"),  # size=512, subsystem=Engine (VISet)
    (0x0120b228, "VISet::AddNode"),  # size=252, subsystem=Engine (VISet)
    (0x0120b328, "VISet::LeftRotate"),  # size=204, subsystem=Engine (VISet)
    (0x0120b3f8, "VISet::RightRotate"),  # size=208, subsystem=Engine (VISet)
    (0x0120b4c8, "VISet::EraseFixup"),  # size=1020, subsystem=Engine (VISet)
    (0x0120b8c8, "VISet::Allocate"),  # size=332, subsystem=Engine (VISet)
    (0x0120ba18, "VISet::constructor"),  # size=28, subsystem=Engine (VISet)
    (0x0120bb30, "VISet::FreeNode"),  # size=68, subsystem=Engine (VISet)
    (0x0120bb78, "VISet::LinkFreeChain"),  # size=176, subsystem=Engine (VISet)
    (0x0120bc28, "VISet::DestroyPool"),  # size=88, subsystem=Engine (VISet)
    (0x0120bce0, "VIPointLight::__typeinfo"),  # size=80, subsystem=Engine (VIPointLight)
    (0x0120bd30, "VIPointLight::SetColor"),  # size=40, subsystem=Engine (VIPointLight)
    (0x0120bdc8, "VIWndOptions::__typeinfo"),  # size=80, subsystem=Engine (VIWndOptions)
    (0x0120be18, "vector::__as"),  # size=712, subsystem=Networking
    (0x0120c0e0, "vector::__as"),  # size=620, subsystem=Networking
    (0x0120c350, "vector::insert"),  # size=860, subsystem=Networking
    (0x0120c7d8, "VIPointSprite::__typeinfo"),  # size=80, subsystem=Engine (VIPointSprite)
    (0x0120c828, "VIPointSprite::GetPointType"),  # size=8, subsystem=Engine (VIPointSprite)
    (0x0120c870, "VIWndPatcher::__typeinfo"),  # size=80, subsystem=Engine (VIWndPatcher)
    (0x0120c8c0, "VIWndPatcher::State"),  # size=8, subsystem=Engine (VIWndPatcher)
    (0x0120c8c8, "VIWndPatcher::SetState"),  # size=8, subsystem=Engine (VIWndPatcher)
    (0x0120c8d8, "VIWndPatcher::SetRestartRequired"),  # size=8, subsystem=Engine (VIWndPatcher)
    (0x0120c8e0, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120c9a8, "VIWndReadMessage::__typeinfo"),  # size=80, subsystem=Engine (VIWndReadMessage)
    (0x0120f110, "VIRadialFloraFilter::__typeinfo"),  # size=80, subsystem=Engine (VIRadialFloraFilter)
    (0x0120f1d8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120f1e8, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x0120f248, "VIArray::DestroyPool"),  # size=160, subsystem=Engine (VIArray)
    (0x0120f2e8, "VIArray::Allocate"),  # size=200, subsystem=Engine (VIArray)
    (0x0120f3b0, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120f418, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120f480, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120f4e8, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120f550, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x0120f5a0, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x0120f5f0, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x0120f680, "VIWndSplash::__typeinfo"),  # size=80, subsystem=Engine (VIWndSplash)
    (0x0120f6d8, "VIWndSplash::NotifyDetached"),  # size=16, subsystem=Engine (VIWndSplash)
    (0x0120f6e8, "VIWndSplash::NotifyIspLost"),  # size=16, subsystem=Engine (VIWndSplash)
    (0x0120f6f8, "VIWndSplash::Done"),  # size=8, subsystem=Engine (VIWndSplash)
    (0x0120f830, "VIWndStationLogin::__typeinfo"),  # size=80, subsystem=Engine (VIWndStationLogin)
    (0x0120f880, "VIWndStationLogin::SetLogin"),  # size=28, subsystem=Engine (VIWndStationLogin)
    (0x0120f8a0, "VIWndStationLogin::GetLogin"),  # size=36, subsystem=Engine (VIWndStationLogin)
    (0x0120f8c8, "VIWndStationLogin::SetPassword"),  # size=28, subsystem=Engine (VIWndStationLogin)
    (0x0120f8e8, "VIWndStationLogin::GetPassword"),  # size=36, subsystem=Engine (VIWndStationLogin)
    (0x0120f910, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120f920, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120f930, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x0120f990, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x0120f9f0, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120fb68, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120fbd0, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x0120fc38, "VIArray::Allocate"),  # size=164, subsystem=Engine (VIArray)
    (0x0120fce0, "VIArray::Allocate"),  # size=128, subsystem=Engine (VIArray)
    (0x0120fd60, "VIArray::DestroyPool"),  # size=168, subsystem=Engine (VIArray)
    (0x0120fe08, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x0120fe58, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120fee0, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x0120ff68, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x0120ffc8, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01210028, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01210090, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x012100f8, "VIArray::Allocate"),  # size=136, subsystem=Engine (VIArray)
    (0x01210180, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x012101d0, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01210220, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x012104f0, "VIRealmInterface::__typeinfo"),  # size=80, subsystem=Engine (VIRealmInterface)
    (0x01210540, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01210578, "VIList::Insert"),  # size=192, subsystem=Engine (VIList)
    (0x01210640, "VIList::Erase"),  # size=156, subsystem=Engine (VIList)
    (0x012106f0, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x01210780, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01210850, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01210920, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x012109f0, "VIList::Erase"),  # size=236, subsystem=Engine (VIList)
    (0x01210ae0, "VIPool::MoveToLast"),  # size=240, subsystem=Engine (VIPool)
    (0x01210bd0, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01210cd8, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01210da8, "VIPool::Allocate"),  # size=256, subsystem=Engine (VIPool)
    (0x01210ea8, "VIPool::DestroyPool"),  # size=104, subsystem=Engine (VIPool)
    (0x01210f10, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01210fa8, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01211010, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012110a8, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01211140, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x012111a8, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01211210, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012112a8, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01211340, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012113d8, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x01211438, "VIList::Init"),  # size=44, subsystem=Engine (VIList)
    (0x01211468, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x012114c8, "VIList::Init"),  # size=44, subsystem=Engine (VIList)
    (0x012114f8, "VIList::Init"),  # size=44, subsystem=Engine (VIList)
    (0x01211528, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x012115f8, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x012116d0, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01211788, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x01211860, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01211918, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x01211980, "VIList::Clear"),  # size=188, subsystem=Engine (VIList)
    (0x01211ab0, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01211b88, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01211bf0, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x01211c80, "VIList::Add"),  # size=144, subsystem=Engine (VIList)
    (0x01211d10, "VIList::Add"),  # size=140, subsystem=Engine (VIList)
    (0x01211e08, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x01211e90, "VIList::Erase"),  # size=136, subsystem=Engine (VIList)
    (0x01211f28, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01211fc8, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x012120d0, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x012121d8, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x012122e0, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x012123e8, "VIPool::Erase"),  # size=228, subsystem=Engine (VIPool)
    (0x012124d0, "VIPool::Add"),  # size=312, subsystem=Engine (VIPool)
    (0x01212608, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01212738, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01212868, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01212998, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01212ac8, "VIPool::Allocate"),  # size=328, subsystem=Engine (VIPool)
    (0x01212c10, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x01212c70, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01212cd8, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01212d30, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01212d88, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01212de0, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01212e38, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01212ed0, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01212f70, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01213010, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x012130b0, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01213150, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x012131f0, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01213288, "VIMap::constructor"),  # size=28, subsystem=Engine (VIMap)
    (0x01213320, "VIMultiMap::constructor"),  # size=28, subsystem=Engine (VIMultiMap)
    (0x012133b8, "VIPool::DestroyPool"),  # size=104, subsystem=Engine (VIPool)
    (0x01213410, "VIMap::DestroyPool"),  # size=88, subsystem=Engine (VIMap)
    (0x01213468, "VIMultiMap::DestroyPool"),  # size=320, subsystem=Engine (VIMultiMap)
    (0x012137d8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01213860, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x012138e8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01213970, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x012139f8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01213a80, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01213ae0, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01213b48, "VIArray::Clear"),  # size=136, subsystem=Engine (VIArray)
    (0x01213bb0, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01213c18, "VIVector::Add"),  # size=168, subsystem=Engine (VIVector)
    (0x01213cc0, "VIVector::Allocate"),  # size=284, subsystem=Engine (VIVector)
    (0x01213db0, "VIArray::DestroyPool"),  # size=160, subsystem=Engine (VIArray)
    (0x01213e50, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01213ea0, "VIArray::Allocate"),  # size=156, subsystem=Engine (VIArray)
    (0x01213f40, "VIVector::DestroyPool"),  # size=76, subsystem=Engine (VIVector)
    (0x01214018, "vector::_M_insert_aux"),  # size=612, subsystem=Networking
    (0x01214280, "vector::_M_insert_aux"),  # size=620, subsystem=Networking
    (0x012144f0, "vector::_M_insert_aux"),  # size=620, subsystem=Networking
    (0x012149e8, "RealmService::RealmGatewayAPI::onCreateAccount"),  # size=8, subsystem=Networking
    (0x012149f0, "RealmService::RealmGatewayAPI::onConsumeKey"),  # size=8, subsystem=Networking
    (0x012149f8, "RealmService::RealmGatewayAPI::onLogin"),  # size=8, subsystem=Networking
    (0x01214a00, "RealmService::RealmGatewayAPI::onLogout"),  # size=8, subsystem=Networking
    (0x01214a08, "RealmService::RealmGatewayAPI::onTouchSession"),  # size=8, subsystem=Networking
    (0x01214a10, "RealmService::RealmGatewayAPI::onCreateAvatar"),  # size=8, subsystem=Networking
    (0x01214a18, "RealmService::RealmGatewayAPI::onDestroyAvatar"),  # size=8, subsystem=Networking
    (0x01214a20, "RealmService::RealmGatewayAPI::onGetPublicRooms"),  # size=8, subsystem=Networking
    (0x01214a28, "RealmService::RealmGatewayAPI::onGetRoom"),  # size=8, subsystem=Networking
    (0x01214a30, "RealmService::RealmGatewayAPI::onCreatePrivateRoom"),  # size=8, subsystem=Networking
    (0x01214a38, "RealmService::RealmGatewayAPI::onEnterRoom"),  # size=8, subsystem=Networking
    (0x01214a40, "RealmService::RealmGatewayAPI::onLeaveRoom"),  # size=8, subsystem=Networking
    (0x01214a48, "RealmService::RealmGatewayAPI::onSendRoomMessage"),  # size=8, subsystem=Networking
    (0x01214a50, "RealmService::RealmGatewayAPI::onSendInstantMessage"),  # size=8, subsystem=Networking
    (0x01214a58, "RealmService::RealmGatewayAPI::onAddFriend"),  # size=8, subsystem=Networking
    (0x01214a60, "RealmService::RealmGatewayAPI::onRemoveFriend"),  # size=8, subsystem=Networking
    (0x01214a68, "RealmService::RealmGatewayAPI::onAddIgnore"),  # size=8, subsystem=Networking
    (0x01214a70, "RealmService::RealmGatewayAPI::onRemoveIgnore"),  # size=8, subsystem=Networking
    (0x01214a78, "RealmService::RealmGatewayAPI::onAddRoomModerator"),  # size=8, subsystem=Networking
    (0x01214a80, "RealmService::RealmGatewayAPI::onRemoveRoomModerator"),  # size=8, subsystem=Networking
    (0x01214a88, "RealmService::RealmGatewayAPI::onAddBan"),  # size=8, subsystem=Networking
    (0x01214a90, "RealmService::RealmGatewayAPI::onRemoveBan"),  # size=8, subsystem=Networking
    (0x01214a98, "RealmService::RealmGatewayAPI::onAddInvite"),  # size=8, subsystem=Networking
    (0x01214aa0, "RealmService::RealmGatewayAPI::onRemoveInvite"),  # size=8, subsystem=Networking
    (0x01214aa8, "RealmService::RealmGatewayAPI::onKickAvatar"),  # size=8, subsystem=Networking
    (0x01214ab0, "RealmService::RealmGatewayAPI::onModifyRoomBanner"),  # size=8, subsystem=Networking
    (0x01214ab8, "RealmService::RealmGatewayAPI::onGetUserInfo"),  # size=8, subsystem=Networking
    (0x01214ac0, "RealmService::RealmGatewayAPI::onGetUserStats"),  # size=8, subsystem=Networking
    (0x01214ac8, "RealmService::RealmGatewayAPI::onGetRealmTime"),  # size=8, subsystem=Networking
    (0x01214ad0, "RealmService::RealmGatewayAPI::onGetRealmStats"),  # size=8, subsystem=Networking
    (0x01214ad8, "RealmService::RealmGatewayAPI::onCreatePrivateGame"),  # size=8, subsystem=Networking
    (0x01214ae0, "RealmService::RealmGatewayAPI::onCreatePublicGame"),  # size=8, subsystem=Networking
    (0x01214ae8, "RealmService::RealmGatewayAPI::onMatchGame"),  # size=8, subsystem=Networking
    (0x01214af0, "RealmService::RealmGatewayAPI::onCancelGame"),  # size=8, subsystem=Networking
    (0x01214af8, "RealmService::RealmGatewayAPI::onGetGame"),  # size=8, subsystem=Networking
    (0x01214b00, "RealmService::RealmGatewayAPI::onStartGame"),  # size=8, subsystem=Networking
    (0x01214b08, "RealmService::RealmGatewayAPI::onRecordGameOutcome"),  # size=8, subsystem=Networking
    (0x01214b10, "RealmService::RealmGatewayAPI::onDoClientDiscovery"),  # size=8, subsystem=Networking
    (0x01214b18, "RealmService::RealmGatewayAPI::onChangePassword"),  # size=8, subsystem=Networking
    (0x01214b20, "RealmService::RealmGatewayAPI::onChangeEmail"),  # size=8, subsystem=Networking
    (0x01214b28, "RealmService::RealmGatewayAPI::onGetRules"),  # size=8, subsystem=Networking
    (0x01214b30, "RealmService::RealmGatewayAPI::onRoundTrip"),  # size=8, subsystem=Networking
    (0x01214b38, "RealmService::RealmGatewayAPI::notifyInstantMessage"),  # size=8, subsystem=Networking
    (0x01214b40, "RealmService::RealmGatewayAPI::notifyRoomMessage"),  # size=8, subsystem=Networking
    (0x01214b48, "RealmService::RealmGatewayAPI::notifyFriendStatus"),  # size=8, subsystem=Networking
    (0x01214b50, "RealmService::RealmGatewayAPI::notifyEnterRoom"),  # size=8, subsystem=Networking
    (0x01214b58, "RealmService::RealmGatewayAPI::notifyLeaveRoom"),  # size=8, subsystem=Networking
    (0x01214b60, "RealmService::RealmGatewayAPI::notifyKickRoom"),  # size=8, subsystem=Networking
    (0x01214b68, "RealmService::RealmGatewayAPI::notifyKickAvatar"),  # size=8, subsystem=Networking
    (0x01214b70, "RealmService::RealmGatewayAPI::notifyModeratorAddedRoom"),  # size=8, subsystem=Networking
    (0x01214b78, "RealmService::RealmGatewayAPI::notifyModeratorAddedAvatar"),  # size=8, subsystem=Networking
    (0x01214b80, "RealmService::RealmGatewayAPI::notifyModeratorRemovedRoom"),  # size=8, subsystem=Networking
    (0x01214b88, "RealmService::RealmGatewayAPI::notifyModeratorRemovedAvatar"),  # size=8, subsystem=Networking
    (0x01214b90, "RealmService::RealmGatewayAPI::notifyAddBanRoom"),  # size=8, subsystem=Networking
    (0x01214b98, "RealmService::RealmGatewayAPI::notifyAddBanAvatar"),  # size=8, subsystem=Networking
    (0x01214ba0, "RealmService::RealmGatewayAPI::notifyRemoveBanRoom"),  # size=8, subsystem=Networking
    (0x01214ba8, "RealmService::RealmGatewayAPI::notifyRemoveBanAvatar"),  # size=8, subsystem=Networking
    (0x01214bb0, "RealmService::RealmGatewayAPI::notifyAddInviteRoom"),  # size=8, subsystem=Networking
    (0x01214bb8, "RealmService::RealmGatewayAPI::notifyAddInviteAvatar"),  # size=8, subsystem=Networking
    (0x01214bc0, "RealmService::RealmGatewayAPI::notifyRemoveInviteRoom"),  # size=8, subsystem=Networking
    (0x01214bc8, "RealmService::RealmGatewayAPI::notifyRemoveInviteAvatar"),  # size=8, subsystem=Networking
    (0x01214bd0, "RealmService::RealmGatewayAPI::notifyRoomBanner"),  # size=8, subsystem=Networking
    (0x01214bd8, "RealmService::RealmGatewayAPI::notifyGameDiscovered"),  # size=8, subsystem=Networking
    (0x01214be0, "RealmService::RealmGatewayAPI::notifyClientRequestsConnect"),  # size=8, subsystem=Networking
    (0x01214be8, "RealmService::RealmGatewayAPI::notifyClientDiscovered"),  # size=8, subsystem=Networking
    (0x01214bf0, "RealmService::RealmGatewayAPI::notifyForcedLogout"),  # size=8, subsystem=Networking
    (0x01214d18, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01214da0, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01214e28, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01214e88, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01214ee8, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01214f50, "VIArray::Clear"),  # size=100, subsystem=Engine (VIArray)
    (0x01214fb8, "VIArray::Allocate"),  # size=136, subsystem=Engine (VIArray)
    (0x01215040, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x01215090, "VIArray::DestroyPool"),  # size=76, subsystem=Engine (VIArray)
    (0x012150e0, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x01215158, "vector::__as"),  # size=688, subsystem=Networking
    (0x01215408, "vector::__as"),  # size=712, subsystem=Networking
    (0x012156d0, "vector::__as"),  # size=712, subsystem=Networking
    (0x0121ae38, "vector::_M_insert_aux"),  # size=484, subsystem=Networking
    (0x0121b020, "vector::_M_insert_aux"),  # size=1208, subsystem=Networking
    (0x0121b4d8, "vector::_M_insert_aux"),  # size=484, subsystem=Networking
    (0x0121b6c0, "vector::_M_insert_aux"),  # size=1124, subsystem=Networking
    (0x0121bb28, "vector::_M_insert_aux"),  # size=484, subsystem=Networking
    (0x0121bd10, "vector::_M_insert_aux"),  # size=604, subsystem=Networking
    (0x0121cc58, "RealmService::ResConsumeKey::getSessionID"),  # size=8, subsystem=Networking
    (0x0121cd80, "RealmService::ResCreateAccount::getSessionID"),  # size=8, subsystem=Networking
    (0x0121d0c8, "RealmService::ResCreateAvatar::getFriendList"),  # size=8, subsystem=Networking
    (0x0121d0d0, "RealmService::ResCreateAvatar::getFriendListPtrs"),  # size=8, subsystem=Networking
    (0x0121d0d8, "RealmService::ResCreateAvatar::getOnlineFriendList"),  # size=8, subsystem=Networking
    (0x0121d0e0, "RealmService::ResCreateAvatar::getOnlineFriendListPtrs"),  # size=8, subsystem=Networking
    (0x0121d610, "RealmService::ResCreatePrivateRoom::getRoomName"),  # size=8, subsystem=Networking
    (0x0121d618, "RealmService::ResCreatePrivateRoom::getRoomBanner"),  # size=8, subsystem=Networking
    (0x0121d620, "RealmService::ResCreatePrivateRoom::getMemberList"),  # size=8, subsystem=Networking
    (0x0121d628, "RealmService::ResCreatePrivateRoom::getMemberListPtrs"),  # size=8, subsystem=Networking
    (0x0121d630, "RealmService::ResCreatePrivateRoom::getModeratorList"),  # size=8, subsystem=Networking
    (0x0121d638, "RealmService::ResCreatePrivateRoom::getModeratorListPtrs"),  # size=8, subsystem=Networking
    (0x0121dd18, "RealmService::ResEnterRoom::getRoomName"),  # size=8, subsystem=Networking
    (0x0121dd20, "RealmService::ResEnterRoom::getRoomBanner"),  # size=8, subsystem=Networking
    (0x0121dd28, "RealmService::ResEnterRoom::getMemberList"),  # size=8, subsystem=Networking
    (0x0121dd30, "RealmService::ResEnterRoom::getMemberListPtrs"),  # size=8, subsystem=Networking
    (0x0121dd38, "RealmService::ResEnterRoom::getModeratorList"),  # size=8, subsystem=Networking
    (0x0121dd40, "RealmService::ResEnterRoom::getModeratorListPtrs"),  # size=8, subsystem=Networking
    (0x0121dec8, "RealmService::ResGetGame::getGameLocation"),  # size=8, subsystem=Networking
    (0x0121ded0, "RealmService::ResGetGame::getGameOwnerName"),  # size=8, subsystem=Networking
    (0x0121ded8, "RealmService::ResGetGame::getMatchGameID"),  # size=8, subsystem=Networking
    (0x0121e350, "RealmService::ResGetPublicRooms::getRoomNames"),  # size=8, subsystem=Networking
    (0x0121e358, "RealmService::ResGetPublicRooms::getRoomNamesPtrs"),  # size=8, subsystem=Networking
    (0x0121e360, "RealmService::ResGetPublicRooms::getRoomBanners"),  # size=8, subsystem=Networking
    (0x0121e368, "RealmService::ResGetPublicRooms::getRoomBannersPtrs"),  # size=8, subsystem=Networking
    (0x0121e370, "RealmService::ResGetPublicRooms::getRoomCurSizes"),  # size=8, subsystem=Networking
    (0x0121e378, "RealmService::ResGetPublicRooms::getRoomMaxSizes"),  # size=8, subsystem=Networking
    (0x0121e408, "RealmService::ResGetRealmStats::getUsersLoggedInGame"),  # size=8, subsystem=Networking
    (0x0121e410, "RealmService::ResGetRealmStats::getUsersLoggedInRealm"),  # size=8, subsystem=Networking
    (0x0121e418, "RealmService::ResGetRealmStats::getGamesRunningGame"),  # size=8, subsystem=Networking
    (0x0121e420, "RealmService::ResGetRealmStats::getGamesRunningRealm"),  # size=8, subsystem=Networking
    (0x0121e428, "RealmService::ResGetRealmStats::getUsersPlayingGame"),  # size=8, subsystem=Networking
    (0x0121e430, "RealmService::ResGetRealmStats::getUsersPlayingRealm"),  # size=8, subsystem=Networking
    (0x0121e438, "RealmService::ResGetRealmStats::getUnmatchedGamesGame"),  # size=8, subsystem=Networking
    (0x0121e440, "RealmService::ResGetRealmStats::getUnmatchedGamesRealm"),  # size=8, subsystem=Networking
    (0x0121e4d0, "RealmService::ResGetRealmTime::getCurRealmTime"),  # size=8, subsystem=Networking
    (0x0121e8d8, "RealmService::ResGetRoom::getRoomName"),  # size=8, subsystem=Networking
    (0x0121e8e0, "RealmService::ResGetRoom::getRoomBanner"),  # size=8, subsystem=Networking
    (0x0121e8e8, "RealmService::ResGetRoom::getMemberList"),  # size=8, subsystem=Networking
    (0x0121e8f0, "RealmService::ResGetRoom::getMemberListPtrs"),  # size=8, subsystem=Networking
    (0x0121e8f8, "RealmService::ResGetRoom::getModeratorList"),  # size=8, subsystem=Networking
    (0x0121e900, "RealmService::ResGetRoom::getModeratorListPtrs"),  # size=8, subsystem=Networking
    (0x0121ea28, "RealmService::ResGetUserInfo::getStationID"),  # size=8, subsystem=Networking
    (0x0121ea30, "RealmService::ResGetUserInfo::getRealmID"),  # size=8, subsystem=Networking
    (0x0121ea38, "RealmService::ResGetUserInfo::getOnline"),  # size=8, subsystem=Networking
    (0x0121ea40, "RealmService::ResGetUserInfo::getInGame"),  # size=8, subsystem=Networking
    (0x0121ea48, "RealmService::ResGetUserInfo::getChatRoom"),  # size=8, subsystem=Networking
    (0x0121eba0, "RealmService::ResGetUserStats::getOverallStats"),  # size=8, subsystem=Networking
    (0x0121eba8, "RealmService::ResGetUserStats::getStatsByGameType"),  # size=8, subsystem=Networking
    (0x0121ede0, "RealmService::ResLogin::getSessionID"),  # size=8, subsystem=Networking
    (0x0121f3d0, "RealmService::ResMatchGame::getGameLocations"),  # size=8, subsystem=Networking
    (0x0121f3d8, "RealmService::ResMatchGame::getGameLocationsPtrs"),  # size=8, subsystem=Networking
    (0x0121f3e0, "RealmService::ResMatchGame::getGameNames"),  # size=8, subsystem=Networking
    (0x0121f3e8, "RealmService::ResMatchGame::getGameNamesPtrs"),  # size=8, subsystem=Networking
    (0x0121f3f0, "RealmService::ResMatchGame::getGameOwnerNames"),  # size=8, subsystem=Networking
    (0x0121f3f8, "RealmService::ResMatchGame::getGameOwnerNamesPtrs"),  # size=8, subsystem=Networking
    (0x0121f400, "RealmService::ResMatchGame::getMatchGameIDs"),  # size=8, subsystem=Networking
    (0x0121f408, "RealmService::ResMatchGame::getGameBlobs"),  # size=8, subsystem=Networking
    (0x0121f9e8, "RealmService::ResStartGame::getGameID"),  # size=8, subsystem=Networking
    (0x0121fc20, "RealmService::ResGetRules::getRules"),  # size=8, subsystem=Networking
    (0x01220498, "VIPool::Add"),  # size=312, subsystem=Engine (VIPool)
    (0x012205d0, "VIMap::Insert"),  # size=1160, subsystem=Engine (VIMap)
    (0x01220a58, "VIMap::Erase"),  # size=600, subsystem=Engine (VIMap)
    (0x01220cb0, "VIMultiMap::Insert"),  # size=756, subsystem=Engine (VIMultiMap)
    (0x01220fa8, "VIMultiMap::Erase"),  # size=512, subsystem=Engine (VIMultiMap)
    (0x012211a8, "VIPool::Insert"),  # size=364, subsystem=Engine (VIPool)
    (0x01221318, "VIPool::Erase"),  # size=228, subsystem=Engine (VIPool)
    (0x01221400, "VIPool::Allocate"),  # size=280, subsystem=Engine (VIPool)
    (0x01221518, "VIMap::AddNode"),  # size=276, subsystem=Engine (VIMap)
    (0x01221630, "VIMap::LeftRotate"),  # size=236, subsystem=Engine (VIMap)
    (0x01221720, "VIMap::RightRotate"),  # size=240, subsystem=Engine (VIMap)
    (0x01221810, "VIMap::EraseFixup"),  # size=1268, subsystem=Engine (VIMap)
    (0x01221d08, "VIMultiMap::AddNode"),  # size=252, subsystem=Engine (VIMultiMap)
    (0x01221e08, "VIMultiMap::LeftRotate"),  # size=204, subsystem=Engine (VIMultiMap)
    (0x01221ed8, "VIMultiMap::RightRotate"),  # size=208, subsystem=Engine (VIMultiMap)
    (0x01221fa8, "VIMultiMap::EraseFixup"),  # size=1020, subsystem=Engine (VIMultiMap)
    (0x012223a8, "VIMap::Allocate"),  # size=488, subsystem=Engine (VIMap)
    (0x01222590, "VIMultiMap::Allocate"),  # size=332, subsystem=Engine (VIMultiMap)
    (0x012226e0, "VIMultiMap::Clear"),  # size=116, subsystem=Engine (VIMultiMap)
    (0x01222758, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x012227c0, "VIMap::Clear"),  # size=116, subsystem=Engine (VIMap)
    (0x01222988, "VIMap::FreeNode"),  # size=76, subsystem=Engine (VIMap)
    (0x012229d8, "VIMultiMap::FreeNode"),  # size=68, subsystem=Engine (VIMultiMap)
    (0x01222a20, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01222ac0, "VIMap::LinkFreeChain"),  # size=192, subsystem=Engine (VIMap)
    (0x01222b80, "VIMultiMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMultiMap)
    (0x01222c70, "VIWave::__typeinfo"),  # size=80, subsystem=Audio
    (0x01222cc0, "VISound::__typeinfo"),  # size=80, subsystem=Engine (VISound)
    (0x01222d28, "VISceneFilter::__typeinfo"),  # size=64, subsystem=Engine (VISceneFilter)
    (0x01222d68, "VISceneFilter::GetActor"),  # size=8, subsystem=Engine (VISceneFilter)
    (0x01222d70, "VISceneFilter::GetSprite"),  # size=8, subsystem=Engine (VISceneFilter)
    (0x01222d78, "VISceneFilter::GetAttachment"),  # size=8, subsystem=Engine (VISceneFilter)
    (0x01222dc0, "VIXm::__typeinfo"),  # size=80, subsystem=Engine (VIXm)
    (0x01222e10, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01222f18, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01222fe8, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x012230b8, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01223188, "VIPool::Erase"),  # size=204, subsystem=Engine (VIPool)
    (0x01223258, "VIMultiMap::Insert"),  # size=756, subsystem=Engine (VIMultiMap)
    (0x01223650, "VIMultiMap::Erase"),  # size=512, subsystem=Engine (VIMultiMap)
    (0x01223850, "VIPool::Allocate"),  # size=256, subsystem=Engine (VIPool)
    (0x01223950, "VIMultiMap::AddNode"),  # size=252, subsystem=Engine (VIMultiMap)
    (0x01223a50, "VIMultiMap::LeftRotate"),  # size=204, subsystem=Engine (VIMultiMap)
    (0x01223b20, "VIMultiMap::RightRotate"),  # size=208, subsystem=Engine (VIMultiMap)
    (0x01223bf0, "VIMultiMap::EraseFixup"),  # size=1020, subsystem=Engine (VIMultiMap)
    (0x01223ff0, "VIMultiMap::Allocate"),  # size=332, subsystem=Engine (VIMultiMap)
    (0x01224140, "VIMultiMap::DestroyPool"),  # size=88, subsystem=Engine (VIMultiMap)
    (0x01224298, "VIPool::DestroyPool"),  # size=104, subsystem=Engine (VIPool)
    (0x01224300, "VISceneOutdoorsFilter::__typeinfo"),  # size=80, subsystem=Engine (VISceneOutdoorsFilter)
    (0x01224350, "VISceneOutdoorsFilter::FilterActor"),  # size=20, subsystem=Engine (VISceneOutdoorsFilter)
    (0x01224368, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x012243d0, "VIList::constructor"),  # size=16, subsystem=Engine (VIList)
    (0x01224438, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x012244d0, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01224568, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01224600, "VIPool::constructor"),  # size=32, subsystem=Engine (VIPool)
    (0x01224698, "VIVector::constructor"),  # size=16, subsystem=Engine (VIVector)
    (0x01224720, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x012247a8, "VIArray::constructor"),  # size=12, subsystem=Engine (VIArray)
    (0x01224830, "VIList::Init"),  # size=44, subsystem=Engine (VIList)
    (0x01224860, "VIList::Init"),  # size=44, subsystem=Engine (VIList)
    (0x01224890, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x012248f0, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x01224950, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x012249b0, "VIPool::Init"),  # size=92, subsystem=Engine (VIPool)
    (0x01224a10, "VIList::Clear"),  # size=132, subsystem=Engine (VIList)
    (0x01224a98, "VIList::Clear"),  # size=100, subsystem=Engine (VIList)
    (0x01224b70, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01224c48, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01224d98, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01224e70, "VIPool::Clear"),  # size=104, subsystem=Engine (VIPool)
    (0x01224ed8, "VIVector::Clear"),  # size=104, subsystem=Engine (VIVector)
    (0x01224f40, "VIVector::Init"),  # size=140, subsystem=Engine (VIVector)
    (0x01224fd0, "VIMultiMap::constructor"),  # size=28, subsystem=Engine (VIMultiMap)
    (0x01225090, "VIList::Add"),  # size=140, subsystem=Engine (VIList)
    (0x01225120, "VIList::Erase"),  # size=188, subsystem=Engine (VIList)
    (0x01225200, "VIList::Add"),  # size=112, subsystem=Engine (VIList)
    (0x01225270, "VIList::Erase"),  # size=156, subsystem=Engine (VIList)
    (0x01225438, "VIMultiMap::FreeNode"),  # size=68, subsystem=Engine (VIMultiMap)
    (0x01225480, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01225520, "VIMultiMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMultiMap)
    (0x01225618, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01225720, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01225828, "VIPool::Add"),  # size=264, subsystem=Engine (VIPool)
    (0x01225930, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01225a60, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01225b90, "VIPool::Allocate"),  # size=304, subsystem=Engine (VIPool)
    (0x01225cc0, "VIMap::constructor"),  # size=28, subsystem=Engine (VIMap)
    (0x01225d30, "VIVector::Add"),  # size=144, subsystem=Engine (VIVector)
    (0x01225dc0, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01225e18, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01225e70, "VIPool::DestroyPool"),  # size=88, subsystem=Engine (VIPool)
    (0x01225ec8, "VIMap::DestroyPool"),  # size=88, subsystem=Engine (VIMap)
    (0x01225f30, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01225fd0, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01226070, "VIPool::LinkFreeChain"),  # size=160, subsystem=Engine (VIPool)
    (0x01226110, "VIVector::Allocate"),  # size=220, subsystem=Engine (VIVector)
    (0x01226318, "VIVector::DestroyPool"),  # size=76, subsystem=Engine (VIVector)
    (0x01226380, "VISceneQuery::__typeinfo"),  # size=64, subsystem=Engine (VISceneQuery)
    (0x012263c0, "VISceneQuery::NumObjects"),  # size=8, subsystem=Engine (VISceneQuery)
    (0x012263c8, "VISceneQuery::Object"),  # size=20, subsystem=Engine (VISceneQuery)
    (0x012263e0, "VIVector::Init"),  # size=92, subsystem=Engine (VIVector)
    (0x01226440, "VIMultiMap::Init"),  # size=92, subsystem=Engine (VIMultiMap)
    (0x012264a0, "VIVector::Clear"),  # size=104, subsystem=Engine (VIVector)
    (0x01226508, "VIMultiMap::Clear"),  # size=116, subsystem=Engine (VIMultiMap)
    (0x012265e0, "VIEffectVolumeSprite::__typeinfo"),  # size=80, subsystem=Engine (VIEffectVolumeSprite)
    (0x01226630, "VIEffectVolumeSprite::EffectVolume"),  # size=8, subsystem=Engine (VIEffectVolumeSprite)
    (0x01226638, "VIMultiMap::Init"),  # size=92, subsystem=Engine (VIMultiMap)
    (0x01226698, "VIMultiMap::Clear"),  # size=116, subsystem=Engine (VIMultiMap)
    (0x01226770, "VISimpleSprite::__typeinfo"),  # size=80, subsystem=Engine (VISimpleSprite)
    (0x012267f0, "VIEnvRay::__typeinfo"),  # size=64, subsystem=Engine (VIEnvRay)
    (0x01226838, "VITransEnvRay::__typeinfo"),  # size=116, subsystem=Engine (VITransEnvRay)
    (0x01226910, "VISkinSprite::__typeinfo"),  # size=80, subsystem=Engine (VISkinSprite)
    (0x01226960, "VIMap::Insert"),  # size=772, subsystem=Engine (VIMap)
    (0x01226c68, "VIMap::AddNode"),  # size=252, subsystem=Engine (VIMap)
    (0x01226d68, "VIMap::LeftRotate"),  # size=204, subsystem=Engine (VIMap)
    (0x01226e38, "VIMap::RightRotate"),  # size=208, subsystem=Engine (VIMap)
    (0x01226f08, "VIMap::Allocate"),  # size=340, subsystem=Engine (VIMap)
    (0x01227060, "VIMap::Init"),  # size=92, subsystem=Engine (VIMap)
    (0x012270c0, "VIVector::Init"),  # size=92, subsystem=Engine (VIVector)
    (0x01227120, "VIVector::Init"),  # size=92, subsystem=Engine (VIVector)
    (0x01227180, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x012271e0, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01227240, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x012272a0, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01227300, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x01227360, "VIArray::Init"),  # size=92, subsystem=Engine (VIArray)
    (0x012273c0, "VIMap::LinkFreeChain"),  # size=176, subsystem=Engine (VIMap)
    (0x01227470, "VIArray::Allocate"),  # size=136, subsystem=Engine (VIArray)
    (0x012274f8, "VIMap::Clear"),  # size=116, subsystem=Engine (VIMap)
    (0x01227570, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x012275e8, "VIArray::Allocate"),  # size=128, subsystem=Engine (VIArray)
    (0x01227668, "VIArray::Allocate"),  # size=128, subsystem=Engine (VIArray)
    (0x012276e8, "VIArray::Allocate"),  # size=120, subsystem=Engine (VIArray)
    (0x01227800, "VISoundSprite::__typeinfo"),  # size=80, subsystem=Engine (VISoundSprite)
    (0x01227870, "Encryptor::__typeinfo"),  # size=64, subsystem=Networking
    (0x01351290, "filebuf::init"),  # size=28, subsystem=C++ Stdlib
    (0x013512b0, "filebuf::constructor"),  # size=100, subsystem=C++ Stdlib
    (0x01351318, "filebuf::constructor"),  # size=120, subsystem=C++ Stdlib
    (0x01351390, "filebuf::constructor"),  # size=160, subsystem=C++ Stdlib
    (0x01351430, "filebuf::~destructor"),  # size=156, subsystem=C++ Stdlib
    (0x013514d0, "filebuf::open"),  # size=352, subsystem=C++ Stdlib
    (0x01351630, "filebuf::open"),  # size=20, subsystem=C++ Stdlib
    (0x01351648, "filebuf::attach"),  # size=20, subsystem=C++ Stdlib
    (0x01351660, "filebuf::setbuf"),  # size=20, subsystem=C++ Stdlib
    (0x01351678, "filebuf::doallocate"),  # size=20, subsystem=C++ Stdlib
    (0x01351690, "filebuf::overflow"),  # size=20, subsystem=C++ Stdlib
    (0x013516a8, "filebuf::underflow"),  # size=20, subsystem=C++ Stdlib
    (0x013516c0, "filebuf::sync"),  # size=20, subsystem=C++ Stdlib
    (0x013516d8, "filebuf::seekoff"),  # size=20, subsystem=C++ Stdlib
    (0x013516f0, "filebuf::close"),  # size=44, subsystem=C++ Stdlib
    (0x01351720, "filebuf::sys_read"),  # size=20, subsystem=C++ Stdlib
    (0x01351738, "filebuf::sys_seek"),  # size=20, subsystem=C++ Stdlib
    (0x01351750, "filebuf::sys_write"),  # size=20, subsystem=C++ Stdlib
    (0x01351768, "filebuf::sys_stat"),  # size=20, subsystem=C++ Stdlib
    (0x01351780, "filebuf::sys_close"),  # size=20, subsystem=C++ Stdlib
    (0x01351798, "filebuf::xsputn"),  # size=44, subsystem=C++ Stdlib
    (0x013517c8, "filebuf::xsgetn"),  # size=20, subsystem=C++ Stdlib
    (0x01351a38, "_IO_istream_withassign::__as"),  # size=100, subsystem=C++ Runtime
    (0x01351aa0, "_IO_ostream_withassign::__as"),  # size=96, subsystem=C++ Runtime
    (0x01351b00, "istream::constructor"),  # size=232, subsystem=C++ Stdlib
    (0x01351c40, "istream::get"),  # size=204, subsystem=C++ Stdlib
    (0x01351d10, "istream::peek"),  # size=184, subsystem=C++ Stdlib
    (0x01351dc8, "istream::ignore"),  # size=268, subsystem=C++ Stdlib
    (0x01351ed8, "istream::read"),  # size=216, subsystem=C++ Stdlib
    (0x01351fb0, "istream::sync"),  # size=100, subsystem=C++ Stdlib
    (0x01352018, "istream::seekg"),  # size=80, subsystem=C++ Stdlib
    (0x01352068, "istream::seekg"),  # size=80, subsystem=C++ Stdlib
    (0x013520b8, "istream::tellg"),  # size=84, subsystem=C++ Stdlib
    (0x01352110, "istream::__rs"),  # size=192, subsystem=C++ Stdlib
    (0x013521d0, "istream::__rs"),  # size=348, subsystem=C++ Stdlib
    (0x013525e0, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x01352640, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x013526a0, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x01352700, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x01352760, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x013527c0, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x01352820, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x01352880, "istream::__rs"),  # size=92, subsystem=C++ Stdlib
    (0x013528e0, "istream::__rs"),  # size=96, subsystem=C++ Stdlib
    (0x01352940, "istream::__rs"),  # size=168, subsystem=C++ Stdlib
    (0x013529e8, "istream::__rs"),  # size=160, subsystem=C++ Stdlib
    (0x01352a88, "istream::__rs"),  # size=160, subsystem=C++ Stdlib
    (0x01352b28, "istream::__rs"),  # size=252, subsystem=C++ Stdlib
    (0x01352c28, "ostream::__ls"),  # size=168, subsystem=C++ Stdlib
    (0x01353080, "ostream::__ls"),  # size=152, subsystem=C++ Stdlib
    (0x01353118, "ostream::__ls"),  # size=112, subsystem=C++ Stdlib
    (0x01353188, "ostream::__ls"),  # size=140, subsystem=C++ Stdlib
    (0x01353218, "ostream::__ls"),  # size=108, subsystem=C++ Stdlib
    (0x01353288, "ostream::__ls"),  # size=140, subsystem=C++ Stdlib
    (0x01353318, "ostream::__ls"),  # size=108, subsystem=C++ Stdlib
    (0x01353388, "ostream::__ls"),  # size=272, subsystem=C++ Stdlib
    (0x01353498, "ostream::__ls"),  # size=372, subsystem=C++ Stdlib
    (0x01353610, "ostream::__ls"),  # size=228, subsystem=C++ Stdlib
    (0x013536f8, "ostream::constructor"),  # size=228, subsystem=C++ Stdlib
    (0x013537e0, "ostream::seekp"),  # size=80, subsystem=C++ Stdlib
    (0x01353830, "ostream::seekp"),  # size=80, subsystem=C++ Stdlib
    (0x01353880, "ostream::tellp"),  # size=84, subsystem=C++ Stdlib
    (0x013538d8, "ostream::flush"),  # size=92, subsystem=C++ Stdlib
    (0x01353a08, "istream::_skip_ws"),  # size=104, subsystem=C++ Stdlib
    (0x01353b60, "ostream::write"),  # size=200, subsystem=C++ Stdlib
    (0x01353c28, "ostream::do_osfx"),  # size=108, subsystem=C++ Stdlib
    (0x01353c98, "iostream::constructor"),  # size=396, subsystem=C++ Runtime
    (0x01353e28, "ios::close"),  # size=108, subsystem=C++ Stdlib
    (0x01353e98, "istream::skip"),  # size=64, subsystem=C++ Stdlib
    (0x01354040, "ostream::~destructor"),  # size=160, subsystem=C++ Stdlib
    (0x013540e0, "ostream::__typeinfo"),  # size=84, subsystem=C++ Stdlib
    (0x01354138, "ostream::constructor"),  # size=164, subsystem=C++ Stdlib
    (0x013541e0, "ostream::opfx"),  # size=60, subsystem=C++ Stdlib
    (0x01354220, "ostream::osfx"),  # size=48, subsystem=C++ Stdlib
    (0x01354250, "ostream::put"),  # size=56, subsystem=C++ Stdlib
    (0x01354288, "ostream::put"),  # size=56, subsystem=C++ Stdlib
    (0x013542c0, "ostream::put"),  # size=56, subsystem=C++ Stdlib
    (0x013542f8, "ostream::write"),  # size=20, subsystem=C++ Stdlib
    (0x01354310, "ostream::write"),  # size=20, subsystem=C++ Stdlib
    (0x01354328, "ostream::write"),  # size=20, subsystem=C++ Stdlib
    (0x01354340, "ostream::__ls"),  # size=28, subsystem=C++ Stdlib
    (0x01354360, "ostream::__ls"),  # size=28, subsystem=C++ Stdlib
    (0x01354380, "ostream::__ls"),  # size=20, subsystem=C++ Stdlib
    (0x01354398, "ostream::__ls"),  # size=20, subsystem=C++ Stdlib
    (0x013543b0, "ostream::__ls"),  # size=28, subsystem=C++ Stdlib
    (0x013543d0, "ostream::__ls"),  # size=24, subsystem=C++ Stdlib
    (0x013543e8, "ostream::__ls"),  # size=20, subsystem=C++ Stdlib
    (0x01354400, "ostream::__ls"),  # size=44, subsystem=C++ Stdlib
    (0x01354430, "ostream::__ls"),  # size=20, subsystem=C++ Stdlib
    (0x01354448, "ostream::__ls"),  # size=28, subsystem=C++ Stdlib
    (0x01354468, "ostream::__ls"),  # size=44, subsystem=C++ Stdlib
    (0x013544a8, "istream::~destructor"),  # size=160, subsystem=C++ Stdlib
    (0x01354548, "istream::__typeinfo"),  # size=84, subsystem=C++ Stdlib
    (0x013545a0, "istream::constructor"),  # size=168, subsystem=C++ Stdlib
    (0x01354648, "istream::get"),  # size=28, subsystem=C++ Stdlib
    (0x01354668, "istream::get"),  # size=20, subsystem=C++ Stdlib
    (0x01354680, "istream::getline"),  # size=28, subsystem=C++ Stdlib
    (0x013546a0, "istream::get"),  # size=20, subsystem=C++ Stdlib
    (0x013546b8, "istream::get"),  # size=28, subsystem=C++ Stdlib
    (0x013546d8, "istream::getline"),  # size=28, subsystem=C++ Stdlib
    (0x013546f8, "istream::read"),  # size=20, subsystem=C++ Stdlib
    (0x01354710, "istream::read"),  # size=20, subsystem=C++ Stdlib
    (0x01354728, "istream::read"),  # size=20, subsystem=C++ Stdlib
    (0x01354740, "istream::ipfx"),  # size=192, subsystem=C++ Stdlib
    (0x01354800, "istream::ipfx0"),  # size=132, subsystem=C++ Stdlib
    (0x01354888, "istream::ipfx1"),  # size=96, subsystem=C++ Stdlib
    (0x013548e8, "istream::isfx"),  # size=8, subsystem=C++ Stdlib
    (0x013548f0, "istream::get"),  # size=156, subsystem=C++ Stdlib
    (0x01354990, "istream::gcount"),  # size=8, subsystem=C++ Stdlib
    (0x01354998, "istream::putback"),  # size=88, subsystem=C++ Stdlib
    (0x013549f0, "istream::unget"),  # size=84, subsystem=C++ Stdlib
    (0x01354a48, "istream::unget"),  # size=88, subsystem=C++ Stdlib
    (0x01354ab0, "istream::__rs"),  # size=20, subsystem=C++ Stdlib
    (0x01354ac8, "istream::__rs"),  # size=20, subsystem=C++ Stdlib
    (0x01354ae0, "istream::__rs"),  # size=20, subsystem=C++ Stdlib
    (0x01354af8, "istream::__rs"),  # size=20, subsystem=C++ Stdlib
    (0x01354b10, "istream::__rs"),  # size=44, subsystem=C++ Stdlib
    (0x01354b40, "istream::__rs"),  # size=28, subsystem=C++ Stdlib
    (0x01354b60, "iostream::~destructor"),  # size=296, subsystem=C++ Runtime
    (0x01354c88, "iostream::__typeinfo"),  # size=92, subsystem=C++ Runtime
    (0x01354ce8, "iostream::constructor"),  # size=312, subsystem=C++ Runtime
    (0x01354e20, "_IO_istream_withassign::~destructor"),  # size=220, subsystem=C++ Runtime
    (0x01354f00, "_IO_istream_withassign::__typeinfo"),  # size=84, subsystem=C++ Runtime
    (0x01354f58, "_IO_istream_withassign::__as"),  # size=20, subsystem=C++ Runtime
    (0x01354f70, "_IO_ostream_withassign::~destructor"),  # size=220, subsystem=C++ Runtime
    (0x01355050, "_IO_ostream_withassign::__typeinfo"),  # size=84, subsystem=C++ Runtime
    (0x013550a8, "_IO_ostream_withassign::__as"),  # size=20, subsystem=C++ Runtime
    (0x01355bd0, "istream::getline"),  # size=384, subsystem=C++ Stdlib
    (0x01355d50, "istream::get"),  # size=272, subsystem=C++ Stdlib
    (0x01355fa0, "istream::gets"),  # size=276, subsystem=C++ Stdlib
    (0x01356160, "istream::scan"),  # size=228, subsystem=C++ Stdlib
    (0x01356248, "istream::vscan"),  # size=176, subsystem=C++ Stdlib
    (0x01356348, "streambuf::vscan"),  # size=64, subsystem=C++ Stdlib
    (0x01356388, "streambuf::scan"),  # size=96, subsystem=C++ Stdlib
    (0x01356430, "stdiobuf::constructor"),  # size=136, subsystem=C++ Stdlib
    (0x013564b8, "stdiobuf::~destructor"),  # size=124, subsystem=C++ Stdlib
    (0x01356538, "stdiobuf::sys_read"),  # size=160, subsystem=C++ Stdlib
    (0x013565d8, "stdiobuf::sys_write"),  # size=92, subsystem=C++ Stdlib
    (0x01356638, "stdiobuf::sys_seek"),  # size=28, subsystem=C++ Stdlib
    (0x01356658, "stdiobuf::sys_close"),  # size=44, subsystem=C++ Stdlib
    (0x01356688, "stdiobuf::sync"),  # size=92, subsystem=C++ Stdlib
    (0x013566e8, "stdiobuf::overflow"),  # size=92, subsystem=C++ Stdlib
    (0x01356748, "stdiobuf::xsputn"),  # size=100, subsystem=C++ Stdlib
    (0x013567b0, "stdiobuf::buffered"),  # size=104, subsystem=C++ Stdlib
    (0x01356920, "stdiobuf::__typeinfo"),  # size=80, subsystem=C++ Stdlib
    (0x01356990, "istdiostream::~destructor"),  # size=244, subsystem=C++ Stdlib
    (0x01356a88, "istdiostream::__typeinfo"),  # size=84, subsystem=C++ Stdlib
    (0x01356ae0, "istdiostream::constructor"),  # size=484, subsystem=C++ Stdlib
    (0x01356cc8, "istdiostream::rdbuf"),  # size=8, subsystem=C++ Stdlib
    (0x01356ce8, "istdiostream::buffered"),  # size=28, subsystem=C++ Stdlib
    (0x01356d08, "ostdiostream::~destructor"),  # size=244, subsystem=C++ Stdlib
    (0x01356e00, "ostdiostream::__typeinfo"),  # size=84, subsystem=C++ Stdlib
    (0x01356e58, "ostdiostream::constructor"),  # size=476, subsystem=C++ Stdlib
    (0x01357038, "ostdiostream::rdbuf"),  # size=8, subsystem=C++ Stdlib
    (0x01357058, "ostdiostream::buffered"),  # size=28, subsystem=C++ Stdlib
    (0x01357708, "ios::sync_with_stdio"),  # size=128, subsystem=C++ Stdlib
    (0x01357898, "streambuf::_un_link"),  # size=28, subsystem=C++ Stdlib
    (0x013578b8, "streambuf::_link_in"),  # size=28, subsystem=C++ Stdlib
    (0x013578d8, "streambuf::switch_to_get_mode"),  # size=20, subsystem=C++ Stdlib
    (0x013578f0, "streambuf::free_backup_area"),  # size=28, subsystem=C++ Stdlib
    (0x01357940, "streambuf::underflow"),  # size=8, subsystem=C++ Stdlib
    (0x01357948, "streambuf::uflow"),  # size=20, subsystem=C++ Stdlib
    (0x01357960, "streambuf::overflow"),  # size=8, subsystem=C++ Stdlib
    (0x01357968, "streambuf::xsputn"),  # size=44, subsystem=C++ Stdlib
    (0x01357998, "streambuf::xsgetn"),  # size=44, subsystem=C++ Stdlib
    (0x013579c8, "streambuf::ignore"),  # size=136, subsystem=C++ Stdlib
    (0x01357a50, "streambuf::sync"),  # size=8, subsystem=C++ Stdlib
    (0x01357a58, "streambuf::pbackfail"),  # size=20, subsystem=C++ Stdlib
    (0x01357a70, "streambuf::setbuf"),  # size=224, subsystem=C++ Stdlib
    (0x01357b50, "streambuf::seekpos"),  # size=56, subsystem=C++ Stdlib
    (0x01357b88, "streambuf::sseekpos"),  # size=20, subsystem=C++ Stdlib
    (0x01357ba0, "streambuf::setb"),  # size=28, subsystem=C++ Stdlib
    (0x01357bc0, "streambuf::doallocate"),  # size=20, subsystem=C++ Stdlib
    (0x01357bd8, "streambuf::doallocbuf"),  # size=28, subsystem=C++ Stdlib
    (0x01357bf8, "streambuf::constructor"),  # size=32, subsystem=C++ Stdlib
    (0x01357c18, "streambuf::~destructor"),  # size=100, subsystem=C++ Stdlib
    (0x01357c80, "streambuf::seekoff"),  # size=8, subsystem=C++ Stdlib
    (0x01357c88, "streambuf::sseekoff"),  # size=20, subsystem=C++ Stdlib
    (0x01357ca0, "streambuf::sputbackc"),  # size=28, subsystem=C++ Stdlib
    (0x01357cc0, "streambuf::sungetc"),  # size=20, subsystem=C++ Stdlib
    (0x01357cd8, "streambuf::get_column"),  # size=60, subsystem=C++ Stdlib
    (0x01357d18, "streambuf::set_column"),  # size=16, subsystem=C++ Stdlib
    (0x01357d28, "streambuf::flush_all"),  # size=20, subsystem=C++ Stdlib
    (0x01357d40, "streambuf::flush_all_linebuffered"),  # size=28, subsystem=C++ Stdlib
    (0x01357d60, "streambuf::sys_stat"),  # size=40, subsystem=C++ Stdlib
    (0x01357d88, "streambuf::sys_read"),  # size=8, subsystem=C++ Stdlib
    (0x01357d90, "streambuf::sys_write"),  # size=8, subsystem=C++ Stdlib
    (0x01357d98, "streambuf::sys_seek"),  # size=8, subsystem=C++ Stdlib
    (0x01357da0, "streambuf::sys_close"),  # size=8, subsystem=C++ Stdlib
    (0x01357da8, "streammarker::constructor"),  # size=20, subsystem=C++ Stdlib
    (0x01357dc0, "streammarker::~destructor"),  # size=84, subsystem=C++ Stdlib
    (0x01357e18, "streammarker::delta"),  # size=20, subsystem=C++ Stdlib
    (0x01357e30, "streammarker::delta"),  # size=20, subsystem=C++ Stdlib
    (0x01357e48, "streambuf::seekmark"),  # size=20, subsystem=C++ Stdlib
    (0x01357e60, "streambuf::unsave_markers"),  # size=28, subsystem=C++ Stdlib
    (0x01357e80, "ios::readable"),  # size=24, subsystem=C++ Stdlib
    (0x01357e98, "ios::writable"),  # size=24, subsystem=C++ Stdlib
    (0x01357eb0, "ios::is_open"),  # size=36, subsystem=C++ Stdlib
    (0x013580e0, "ios::__typeinfo"),  # size=80, subsystem=C++ Stdlib
    (0x01358138, "ios::tie"),  # size=12, subsystem=C++ Stdlib
    (0x01358150, "ios::fill"),  # size=12, subsystem=C++ Stdlib
    (0x01358168, "ios::flags"),  # size=12, subsystem=C++ Stdlib
    (0x01358180, "ios::precision"),  # size=16, subsystem=C++ Stdlib
    (0x01358190, "ios::setf"),  # size=16, subsystem=C++ Stdlib
    (0x013581a0, "ios::setf"),  # size=28, subsystem=C++ Stdlib
    (0x013581c0, "ios::unsetf"),  # size=20, subsystem=C++ Stdlib
    (0x013581e0, "ios::width"),  # size=12, subsystem=C++ Stdlib
    (0x013581f8, "ios::clear"),  # size=24, subsystem=C++ Stdlib
    (0x01358210, "ios::set"),  # size=16, subsystem=C++ Stdlib
    (0x01358220, "ios::setstate"),  # size=16, subsystem=C++ Stdlib
    (0x013582a8, "ios::exceptions"),  # size=8, subsystem=C++ Stdlib
    (0x013582b8, "ios::rdbuf"),  # size=24, subsystem=C++ Stdlib
    (0x013582d0, "ios::sync_with_stdio"),  # size=28, subsystem=C++ Stdlib
    (0x013582f0, "ios::unset"),  # size=20, subsystem=C++ Stdlib
    (0x01358310, "streammarker::set_offset"),  # size=8, subsystem=C++ Stdlib
    (0x01358318, "streammarker::saving"),  # size=8, subsystem=C++ Stdlib
    (0x01358320, "streambuf::__typeinfo"),  # size=80, subsystem=C++ Stdlib
    (0x01358370, "streambuf::_vtable"),  # size=8, subsystem=C++ Stdlib
    (0x01358378, "streambuf::xchain"),  # size=8, subsystem=C++ Stdlib
    (0x01358418, "streambuf::xput_char"),  # size=24, subsystem=C++ Stdlib
    (0x01358430, "streambuf::xflags"),  # size=8, subsystem=C++ Stdlib
    (0x01358438, "streambuf::xflags"),  # size=12, subsystem=C++ Stdlib
    (0x01358448, "streambuf::xsetflags"),  # size=16, subsystem=C++ Stdlib
    (0x01358458, "streambuf::xsetflags"),  # size=28, subsystem=C++ Stdlib
    (0x01358478, "streambuf::gbump"),  # size=44, subsystem=C++ Stdlib
    (0x013584a8, "streambuf::pbump"),  # size=16, subsystem=C++ Stdlib
    (0x013584b8, "streambuf::setp"),  # size=16, subsystem=C++ Stdlib
    (0x013584c8, "streambuf::setg"),  # size=100, subsystem=C++ Stdlib
    (0x01358530, "streambuf::shortbuf"),  # size=8, subsystem=C++ Stdlib
    (0x01358538, "streambuf::in_backup"),  # size=12, subsystem=C++ Stdlib
    (0x01358548, "streambuf::Gbase"),  # size=32, subsystem=C++ Stdlib
    (0x01358568, "streambuf::eGptr"),  # size=32, subsystem=C++ Stdlib
    (0x01358588, "streambuf::Bbase"),  # size=32, subsystem=C++ Stdlib
    (0x013585a8, "streambuf::Bptr"),  # size=8, subsystem=C++ Stdlib
    (0x013585b0, "streambuf::eBptr"),  # size=32, subsystem=C++ Stdlib
    (0x013585d0, "streambuf::Nbase"),  # size=8, subsystem=C++ Stdlib
    (0x013585d8, "streambuf::eNptr"),  # size=8, subsystem=C++ Stdlib
    (0x013585e0, "streambuf::have_backup"),  # size=12, subsystem=C++ Stdlib
    (0x013585f0, "streambuf::have_markers"),  # size=12, subsystem=C++ Stdlib
    (0x01358600, "streambuf::put_mode"),  # size=12, subsystem=C++ Stdlib
    (0x01358610, "streambuf::pubseekoff"),  # size=20, subsystem=C++ Stdlib
    (0x01358628, "streambuf::pubseekpos"),  # size=20, subsystem=C++ Stdlib
    (0x01358640, "streambuf::unbuffered"),  # size=16, subsystem=C++ Stdlib
    (0x01358650, "streambuf::linebuffered"),  # size=16, subsystem=C++ Stdlib
    (0x01358660, "streambuf::unbuffered"),  # size=40, subsystem=C++ Stdlib
    (0x01358688, "streambuf::linebuffered"),  # size=40, subsystem=C++ Stdlib
    (0x013586b0, "streambuf::allocate"),  # size=80, subsystem=C++ Stdlib
    (0x01358700, "streambuf::allocbuf"),  # size=40, subsystem=C++ Stdlib
    (0x01358728, "streambuf::in_avail"),  # size=16, subsystem=C++ Stdlib
    (0x01358738, "streambuf::out_waiting"),  # size=16, subsystem=C++ Stdlib
    (0x01358748, "streambuf::sputn"),  # size=48, subsystem=C++ Stdlib
    (0x01358778, "streambuf::padn"),  # size=28, subsystem=C++ Stdlib
    (0x01358798, "streambuf::sgetn"),  # size=44, subsystem=C++ Stdlib
    (0x013587c8, "streambuf::sputc"),  # size=32, subsystem=C++ Stdlib
    (0x013587e8, "streambuf::sbumpc"),  # size=20, subsystem=C++ Stdlib
    (0x01358800, "streambuf::sgetc"),  # size=84, subsystem=C++ Stdlib
    (0x01358858, "streambuf::snextc"),  # size=128, subsystem=C++ Stdlib
    (0x013588d8, "streambuf::stossc"),  # size=32, subsystem=C++ Stdlib
    (0x013588f8, "filebuf::__typeinfo"),  # size=80, subsystem=C++ Stdlib
    (0x01358970, "filebuf::is_reading"),  # size=52, subsystem=C++ Stdlib
    (0x013589a8, "filebuf::cur_ptr"),  # size=80, subsystem=C++ Stdlib
    (0x013589f8, "filebuf::file_ptr"),  # size=32, subsystem=C++ Stdlib
    (0x01358a18, "ios::init"),  # size=76, subsystem=C++ Stdlib
    (0x01358a68, "ios::constructor"),  # size=92, subsystem=C++ Stdlib
    (0x01358ac8, "ios::~destructor"),  # size=100, subsystem=C++ Stdlib
    (0x01358b30, "_ios_fields::__typeinfo"),  # size=64, subsystem=C++ Runtime
    (0x01358b70, "_IO_FILE::__typeinfo"),  # size=64, subsystem=C++ Runtime
]
