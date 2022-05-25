rf_parameters = {
  'regressor__max_depth': [None, 4, 5, 6, 8, 10],
  'regressor__criterion': ['mse', 'mae', 'poisson'],
  'regressor__n_estimators': [10, 100, 500],
  'regressor__max_features': ['auto', 'sqrt', 'log2']
}
