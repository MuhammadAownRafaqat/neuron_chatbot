# # our neuron's knowledge
# weight = 0.7
# bias = -0.1

# # 1. Get input from the user
# user_text = input("Say something to the bot: ").lower()

# # 2. Convert text to a number (The "Input")
# if "hello" in user_text:
#     user_input = 1
# else:
#     user_input = 0

# # 3. The Math (The "Neuron")
# score = (user_input * weight) + bias

# # 4. The Decision (The "Activation")
# if score > 0:
#     print("Bot: Hi There")
# else:
#     print("Bot: ...")

# Starting values (deliberately low so it has to learn)
weight = 0.1
bias = -0.2
learning_rate = 0.1
target = 1 # We want the bot to say "Hi!" when input is 1

print("--- Training Started ---")

for epoch in range(10):
    user_input = 1 # Simulating the user saying "hello"

    # 1. Guess
    score = (user_input * weight) + bias
    prediction = 1 if score > 0 else 0

    # 2. Calculate Error
    error = target - prediction

    # 3. Adjust weight
    weight = weight + (user_input * error * learning_rate)

    print(f"Epoch {epoch+1}: Weight is now {weight: .2f}, Score: {score: .2f}")
