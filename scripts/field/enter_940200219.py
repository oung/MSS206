# id 940200219 (Arcana : Near the Bramble Harp), field 940200219
sm.completeQuestNoCheck(34490)
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(300)
sm.spawnNpc(3003350, -360, 50)
sm.showNpcSpecialActionByTemplateId(3003350, "summon", 0)
sm.spawnNpc(3003365, 260, 50)
sm.showNpcSpecialActionByTemplateId(3003365, "summon", 0)
sm.spawnNpc(3003357, 490, 50)
sm.showNpcSpecialActionByTemplateId(3003357, "summon", 0)
sm.spawnNpc(3003372, 780, 50)
sm.showNpcSpecialActionByTemplateId(3003372, "summon", 0)
sm.showNpcSpecialActionByTemplateId(3003365, "stand2", -1)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003309) # Tree Spirits
sm.sendNext("#face0#We warned you to leave this place...")
sm.sendSay("#face0#I knew it! You pretended not to be the same stranger, but you're clearly up to no good...")
sm.zoomCamera(2000, 1500, 2000, 180, 50)
sm.moveNpcByTemplateId(3003350, False, 350, 140)
sm.sendDelay(300)
sm.forcedMove(False, 380)
sm.sendDelay(900)
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendNext("#face0#We were just trying to revive the Bramble Harp! Just wait, any moment now it will be brimming with life!")
sm.sendDelay(600)
sm.setInnerOverrideSpeakerTemplateID(3003309) # Tree Spirits
sm.sendNext("#face0#The harp is dead! Just like this slowly-withering forest...\r\nThere is no hope, no coming back.")
sm.sendSay("#face0#You ignored our warning, stranger. Now you will face the consequences.")
sm.showEffect("Effect/Direction19.img/effect/arcana_tree/0", 800, 0, 0, 0, 173164485, 0, 0)
sm.sendDelay(700)
sm.avatarOriented("Effect/Direction19.img/effect/arcana_tree/0")
sm.showEffect("Effect/Direction19.img/effect/arcana_tree/1", 180000, 0, 0, 0, 173164485, 0, 0)
sm.setInnerOverrideSpeakerTemplateID(3003328) # Rescued Tree Spirit
sm.sendNext("#face0#No, stop!")
sm.zoomCamera(1000, 1500, 1000, 230, 50)
sm.moveNpcByTemplateId(3003372, True, 130, 200)
sm.sendDelay(1200)
sm.sendNext("#face0#Can't you see?! The Bramble Harp is beginning to bloom!")
sm.resetNpcSpecialActionByTemplateId(3003365)
sm.showNpcSpecialActionByTemplateId(3003365, "change", 0)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/harp", 200)
sm.sendDelay(2000)
sm.startQuest(34490)
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(3003301) # Small Spirit
sm.sendNext("#face2#Ah, that beautiful sound... How I've missed it.")
sm.setInnerOverrideSpeakerTemplateID(3003309) # Tree Spirits
sm.sendSay("#face0#.........................")
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(940200216)
