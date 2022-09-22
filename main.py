import random
from sys import maxsize

class_type = input('Choose your class(Warrior or Mage): ')
dice_roll = 0
action_result = ''

max_hp = 0
power = 0
block = 0
# charisma = 0
encounter_chance = 0
special_power_one = ''
special_power_two = ''
current_hp = 0
condition = True

if class_type == 'Warrior':
    current_hp = 13
    max_hp = 13
    power += 13
    block += 8
    # charisma += 10
    special_power_one = 'Strike'
    special_power_two = 'Cleave'
elif class_type == 'Mage':
    current_hp = 12
    max_hp = 12
    power += 22
    block += 5
    # charisma += 10
    special_power_one = 'Ignite'
    special_power_two = 'Fireball'
# elif class_type == 'Bard':
#     current_hp = 10
#     max_hp = 10
#     power += 12
#     block += 10
#     charisma += 20
else:
    condition = False
    print('Please select a valid class!')
info = input('Do you need info for the class?(Y/N): ')
if info == 'Y':
    if class_type == 'Warrior':
        print(f"The Warrior is an unstoppable brute force always ready to fight. He specializes in melee fighting.\n"
              f"His special abilities are Cleave and Strike.\n"
              f"Strike has 80% chance to hit while doing the current warrior's power.\n"
              f"Cleave has 50% chance to instantly kill any foe.\n"
              f"Attributes:\n"
              f" Max HP = {max_hp}\n"
              f" Power = {power}\n"
              f" Block = {block}\n")
    # f" Charisma = {charisma}")
    elif class_type == 'Mage':
        print('The Mage has studied his whole life to gain power unimaginable to human beings thus possessing\n'
              'great strength but due to his lack of physical training he is more or less fragile.\n'
              'His special abilities are Ignite and Fireball.\n'
              "Ignite has 80% chance to hit while doing the current mage's power.\n"
              "Fireball has 50% chance to instantly kill any foe.\n"
              f"Attributes:\n"
              f" Max HP = {max_hp}\n"
              f" Power = {power}\n"
              f" Block = {block}\n")
    # f" Charisma = {charisma}")
    elif class_type == 'Bard':
        pass
else:
    pass

decide = ''
# for rooms
rooms = maxsize
rooms_cleared = 0

# for events in general
event_chance = 0
game_over = False

if condition:
    decide = input('Begin your adventure?(Y/N): ')
    if decide == 'Y':
        print('You come across an abandoned dungeon. As your interest grows bigger you enter the'
              ' twisted location and \n'
              'the door behind you shuts close!')

        if condition:
            for _ in range(0, rooms):
                if game_over:
                    break
                rooms_cleared += 1
                monster_list = ['Ogre', 'Troll', 'Goblin', 'Minotaur', 'Harpy', 'Giant Snake',
                                'Big Tarantula', 'Катаджия']
                monster = random.choice(monster_list)
                rng = random.randint(20, 131)
                rng_chest = random.randint(1, 101)
                movement = input('You come across 2 doors each leading to different paths.\n'
                                 'Which door do you take?(Left or Right):')
                if movement == 'Right':
                    encounter_chance = random.randint(1, 101)
                    if encounter_chance <= 10:
                        event = input(
                            f'As you enter the {movement} door you stumble upon a treasure room containing a '
                            f'big chest.\n'
                            f' What do you do?(Open or Skip): ')
                        if event == 'Open':
                            event_chance = random.randint(1, 101)
                            if event_chance <= 10:
                                print('You find nothing in the chest.')
                            elif event_chance <= rng_chest:
                                max_hp += 2
                                current_hp += 2
                                power += 2
                                block += 2
                                # charisma += 2
                                print('You find an artifact which grants you all stats up (+ 2)')
                                print(f'Your stats now are as it follows: HP = {current_hp} / {max_hp},'
                                      f' Power = {power}, '
                                      f'Block = {block},')
                            # f' Charisma = {charisma}')
                            else:
                                print('You find an artifact which is cursed! It takes away stats from you (- 2)')
                                max_hp -= 2
                                current_hp -= 2
                                power -= 2
                                block -= 2
                                if current_hp <= 0:
                                    game_over = True
                                # charisma -= 2
                                print(f'Your stats now are as it follows: HP = {current_hp} / {max_hp},'
                                      f' Power = {power},'
                                      f' Block = {block},')
                        # f' Charisma = {charisma}')
                        elif event == 'Skip':
                            pass
                    elif encounter_chance <= rng:
                        action = input(f'As you enter the {movement} door you stumble upon a {monster}.\n'
                                       f' His total hp and power is 15 and can only be killed in 1 hit.\n'
                                       f' What do you do?({special_power_one} / {special_power_two}): ')
                        if action == special_power_one:
                            dice_roll = random.randint(1, 101)
                            if dice_roll <= 80:
                                action_result = 'hit'
                            else:
                                action_result = 'miss'
                            if action_result == 'hit':
                                print('The monster gets hit! Finish him while you still can!')
                                action_two = input(
                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                if action_two == special_power_one:
                                    dice_roll = random.randint(1, 101)
                                    if dice_roll <= 80:
                                        action_result = 'hit'
                                    else:
                                        action_result = 'miss'
                                    if action_result == 'hit':
                                        print('The monster falls to the ground defeated')
                                        print('You may proceed.')
                                    elif action_result == 'miss':
                                        damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                        if damage_done < 0:
                                            damage_done = 0
                                        current_hp -= damage_done
                                        if current_hp <= 0:
                                            game_over = True
                                            print(
                                                f'You miss the {monster} and then he strikes'
                                                f' you for 15 killing you\n'
                                                f' and ending your journey. GAME OVER!')

                                        else:
                                            print(
                                                f'You miss the {monster} and then it strikes you for 15 leaving'
                                                f' you on {current_hp}HP.')
                                            print('The monster is badly hurt and leaves you be... for now.')
                                elif action_two == special_power_two:
                                    dice_roll = random.randint(1, 101)
                                    if dice_roll <= 50:
                                        action_result = 'hit'
                                    else:
                                        action_result = 'miss'
                                    if action_result == 'hit':
                                        print('The monster falls to the ground defeated')
                                        print('You may proceed.')
                                    elif action_result == 'miss':
                                        damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                        if damage_done < 0:
                                            damage_done = 0
                                        current_hp -= damage_done
                                        if current_hp <= 0:
                                            game_over = True
                                            print(
                                                f'You miss the {monster} and then it strikes'
                                                f' you for 15 killing you\n'
                                                f' and ending your journey. GAME OVER!')
                                        else:
                                            print(
                                                f'You miss the {monster} and then it strikes you'
                                                f' for 15 leaving you on {current_hp}HP.')
                                            print('The monster is badly hurt and leaves you be... for now.')
                            elif action_result == 'miss':
                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                if damage_done < 0:
                                    damage_done = 0
                                current_hp -= damage_done
                                if current_hp <= 0:
                                    print(f'You miss the {monster} and then it strikes you for 15 killing you\n'
                                          f' and ending your journey. GAME OVER!')
                                else:
                                    print(
                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                        f' you on {current_hp}HP.')
                                    if action_result == 'miss':
                                        action_two = input(
                                            f'What do you do?({special_power_one} / {special_power_two}): ')
                                        if action_two == special_power_one:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 80:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster gets hit! Finish him while you still can!')
                                                action_three = input(
                                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                                if action_three == special_power_one:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 80:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then he strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')

                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it strikes you'
                                                                f' for 15 leaving'
                                                                f' you on {current_hp}HP.')
                                                            print('After it strikes you for the second time you\n'
                                                                  'the monster losses interest in you and leaves you')
                                                elif action_three == special_power_two:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 50:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then it strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')
                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it strikes you'
                                                                f' for 15 leaving you on {current_hp}HP.')
                                                            print(
                                                                'The monster is badly hurt and leaves'
                                                                ' you be... for now.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then he strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')

                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                                        f' you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                                        elif action_two == special_power_two:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 50:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster falls to the ground defeated')
                                                print('You may proceed.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you'
                                                        f' for 15 leaving you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                        elif action == special_power_two:
                            dice_roll = random.randint(1, 101)
                            if dice_roll <= 50:
                                action_result = 'hit'
                            else:
                                action_result = 'miss'

                            if action_result == 'hit':
                                print('The monster falls to the ground defeated')
                                print('You may proceed.')
                            elif action_result == 'miss':
                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                if damage_done < 0:
                                    damage_done = 0
                                current_hp -= damage_done
                                if current_hp <= 0:
                                    game_over = True
                                    print(f'You miss the {monster} and then it strikes you for 15 killing you\n'
                                          f' and ending your journey. GAME OVER!')
                                else:
                                    print(
                                        f'You miss the {monster} and then it strikes'
                                        f' you for 15 leaving you on {current_hp}HP.')
                                    if action_result == 'miss':
                                        action_two = input(
                                            f'What do you do?({special_power_one} / {special_power_two}): ')
                                        if action_two == special_power_one:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 80:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster gets hit! Finish him while you still can!')
                                                action_two = input(
                                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                                if action_two == special_power_one:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 80:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then he strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')

                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it '
                                                                f'strikes you for 15 leaving'
                                                                f' you on {current_hp}HP.')
                                                            print('After it strikes you for the second time you\n'
                                                                  'the monster losses interest in you and leaves you')
                                                elif action_two == special_power_two:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 50:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then it strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')
                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it strikes you'
                                                                f' for 15 leaving you on {current_hp}HP.')
                                                            print(
                                                                'The monster is badly hurt and'
                                                                ' leaves you be... for now.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                                        f' you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                                        elif action_two == special_power_two:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 50:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster falls to the ground defeated')
                                                print('You may proceed.')

                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you'
                                                        f' for 15 leaving you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                    else:
                        print(f'You enter through the door and see that the room is empty')
                        print('You may proceed.')

                if movement == 'Left':
                    encounter_chance = random.randint(1, 101)
                    if encounter_chance <= 10:
                        event = input(
                            f'As you enter the {movement} door you stumble upon a treasure room'
                            f' containing a big chest.\n'
                            f' What do you do?(Open or Skip): ')
                        if event == 'Open':
                            event_chance = random.randint(1, 101)
                            if event_chance <= 10:
                                treasure_result = 'You find nothing in the chest.'
                                print(treasure_result)
                            elif event_chance <= rng_chest:
                                max_hp += 2
                                current_hp += 2
                                power += 2
                                block += 2
                                # charisma += 2
                                print('You find an artifact which grants you all stats up (+ 2)')
                                print(
                                    f'Your stats now are as it follows: HP = {current_hp} / {max_hp}, Power = {power}, '
                                    f'Block = {block},')
                            # f' Charisma = {charisma}')
                            else:
                                print('You find an artifact which is cursed! It takes away stats from you (- 2)')
                                max_hp -= 2
                                current_hp -= 2
                                power -= 2
                                block -= 2
                                if current_hp <= 0:
                                    game_over = True
                                # charisma -= 2
                                print(f'Your stats now are as it follows: HP = {current_hp} / {max_hp},'
                                      f' Power = {power},'
                                      f' Block = {block}, ')
                        # f'Charisma = {charisma}')
                        elif event == 'Skip':
                            pass
                    elif encounter_chance <= rng:
                        action = input(f'As you enter the {movement} door you stumble upon an {monster}.\n'
                                       f' His total hp is 15.\n'
                                       f' What do you do?({special_power_one} / {special_power_two}): ')
                        if action == special_power_one:
                            dice_roll = random.randint(1, 101)
                            if dice_roll <= 80:
                                action_result = 'hit'
                            else:
                                action_result = 'miss'
                            if action_result == 'hit':
                                print('The monster gets hit! Finish him while you still can!')
                                action_two = input(
                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                if action_two == special_power_one:
                                    dice_roll = random.randint(1, 101)
                                    if dice_roll <= 80:
                                        action_result = 'hit'
                                    else:
                                        action_result = 'miss'
                                    if action_result == 'hit':
                                        print('The monster falls to the ground defeated')
                                        print('You may proceed.')
                                    elif action_result == 'miss':
                                        damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                        if damage_done < 0:
                                            damage_done = 0
                                        current_hp -= damage_done
                                        if current_hp <= 0:
                                            game_over = True
                                            print(
                                                f'You miss the {monster} and then he strikes'
                                                f' you for 15 killing you\n'
                                                f' and ending your journey. GAME OVER!')

                                        else:
                                            print(
                                                f'You miss the {monster} and then it strikes you for 15 leaving'
                                                f' you on {current_hp}HP.')
                                            print('The monster is badly hurt and leaves you be... for now.')
                                elif action_two == special_power_two:
                                    dice_roll = random.randint(1, 101)
                                    if dice_roll <= 50:
                                        action_result = 'hit'
                                    else:
                                        action_result = 'miss'
                                    if action_result == 'hit':
                                        print('The monster falls to the ground defeated')
                                        print('You may proceed.')
                                    elif action_result == 'miss':
                                        damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                        if damage_done < 0:
                                            damage_done = 0
                                        current_hp -= damage_done
                                        if current_hp <= 0:
                                            game_over = True
                                            print(
                                                f'You miss the {monster} and then it strikes'
                                                f' you for 15 killing you\n'
                                                f' and ending your journey. GAME OVER!')
                                        else:
                                            print(
                                                f'You miss the {monster} and then it strikes you'
                                                f' for 15 leaving you on {current_hp}HP.')
                                            print('The monster is badly hurt and leaves you be... for now.')
                            elif action_result == 'miss':
                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                if damage_done < 0:
                                    damage_done = 0
                                current_hp -= damage_done
                                if current_hp <= 0:
                                    print(f'You miss the {monster} and then it strikes you for 15 killing you\n'
                                          f' and ending your journey. GAME OVER!')
                                else:
                                    print(
                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                        f' you on {current_hp}HP.')
                                    if action_result == 'miss':
                                        action_two = input(
                                            f'What do you do?({special_power_one} / {special_power_two}): ')
                                        if action_two == special_power_one:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 80:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster gets hit! Finish him while you still can!')
                                                action_three = input(
                                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                                if action_three == special_power_one:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 80:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then he strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')

                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it'
                                                                f' strikes you for 15 leaving'
                                                                f' you on {current_hp}HP.')
                                                            print('After it strikes you for the second time you\n'
                                                                  'the monster losses interest in you and leaves you')
                                                elif action_three == special_power_two:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 50:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then it strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')
                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it strikes you'
                                                                f' for 15 leaving you on {current_hp}HP.')
                                                            print(
                                                                'The monster is badly hurt and'
                                                                ' leaves you be... for now.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then he strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')

                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                                        f' you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                                        elif action_two == special_power_two:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 50:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster falls to the ground defeated')
                                                print('You may proceed.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you'
                                                        f' for 15 leaving you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                        elif action == special_power_two:
                            dice_roll = random.randint(1, 101)
                            if dice_roll <= 50:
                                action_result = 'hit'
                            else:
                                action_result = 'miss'

                            if action_result == 'hit':
                                print('The monster falls to the ground defeated')
                                print('You may proceed.')
                            elif action_result == 'miss':
                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                if damage_done < 0:
                                    damage_done = 0
                                current_hp -= damage_done
                                if current_hp <= 0:
                                    game_over = True
                                    print(f'You miss the {monster} and then it strikes you for 15 killing you\n'
                                          f' and ending your journey. GAME OVER!')
                                else:
                                    print(
                                        f'You miss the {monster} and then it strikes'
                                        f' you for 15 leaving you on {current_hp}HP.')
                                    if action_result == 'miss':
                                        action_two = input(
                                            f'What do you do?({special_power_one} / {special_power_two}): ')
                                        if action_two == special_power_one:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 80:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster gets hit! Finish him while you still can!')
                                                action_two = input(
                                                    f'What do you do?({special_power_one} / {special_power_two}): ')
                                                if action_two == special_power_one:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 80:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then he strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')

                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then'
                                                                f' it strikes you for 15 leaving'
                                                                f' you on {current_hp}HP.')
                                                            print('After it strikes you for the second time you\n'
                                                                  'the monster losses interest in you and leaves you')
                                                elif action_two == special_power_two:
                                                    dice_roll = random.randint(1, 101)
                                                    if dice_roll <= 50:
                                                        action_result = 'hit'
                                                    else:
                                                        action_result = 'miss'
                                                    if action_result == 'hit':
                                                        print('The monster falls to the ground defeated')
                                                        print('You may proceed.')
                                                    elif action_result == 'miss':
                                                        damage_done = random.randint(1, 16) - random.randint(1,
                                                                                                             block + 1)
                                                        if damage_done < 0:
                                                            damage_done = 0
                                                        current_hp -= damage_done
                                                        if current_hp <= 0:
                                                            game_over = True
                                                            print(
                                                                f'You miss the {monster} and then it strikes'
                                                                f' you for 15 killing you\n'
                                                                f' and ending your journey. GAME OVER!')
                                                        else:
                                                            print(
                                                                f'You miss the {monster} and then it strikes you'
                                                                f' for 15 leaving you on {current_hp}HP.')
                                                            print(
                                                                'The monster is badly hurt and'
                                                                ' leaves you be... for now.')
                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you for 15 leaving'
                                                        f' you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                                        elif action_two == special_power_two:
                                            dice_roll = random.randint(1, 101)
                                            if dice_roll <= 50:
                                                action_result = 'hit'
                                            else:
                                                action_result = 'miss'
                                            if action_result == 'hit':
                                                print('The monster falls to the ground defeated')
                                                print('You may proceed.')

                                            elif action_result == 'miss':
                                                damage_done = random.randint(1, 16) - random.randint(1, block + 1)
                                                if damage_done < 0:
                                                    damage_done = 0
                                                current_hp -= damage_done
                                                if current_hp <= 0:
                                                    game_over = True
                                                    print(
                                                        f'You miss the {monster} and then it strikes'
                                                        f' you for 15 killing you\n'
                                                        f' and ending your journey. GAME OVER!')
                                                else:
                                                    print(
                                                        f'You miss the {monster} and then it strikes you'
                                                        f' for 15 leaving you on {current_hp}HP.')
                                                    print('After it strikes you for the second time you\n'
                                                          'the monster losses interest in you and leaves you')
                    else:
                        monster = 'Empty room'
                        print(f'You enter through the door and see that the room is empty')
                        print('You may proceed.')

    else:
        print(f'You live your life peacefully as you age with your wife and kids. After becoming'
              f' {random.randint(65, 101)} years old you\n'
              f' die of old age. How boring...')
        pass

print(f'Congratulations you have gone through {rooms_cleared} rooms! Your reward is a cookie.')
