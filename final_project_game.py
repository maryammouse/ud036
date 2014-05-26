import final_project
import time

first = final_project.Step("""
                           You are in a cave.
                           It's dark and cold, and you
                           are tired. But you can hear
                           wolves howling behind you.
                           Surely they won't see you
                           in the dark?
                           What do you do?""",
                           "Rest",
                           "Keep Walking", "neutral")

rest = final_project.Step("""
                  You find a corner and you bed down,
                  sighing with relief. Your feet really
                  were aching a lot.
                  Your eyes are drifting shut already.
                  Then you feel something brush past you in
                  the dark and cut into you. Everything goes dark...
                  """,
                    'n/a', 'n/a', "Lose")

keep_walking = final_project.Step("""
                          You keep walking, though your body
                          begs for rest. After stumbling through
                          the caves for a few more hours, you see
                          a beautiful light - the exit! It's daylight
                          now and you can see your home village from
                          here. Finally! After all you saw, you
                          didn't think you'd make it back...but you did!
                          """,
                            'n/a', 'n/a', "Win")


print(first.dialogue)
print(first.option1)
print(first.option2)

first_selection = raw_input(" > ")


if first_selection == first.option1:
    print(rest.dialogue)
    time.sleep(5)
    rest.win_or_lose()

elif first_selection == first.option2:
    print(keep_walking.dialogue)
    time.sleep(5)
    keep_walking.win_or_lose()
