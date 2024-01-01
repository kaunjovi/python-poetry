import random
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def generate_training_data(count_of_training_data, data_dump_file=""):

    training_data = []

    for i in range(count_of_training_data):
        addend1 = random.randint(0, 100)
        addend2 = random.randint(0, 100)
        sum = addend1 + addend2
        single_training_data = [addend1, addend2, sum]
        training_data.append(single_training_data)

    df = pd.DataFrame(training_data, columns=["addend1", "addend2", "output"])

    print(f"{df.head()}")

    if len(data_dump_file) > 0:
        df.to_csv(data_dump_file, index=False)

    return df


def generate_trained_ml_model(training_data_df):

    Y = training_data_df.output
    print("Prediction Target")
    print(f"{Y.head()}")

    X = training_data_df[["addend1", "addend2"]]

    addition_model = DecisionTreeRegressor(random_state=1)
    addition_model.fit(X, Y)

    return addition_model


def predict(addition_model, addend1, addend2):
    data = [[addend1, addend2]]
    column_names = ["addend1", "addend2"]
    X = pd.DataFrame(data, columns=column_names)
    return addition_model.predict(X)


if __name__ == "__main__":

    training_data_df = generate_training_data(
        10000, "learnml0010-add/training_data_additions.csv"
    )
    addition_model = generate_trained_ml_model(training_data_df)

    # addend1, add  end2 = input("Enter x y :").split()
    # output = int(addend1) + int(addend2)

    test_data_df = pd.read_csv("learnml0010-add/predict_additions.csv")

    for ind in test_data_df.index:
        addend1 = test_data_df["addend1"][ind]
        addend2 = test_data_df["addend2"][ind]

        predicted_output = predict(addition_model, addend1, addend2)
        output = addend1 + addend2
        print(f"{addend1} + {addend2} = {output} | {predicted_output} (predicted)")
        assert (
            output == predicted_output
        ), f"Output {output} is NOT the same as ML model output {predicted_output}."
