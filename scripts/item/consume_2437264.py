# id 2437264 (Medicine), field 402000002
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001271)
sm.sendNext("#face6##b(The bitter taste of the medicine takes me back to a time when I was at my weakest.)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/8", 128)
sm.sendSay("#face6##b(That was the day I met the boss... After waking up from one long nightmare to another, I had never felt so helpless.)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/9", 128)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.bgmVolume(0, 2000)
sm.sendDelay(2000)
sm.changeBGM("Bgm00.img/Silence", 0, 0)
sm.onLayer(900, "00", 0, -80, 12, "Effect/Direction19.img/effect/cadena_dir/0", 4, False, -1, False)
sm.sendDelay(1000)
sm.sendNext("#face8#Let me go, I have to get to the castle!")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/0", 128)
sm.sendSay("#face9#I don't have time for this!")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/1", 128)
sm.setInnerOverrideSpeakerTemplateID(3001250)
sm.sendSay("#face2#Calm yourself!")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/10", 128)
sm.sendSay("#face2#There's no one left there to save. You were the only survivor.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/11", 128)
sm.offLayer(300, "00", False)
sm.onLayer(900, "01", 0, -80, 12, "Effect/Direction19.img/effect/cadena_dir/1", 4, False, -1, False)
sm.setInnerOverrideSpeakerTemplateID(3001271)
sm.sendSay("#face10#W-what?")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/2", 128)
sm.setInnerOverrideSpeakerTemplateID(3001250)
sm.sendSay("#face2#They're all dead. It's been years since the castle was taken. The General found you and saw you were still breathing, but no one else was so lucky.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/12", 128)
sm.setInnerOverrideSpeakerTemplateID(3001271)
sm.sendSay("#face10#...")
sm.setInnerOverrideSpeakerTemplateID(3001250)
sm.sendSay("#face2#...When the general brought you here, you were hanging onto life by a thread.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/13", 128)
sm.sendSay("#face2#In the end, you survived, but the medicine that saved your life also put you into a coma.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/14", 128)
sm.setInnerOverrideSpeakerTemplateID(3001271)
sm.sendSay("#face10#Why... Why did you save me?")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/3", 128)
sm.setInnerOverrideSpeakerTemplateID(3001250)
sm.sendSay("#face2#I didn't do it out of the goodness of my heart if that's what you're thinking. It was a favor to the general. You should be grateful to him.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/15", 128)
sm.offLayer(300, "01", False)
sm.onLayer(900, "02", 0, -80, 12, "Effect/Direction19.img/effect/cadena_dir/2", 4, False, -1, False)
sm.sendDelay(500)
sm.sendNext("#face2#Anyway, I've kept my promise. You're alive and awake. I've no more obligation to protect you. You'd better learn to fend for yourself.")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/16", 128)
sm.offLayer(300, "02", False)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setInnerOverrideSpeakerTemplateID(3001271)
sm.sendNext("#face0##b(Not long after I awoke, I started working for the local branch of Shadowdealers. The naive and cowardly royal I was before was dead. I would need a new name...)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/4", 128)
sm.sendSay("#face0##b(I reinvented myself as Cadena, and took up the chain as my weapon. In doing so, I vowed that I would never be helpless again.)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/5", 128)
sm.sendSay("#face0##b(My only thought was of be56coming stronger, no matter the cost. I would climb the Shadowdealers' ranks until there was no one above me.)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/6", 128)
sm.sendSay("#face0##b(I'm going to get stronger and stronger... And someday I'll claw my way to the top of this darkness. I will never forget my vow, or this throbbing pain in my heart.)#k")
sm.playExclSoundWithDownBGM("Voice3.img/cadena/Q2/Male/7", 128)
sm.completeQuest(34603)
sm.consumeItem(2437264)
sm.lockInGameUI(False, True)