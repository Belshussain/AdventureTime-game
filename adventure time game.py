answer = input("Would you like to embark on this journey? (enter yes or no) ")

if answer.lower() == "yes":
    print('')
else:
    quit()

name = input('Please enter your name young traveller: ')
print('Splended to meet you', name, 'Welcome to this adventure!')

answer = input('You are walking on a long dirt road. You finally arrive at the end of the road but, there are only 2 paths. Do you want to go right or left? ').lower()

if answer == 'left':
    answer = input('After a long walk, you finally arrive at a wooden house. Do you enter, or ignore and keep walking? Type enter to enter the house and ignore to carry on walking ').lower()

    if answer == 'enter':
        print('You walk towards the wooden house and enter through the door. Suddenly you hear cracking. The roof begins to collapse and you run towards the door. You trip and the roof collapses ontop of you. You die. ')

    
    elif answer == 'ignore':
        print('After ignoring the wooden house, you walk for what seems to be ages. You run out of water and food. You die due to dehydration')


    else:
        print('You didnt enter a valid answer. You Lose')



elif answer == 'right':
    answer = input('You arrive at a river that is blocking your path. You can either swim across or go around. Enter swim to swim across or around to go around it').lower()
    
    if answer == 'swim':
        print('You felt something grab onto your feet. It was a mermaid. You got dragged to the bottom of the river and drowned.')

    elif answer == 'around':
        answer = input('The only way around was through a dark enchanted forest.Upon entry you are greeted by fairies. They give you food and water. They offer to join you on your journey ahead. Do you allow them to join you ? (yes/no)').lower()
        
        if answer == 'yes':
            print('The fairies prove to be very helpful and trustworthy. They help you safely on your journey until you reach your destination. YOU WON! ')

        elif answer == 'no':
            print('You thank the fairies for their hospitality and then continue on your journey. You arrive at a bridge. You decide to cross the bridge quickly. It breaks underneath you and you fall to your death ')
        
        else:
            print('You didnt enter a valid answer. You Lose')

else:
    print('You didnt enter a valid answer. You Lose')

print('Thank you for playing ',name)