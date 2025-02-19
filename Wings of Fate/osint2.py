def main():
    correct_answers = [
        "Istanbul", "Beijing", "Istanbul", "Los Angeles", 
        "Istanbul", "Dubai", "Istanbul", "Miami", "Istanbul"
    ]
    
    user_answers = []
    
    print("This plane was last spotted a few days ago in Tokyo. What was its next destination?")
    
    for i, destination in enumerate(correct_answers):
        user_input = input(f"Next destination after {user_answers[-1] if user_answers else 'Tokyo'}: ").strip().lower()
        user_answers.append(user_input)
    
    if [ans.lower() for ans in user_answers] == [ans.lower() for ans in correct_answers]:
        print("AxP25{b4nd_0f_th3_h4wk5}")
    else:
        print("AxP25{TrY_H4rd3r_N3v3r_G1v3_Up}")
    
if __name__ == "__main__":
    main()
