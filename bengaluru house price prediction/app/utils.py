import numpy as np


def predict_price(location, sqft, bath, bhk, model, x_columns):
    """
    Predict price based on inputs and one-hot encoded columns.
    """
    # Ensure x_columns is a numpy array
    x_columns = np.array(x_columns)

    # Create input array
    x = np.zeros(len(x_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Only set location if it exists in columns
    if location in x_columns:
        loc_index = np.where(x_columns == location)[0][0]
        x[loc_index] = 1
    # else leave location as all zeros (for 'other' locations)

    # Ensure input is 2D for sklearn
    x = np.atleast_2d(x)

    return model.predict(x)[0]
