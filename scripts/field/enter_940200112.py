# id 940200112 (Hidden Street : Twilight Training Grounds), field 940200112
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.zoomCamera(0, 1000, 0, -5, 160)
sm.sendDelay(500)
sm.spawnNpc(3003274, 2400, 180)
sm.showNpcSpecialActionByTemplateId(3003274, "summon", 0)
sm.spawnNpc(3003271, -200, 180)
sm.showNpcSpecialActionByTemplateId(3003271, "summon", 0)
sm.spawnNpc(3003275, 2850, 180)
sm.showNpcSpecialActionByTemplateId(3003275, "summon", 0)
sm.spawnNpc(3003278, 2900, 180)
sm.showNpcSpecialActionByTemplateId(3003278, "summon", 0)
sm.sendDelay(1000)
sm.blind(False, 0, 0, 0, 0, 1500)
sm.moveNpcByTemplateId(3003271, False, 250, 160)
sm.sendDelay(1500)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendNext("#face1#...The more I think about it, the more certain I am I can't give up.")
sm.moveNpcByTemplateId(3003271, True, 70, 160)
sm.sendSay("#face1#Why did I hesitate? I should have been the first to offer my help! If I hadn't waited, things could've turned out differently...")
sm.sendSay("#face2#...Be brave, Lucid. You can convince her! There's still time!")
sm.moveNpcByTemplateId(3003271, False, 230, 160)
sm.zoomCamera(2000, 1000, 2000, 300, 160)
sm.sendDelay(2000)
sm.zoomCamera(3000, 1000, 3000, 2600, 160)
sm.sendDelay(3000)
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendNext("#face0#Your Majesty!")
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.zoomCamera(0, 2000, 0, 2600, 260)
sm.sendDelay(500)
sm.zoomCamera(3000, 2000, 3000, 2900, 260)
sm.moveNpcByTemplateId(3003274, False, 250, 160)
sm.sendNext("#face0#Your Majesty, wait! I still have something to say!")
sm.sendDelay(500)
sm.spawnNpc(3003271, 2350, -20)
sm.showNpcSpecialActionByTemplateId(3003271, "summon", 0)
sm.setInnerOverrideSpeakerTemplateID(3003275) # Danika
sm.sendNext("If you're here to ask to tag along, I won't hear it. Return to the village.")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face0#You're right. That's what I came here to say. But... I have to come! Because I...")
sm.zoomCamera(1000, 2000, 1000, 2800, 260)
sm.sendDelay(500)
sm.moveNpcByTemplateId(3003271, False, 130, 160)
sm.sendDelay(1500)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, 0, 0, 134960159, 0, 0)
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(3003278) # Mercedes
sm.sendNext("Very well.")
sm.blind(True, 200, 0, 0, 0, 1300)
sm.sendDelay(1600)
sm.onLayer(1000, "lucid", 0, -80, 0, "Map/Effect3.img/Lacheln/episode3", 4, True, -1, False)
sm.sendNext("Athena, I want you to carry this with you. ")
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendSay("#face3#...")
sm.setInnerOverrideSpeakerTemplateID(3003274) # Athena Pierce
sm.sendSay("#face0#That's the Mistelteinn!")
sm.setInnerOverrideSpeakerTemplateID(3003278) # Mercedes
sm.sendSay("It will protect you.")
sm.sendDelay(1500)
sm.setInnerOverrideSpeakerTemplateID(3003270) # Lucid
sm.sendNext("#face3#No... She gets everything handed to her! And now even Elluel's greatest treasure, the Mistelteinn...")
sm.sendSay("#face4#There's nothing I can say or do that will change anything... Athena Pierce will always be her favorite...")
sm.sendSay("#face4#I hate them all. Athena Pierce, this stupid kingdom, and everyone in it! Why do they stand in my way?!")
sm.offLayer(500, "lucid", False)
sm.playSound("Sound/SoundEff.img/ArcaneRiver/butterfly0", 200)
sm.spineScreen(True, False, False, 0, "Map/Effect3.img/BossLucid/butterfly/005","animation","")
sm.sendDelay(5000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(450003000)
