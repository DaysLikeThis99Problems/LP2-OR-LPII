import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

class MedicalExpertSystem:
    def __init__(self, csv_file):
        self.knowledge_base = {}
        self.symptoms_set = set()

        df = pd.read_csv(csv_file)
        symptom_cols = [col for col in df.columns if col.startswith("Symptom")]

        for _, row in df.iterrows():
            disease = row['Disease']
            symptoms = [str(row[col]).strip().lower() for col in symptom_cols if pd.notna(row[col])]
            self.knowledge_base[disease] = symptoms
            self.symptoms_set.update(symptoms)

        self.symptoms_list = sorted(self.symptoms_set)


    def diagnose(self, user_symptoms):
        if not user_symptoms:
            return ["No symptoms selected. Please select at least one symptom to diagnose."]

        diagnoses = []
        partial_matches = []
        for disease, symptoms in self.knowledge_base.items():
            matching_symptoms = [s for s in symptoms if s in user_symptoms]
            match_ratio = len(matching_symptoms) / len(symptoms)
            if match_ratio >= 0.4:
                diagnoses.append({
                    "disease": disease,
                    "matched": matching_symptoms,
                    "confidence": round(match_ratio * 100, 2)
                })
            elif matching_symptoms:
                partial_matches.append({
                    "disease": disease,
                    "matched": matching_symptoms,
                    "confidence": round(match_ratio * 100, 2)
                })

        if not diagnoses:
            partial_info = "\nPartial matches (not enough symptoms):"
            for pm in sorted(partial_matches, key=lambda x: x["confidence"], reverse=True):
                partial_info += f"\n- {pm['disease']} (Confidence: {pm['confidence']}%, Symptoms matched: {', '.join(pm['matched'])})"
            return ["No clear diagnosis based on selected symptoms. Please consult a healthcare professional." + partial_info]

        diagnoses.sort(key=lambda x: x["confidence"], reverse=True)
        return [f"Possible {d['disease']} (Confidence: {d['confidence']}%, Symptoms matched: {', '.join(d['matched'])})" for d in diagnoses]

# Update the path if needed
csv_path = "datasets/medical_data.csv"
expert_system = MedicalExpertSystem(csv_path)

# UI setup
symptom_checkboxes = [widgets.Checkbox(value=False, description=symptom, indent=False) for symptom in expert_system.symptoms_list]
submit_button = widgets.Button(description="Diagnose", button_style="success")
clear_button = widgets.Button(description="Clear", button_style="warning")
output = widgets.Output()

checkbox_grid = widgets.GridBox(symptom_checkboxes, layout=widgets.Layout(grid_template_columns="repeat(3, 33%)"))
button_box = widgets.HBox([submit_button, clear_button])

def on_submit_clicked(b):
    with output:
        clear_output()
        selected = [cb.description for cb in symptom_checkboxes if cb.value]
        print("Medical Diagnosis Expert System")
        print("Selected symptoms:", ", ".join(selected) if selected else "None")
        results = expert_system.diagnose(selected)
        print("\nDiagnosis Results:")
        for r in results:
            print("-", r)
        print("\nNote: Always consult a healthcare professional.")

def on_clear_clicked(b):
    for cb in symptom_checkboxes:
        cb.value = False
    with output:
        clear_output()

submit_button.on_click(on_submit_clicked)
clear_button.on_click(on_clear_clicked)

# Display
print("Select symptoms for diagnosis:")
display(checkbox_grid, button_box, output)

