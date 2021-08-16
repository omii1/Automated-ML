import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler

class preprocessing:

    def __init__(self, file_object, logger_object):
        self.file_object = file_object
        self.logger_object = logger_object

 def removeDuplicates(self,data):
        duplicate_count=data.duplicated().sum()
        if duplicate_count>0:
            data.drop_duplicates(inplace=True)
        return data


def impute_missing_values(self, data):
    self.logger_object.log(self.file_object, 'Entered the impute_missing_values method of the Preprocessor class')
    self.data = data
    try:
        imputer = KNNImputer(n_neighbors=3, weights='uniform', missing_values=np.nan)
        self.new_array = imputer.fit_transform(self.data)  # impute the missing values
        # convert the nd-array returned in the step above to a Dataframe
        self.new_data = pd.DataFrame(data=(self.new_array), columns=self.data.columns)
        self.logger_object.log(self.file_object,
                               'Imputing missing values Successful. Exited the impute_missing_values method of the Preprocessor class')
        return self.new_data
    except Exception as e:
        self.logger_object.log(self.file_object,
                               'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(
                                   e))
        self.logger_object.log(self.file_object,
                               'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
        raise Exception()
