import Del1

def test_batteri():
    batteri1 = Del1.batteri("B1", 100)
    
    batteri1.ladOpp(30)
    print(f"Energinivå: {batteri1.visEnerginivå()}")
    
    batteri1.brukEnergi(20)
    print(f"Energinivå: {batteri1.visEnerginivå()}")
    
    # batteri1.brukEnergi(20)
    # print(f"Energinivå: {batteri1.visEnerginivå()}")
    
    try:
        batteri1.brukEnergi(50)
    except ValueError:
        print("Feil fanget")
        
    try: 
        batteri1.ladOpp(-10)
    except ValueError:
        print("Feil fanget")
        
    batteri1.ladOpp(1000)
    
test_batteri()