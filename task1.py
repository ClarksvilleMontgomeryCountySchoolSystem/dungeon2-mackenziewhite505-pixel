good = r'''
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          '''
print(good)
bad = r'''
   .-._______
  .={ . }..--""
 [/"`._.'    fsc








             , .
      _-|---= *:--
   ._(O)/     ' `
   '''
print(bad)
torch_lit = True
if torch_lit:
    outcome = "Flicker: Yay! There's light"
else:
    outcome = "Doom: Who blew the torch out?"
print(outcome)