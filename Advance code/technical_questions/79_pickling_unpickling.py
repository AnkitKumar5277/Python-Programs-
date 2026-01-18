import pickle

# Sample data (a dictionary)
data = {"name": "Alice", "age": 25, "city": "New York"}

# Pickling: Saving the object to a file
with open("data.pkl", "wb") as file:  # 'wb' means write binary
    pickle.dump(data, file)
    print("Data pickled successfully!")

# Unpickling: Loading the object from the file
with open("data.pkl", "rb") as file:  # 'rb' means read binary
    loaded_data = pickle.load(file)
    print("Unpickled data:", loaded_data)

