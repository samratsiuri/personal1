mood=str(input('What is your current mood?(happy/tired/bored/energetic): '))
weather=str(input('What is the current weather?(sunny/rainy/cold/windy): '))
if mood=='happy' and weather=='sunny':
    print('Great!! what a lovely day for a picnic.')
elif    mood=='happy' and weather=='rainy':
    print('Put on some music, and maybe dance in the rain?')
elif    mood=='happy' and weather=='cold':
    print('How about some hot coffee and a good book?')
elif    mood=='happy' and weather=='windy':
    print('Take a walk, let the wind match your vibe.')
elif    mood=='tired' and weather=='sunny':
    print('Sit by the window, put on some good music. Let your mind be free.')
elif    mood=='tired' and weather=='rainy':
    print('Snug into your blanket, put on Netflix.')
elif mood == 'tired' and weather == 'cold':
    print('Warm soup, soft music and an early nap-- self-care time.')
elif    mood=='tired' and weather=='windy':
    print("Don't go out, try to write something.")
elif    mood=='bored' and weather=='sunny':
    print('Call a friend and go for a random walk-adventure is out there.')
elif    mood=='bored' and weather=='rainy':
    print("Try a cook a new recipe. Don't forget to put on the music.")
elif mood == 'bored' and weather == 'cold':
    print('Get into the blanket, watch a movie.')
elif    mood=='bored' and weather=='windy':
    print("Go to the nearby bookstore or explore a new coffee shop.")
elif    mood=='energetic' and weather=='sunny':
    print('Go hiking, cycling or just go out.')
elif    mood=='energetic' and weather=='rainy':
    print("Do some indoor workout. Keep the energy flowing.")
elif mood == 'energetic' and weather == 'cold':
    print('Take a walk, the chill will wake up your senses.')
elif    mood=='energetic' and weather=='windy':
    print("Go for a run. Let nature boost your mind.")
else:
    print('none')
print('Have a nice day!!!')