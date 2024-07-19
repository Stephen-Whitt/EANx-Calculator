# ATA == Atmospheric Absolute
# 1 ATA == 14.7 PSI (i.e, ambient pressure at sea level)
# Every additional 33' adds 1 ATA to the ambient ATA at the surface

PO2 = 1.4 # Constant to ensure calculations are based on the recommended maximum PO2 (partial pressure of O2) [excluding 02_Dose calculations]

# Calculate and print the Maximum Operating Depth for a given EANx blend (decimal PO2)
def MOD():
    print("\n")
    try:
        eanx_Blend = float(input("Which EANx FO\u2082 would you like to use? (e.g., 0.32): "))
        ATA = (PO2 / eanx_Blend) # Calculate ATA for the given EANx blend
        M_O_D = round((ATA - 1) * 33) # Convert ATA to depth in feet
        print(f"The Maximum Operating Depth (MOD) for FO\u2082 {eanx_Blend} is {M_O_D} feet.")
    except ValueError:
        print("\nPlease correct input formatting such that '0.32' corresponds to 32% EANx ...\n")
        MOD()
    
# Calculate and print the optimal gas mixture (decimal PO2) for a given maximum depth
def Best_Mix():
    print("\n")
    try:
        max_Depth = float(input("What is the maximum depth, in feet, for this planned dive? (e.g., 60): "))
        ATA = ((max_Depth / 33) + 1) # Convert max depth to ATA
        Max_FO2 = round((PO2 / ATA), 2) # Calculate the maximum FO2 (Fractional amount of O2) for the given maximum depth
        print(f"The maximum FO\u2082 (Fractional amount of O\u2082) blend for a maximum of {max_Depth} feet is {Max_FO2}")
        if (Max_FO2 < 0.40 and Max_FO2 > 0.21): # Must be < 0.40 (recreational limit) but > 0.21 (air), with 0.32 & 0.36 being the most common
            optimal_Blend = Max_FO2
            print(f"The optimal EANx blend for a maximum of {max_Depth} feet is {optimal_Blend}")
        elif (Max_FO2 > 0.40):
            print(f"A {Max_FO2} EANx blend is outside the recreational EANx limit of 0.40, thus the practical maximum is 0.40.")
        elif (Max_FO2 <= 0.21):
            print(f"The maximum FO\u2082 of {Max_FO2} does not qualify as EANx, therefore standard air (FO\u2082 0.21) is the optimal gas unless qualified to use Trimix.")
        if (max_Depth < 50):
            print("Consider using standard air instead of EANx as you are likely to exhaust your gas supply before reaching your no decompression limit; it may still be a good option to lower necessary surface interval(s).")
    except ValueError:
        print("\nPlease correct input formatting such that '60' corresponds to a planned 60 ft. maximum depth ...\n")
    
# Calculate and print the O2 dose for a given maximum depth
def O2_Dose():
    print("\n")
    try:
        max_Depth = float(input("What is the maximum depth, in feet, for this planned dive? (e.g., 60): "))
        ATA = ((max_Depth / 33) + 1) # Convert max depth to ATA
        FO2 = float(input("Which EANx mixture would you like to use? (e.g., 0.32): "))
        PO2 = round((FO2 * ATA), 2) # Calculate the PO2 for the given EANx blend & maximum depth
        print(f"The PO\u2082 (Partial pressure of O\u2082) at the maximum depth of {max_Depth} feet is {PO2}")
    except ValueError:
        print("\nPlease correct input formatting such that '60' corresponds to a planned 60 ft. maximum depth and '0.32' corresponds to 32% EANx ...\n")
        O2_Dose()
        
def another():
    another_choice = input("\nWould you like to perform another calculation? (y/n): ")
    if (another_choice.lower() == "y"):
        choose()
    else:
        print(
            """
        ____             _                
         /  / _   /  _  (_   _      _ '  _
        (  /)(//)/(_)   / ()/   (/_) //)(/
                                       _/ 
         ___  _             _                                   
         )_  /_) )\ )      / ` _   ) _      ) _  _)_ _   _
        (__ / / (  ( \)   (_. (_( ( (_ (_( ( (_( (_ (_) )           
                     (\                                   
                          __  
                         / _) 
                        /(_)(/
                            / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~      __                        __       __)                                           ~
~  (__/  )         /)           (, )  |  /  /)   ,                /)                    ~
~    / _/_  _ __  (/    _ __       | /| /  (/     _/__/_  _ __   (/_  _  __  _    _  __ ~
~ ) /  (___(/_/_)_/ )__(/_/ (_     |/ |/   / )__(_(__(___(/_/ (_/_) _(/_/ (_(_/__(/_/ (_~
~(_/       .-/                     /  |                                    .-/          ~
~         (_/                                                             (_/           ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
        return

def choose():
    try:
        usr_choice = input(
            "1). Maximum Operating Depth (MOD) \n"
            "2). Optimal Mixture \n"
            "3). O\u2082 Dose\n"
            "4). Quit\n"
            "Which operation would you like to calculate?: "
        )
        if (usr_choice == "1"):
            MOD()
            another()
        elif (usr_choice == "2"):
            Best_Mix()
            another()
        elif (usr_choice == "3"):
            O2_Dose()
            another()
        elif (usr_choice == "4"):
            print(
            """
        ____             _                
         /  / _   /  _  (_   _      _ '  _
        (  /)(//)/(_)   / ()/   (/_) //)(/
                                       _/ 
         ___  _             _                                   
         )_  /_) )\ )      / ` _   ) _      ) _  _)_ _   _
        (__ / / (  ( \)   (_. (_( ( (_ (_( ( (_( (_ (_) )           
                     (\                                   
                          __  
                         / _) 
                        /(_)(/
                            / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~      __                        __       __)                                           ~
~  (__/  )         /)           (, )  |  /  /)   ,                /)                    ~
~    / _/_  _ __  (/    _ __       | /| /  (/     _/__/_  _ __   (/_  _  __  _    _  __ ~
~ ) /  (___(/_/_)_/ )__(/_/ (_     |/ |/   / )__(_(__(___(/_/ (_/_) _(/_/ (_(_/__(/_/ (_~
~(_/       .-/                     /  |                                    .-/          ~
~         (_/                                                             (_/           ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
            return
        else:
            print("\nInvalid option ... try again\n")
            choose()
    except KeyboardInterrupt:
        print(
            """
        ____             _                
         /  / _   /  _  (_   _      _ '  _
        (  /)(//)/(_)   / ()/   (/_) //)(/
                                       _/ 
         ___  _             _                                   
         )_  /_) )\ )      / ` _   ) _      ) _  _)_ _   _
        (__ / / (  ( \)   (_. (_( ( (_ (_( ( (_( (_ (_) )           
                     (\                                   
                          __  
                         / _) 
                        /(_)(/
                            / 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~      __                        __       __)                                           ~
~  (__/  )         /)           (, )  |  /  /)   ,                /)                    ~
~    / _/_  _ __  (/    _ __       | /| /  (/     _/__/_  _ __   (/_  _  __  _    _  __ ~
~ ) /  (___(/_/_)_/ )__(/_/ (_     |/ |/   / )__(_(__(___(/_/ (_/_) _(/_/ (_(_/__(/_/ (_~
~(_/       .-/                     /  |                                    .-/          ~
~         (_/                                                             (_/           ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
        return

print(
        """
                        .   o
                       o   .
                      .   o
                        o
                       o
                    .   o
                    =-:         
                    .::.        
                   .=:==.       
                   .=-==.       
                   .=-==.       
                   .+-==.       
                    --=-     
 ___  _             _                                   
 )_  /_) )\ )      / ` _   ) _      ) _  _)_ _   _
(__ / / (  ( \)   (_. (_( ( (_ (_( ( (_( (_ (_) )           
             (\                                   
        """
    )


choose()