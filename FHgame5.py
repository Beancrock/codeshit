'''
very loose game idea. essentially glorified "paper, rock, sissors" but hoping for ideas
to create more depth and strategy.
You'll notice a pattern, which is important to maintain for balance and semetry.
further to the right = stronger and further to the left = weaker, middle is character in question.

archer < shield < axe
shield < axe < archer
axe < archer < shield
  
pike, archer < shield < calvary, axe
archer, shield < calvary < axe, pike
shield ,calvary < axe < pike, archer   
calvary, axe < pike < archer, shield
axe, pike < archer < shield, calvary

?12/60, 15/60, 20/60 < 30/60 < 40/60, 45/60, 48/60?

pike, wizard, archer, < shield < rogue, calvary, axe   
wizard, archer, shield < rogue < calvary, axe, pike
archer, shield, rogue < calvary < axe, pike, wizard
shield, rogue, calvary < axe < pike, wizard, archer  
rogue, calvary, axe < pike < wizard, archer, shield   
calvary, axe, pike < wizard < archer, shield, rogue 
axe, pike, wizard < archer < shield, rogue, calvary  

-A
D\P R S *
-P
-R
-S

W, N, B, C

[1PP][][][][][][][][2PP]
[1PR][][][][][][][][2PR]
[1PS][][][][][][][][2PS]
[1P*][][][][][][][][2P*]
[1RP][][][][][][][][2RP]
[1RR][][][][][][][][2RR]
[1RS][][][][][][][][2RS]
[1R*][][][][][][][][2R*]
[1SP][][][][][][][][2SP]
[1SR][][][][][][][][2SR]
[1SS][][][][][][][][2SS]
[1S*][][][][][][][][2S*]

* = ranged attack, but no defense
W = wizard, no attack or defense, swap position with another until as turn action
N = ninja, no defense, position invisible except on attacking move 
B = Berzerker, all suit attack, no defense
C = cleric, returns dead unit to deck upon moving to it's spot
'''