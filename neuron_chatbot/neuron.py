# 1. Get input from the user
user_text = input("Say something to the bot: ").lower()

# Starting values (deliberately low so it has to learn)
w_hello = 0.6
w_bye = 0.8
bias = -0.2
learning_rate = 0.1
target = 1 # We want the bot to say "Hi!" when input is 1


# 2. Convert text to a number (The "Input")
if "hello" in user_text:
    user_hello = 1
else:
    user_hello = 0

if "bye" in user_text:
    user_bye = 1
else:
    user_bye = 0

training_data = [(1,0,1), (0,1,1), (0,0,0)]
for epoch in range(10):
    for h_in, b_in, goal in training_data:
        # 1. Guess: Use BOTH inputs and BOTH weights
        score = (h_in * w_hello) + (b_in * w_bye) + bias
        prediction = 1 if score > 0 else 0
        
        # 2. Calculate Error
        error = goal - prediction
        
        # 3. Adjust BOTH weights based on their specific inputs
        w_hello = w_hello + (h_in * error * learning_rate)
        w_bye = w_bye + (b_in * error * learning_rate)
        
    print(f"Epoch {epoch+1}: w_hello={w_hello:.2f}, w_bye={w_bye:.2f}")

score =  (user_hello * w_hello) + (user_bye * w_bye) + bias
# 4. The Decision (The "Activation")
if score > 0 and user_hello == 1:
    print("Bot: Hi There")
if score > 0 and user_hello == 0 and "bye" not in user_text:
    print("Bot: ...")
if score > 0 and user_bye == 1:
    print("Bot: See ya")
if score > 0 and user_bye == 0:
    print("Bot: ...")
