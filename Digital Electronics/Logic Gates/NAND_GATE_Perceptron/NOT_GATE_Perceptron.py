# NOT Gate Using Perceptron

# a y 
# 0 1
# 1 0

def activation(sum,threshold):
    if sum == threshold:
        return 1
    else:
        return 0

def perceptron(not_input):
    a = [0,1]
    y = [1,0] # Actual Output
    w = 0
    threshold = 0
    learning_rate = 0.5
    i=0
    print("NOT Gate Perceptron Training : ")
    # print("#####################")
    # print("-----------------")
    while i<2:
        summation = a[i]*w
        o = activation(summation,threshold)
        # print("Input : " + str(a[i]))
        # print("Weights : " + str(w))
        # print("summation : "+str(summation) + " threshold : "+str(threshold) )
        # print("Actual Output : "+str(y[i])+" Predicated Output : "+str(o))
        if(o!=y[i]):
            # w = w + learning_rate(actual_output - predicated_output)*input
            # print("_______\nUpdating Weights")
            w = w + learning_rate*(y[i]-o)*a[i]
            # print("Updated Weights : " + str(w))
            i = -1
            # print("\nWeights Updated Training Again : ")
            # print("###################################")
        i=i+1
        # print("------------------")
    # Prediction Part
    summation = not_input * w
    return activation(summation,threshold)

