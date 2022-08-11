# id 910370111 (null), field 910370111
sm.lockInGameUI(True, False)
sm.forcedInput(2)
sm.sendDelay(1400)
sm.forcedInput(1)
sm.sendDelay(30)
sm.forcedInput(0)
sm.setSpeakerType(3)
sm.setSpeakerID(1052001) # Dark Lord
sm.setParam(1)
sm.sendNext("Listen up, #b#h0#!#k! I'm going to give you a rough overview of the Shadower skills.")
res = sm.sendNext("First, let me ask you something. Do you know which one of the following is a basic Shadower skill?\r\n\r\n#b#L0#Critical Growth#l\r\n#L1#Freezing Crush#l\r\n#L2#Combo Attack#l")
sm.sendNext("Yeah, #bCritical Growth#k is the right answer!")
sm.sendSay("Do you want to know what kind of skill it is? Well, let me show you what it can do.")
sm.showEffect("Effect/CharacterEff.img/advTutorial/skillUI/4200013", 0, -450, -200, 0, 0, 0, 0)
sm.sendDelay(2520)
sm.sendNext("As you can see, this skill will increase your Critical Rate continuously.")
sm.setParam(3)
sm.sendSay("I know how important the basics are, but... Can I see the #rmost powerful skill#k out of all the Shadower skills?")
sm.setParam(1)
sm.sendSay("Of course. In fact, I will give you a chance to try them out! The two top skills are #rAssassinate#k and #rShadower Instinct#k.")
sm.showEffect("Effect/CharacterEff.img/advTutorial/skillUI/4221001", 0, -460, -200, 0, 0, 0, 0)
sm.showEffect("Effect/CharacterEff.img/advTutorial/skillUI/4221013", 0, -135, -200, 0, 0, 0, 0)
sm.sendDelay(2520)
sm.sendNext("These skills are different from any other attack and buff skills. They become much more powerful when you have a high #bBody Count#k.")
sm.setParam(3)
sm.sendSay("#bBody Count#k?")
sm.setParam(1)
sm.sendSay("Yes. Your Body Count refers to the points that you gain for attacking enemies. You'll find it in the upper right corner, shown as a buff icon.")
sm.sendSay("#i3800573#, #i3800574#, #i3800575#, #i3800576#, and #i3800577#!")
sm.sendSay("See #i3800577#? You'll see some incredible effects if you use the #bAssassinate#k and #bShadower Instinct#k skills when you see this icon.")
res = sm.sendAskYesNo("That's the end of the Shadower skill tutorial. Ready to move on?\r\n#r(Press Yes to return your original location.)#k")
sm.lockInGameUI(False, True)
sm.warp(610050000)
