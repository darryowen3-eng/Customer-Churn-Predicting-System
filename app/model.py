import joblib
import shap

package = joblib.load(
"models/CustomerChurn_Predictor.pkl"
)

pipeline = package["model"]
threshold = package["threshold"]

rf_model = pipeline.named_steps["classifier"]

explainer = shap.TreeExplainer(rf_model)
