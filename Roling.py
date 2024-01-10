from dice_storage import d4, d6, d8, d10, d12, d20

class Rolling:


    def __init__(self):
        result4 = 0
        result3 = 0
        result2 = 0
        result1 = 0

        self.dices = [d4, d6, d8, d10, d12, d20]
        self.dices_string = ["d4", "d6", "d8", "d10", "d12", "d20"]
        while True:

            print("which dice do you wish to roll?",
                "\n(d20, d12, d8, d6, d4) d0 to exit")  

            
            option = input("")
            

            if option == "d0":
                break

            elif option in ["d4", "d6", "d8", "d10", "d12", "d20"]:
                try:
                    times_rolled_option = int(input("roll how many times? "))

                    total_result = 0
                    i = 0
                    for dice in self.dices_string:
                        if option == dice:
                            for times in range(0, times_rolled_option):
                                chosen_dice = self.dices[i]
                                chosen_dice.roll()
                                total_result += chosen_dice.result

                                if chosen_dice.result == 4:
                                    result4 += 1
                                elif chosen_dice.result == 3:
                                    result3 += 1
                                elif chosen_dice.result == 2:
                                    result2 += 1
                                elif chosen_dice.result == 1:
                                    result1 += 1        



                            print("total result", total_result)   
                            print("times 4 appeared", times_rolled_option, result4)
                            print("times 3 appeared", result3)
                            print("times 2 appeared", result2)
                            print("times 1 appeared", result1) 

                        i += 1     
                except ValueError:
                    print("please chose a number")

            else:
                print("please chose one of the options avaliable")        


 
        
