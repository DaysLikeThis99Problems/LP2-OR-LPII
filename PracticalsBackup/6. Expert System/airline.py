import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

class AirlineExpertSystemFromCSV:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.actions = self.df['Action'].unique()
        self.conditions_list = sorted(self.df['Condition'].unique())

    def evaluate(self, selected_conditions):
        if not selected_conditions:
            return ["No conditions selected. Please select at least one to evaluate scheduling."]

        recommendations = []
        partial_matches = []

        for action in self.actions:
            action_conditions = self.df[self.df['Action'] == action]['Condition'].tolist()
            matched = [cond for cond in action_conditions if cond in selected_conditions]
            match_ratio = len(matched) / len(set(action_conditions))
            if match_ratio >= 0.4:
                recommendations.append({
                    "action": action,
                    "matched": matched,
                    "confidence": round(match_ratio * 100, 2)
                })
            elif matched:
                partial_matches.append({
                    "action": action,
                    "matched": matched,
                    "confidence": round(match_ratio * 100, 2)
                })

        if not recommendations:
            partial_info = "\nPartial matches:"
            for pm in sorted(partial_matches, key=lambda x: x["confidence"], reverse=True):
                partial_info += f"\n- {pm['action']} (Confidence: {pm['confidence']}%, Conditions matched: {', '.join(pm['matched'])})"
            return ["No strong scheduling recommendation." + partial_info]

        recommendations.sort(key=lambda x: x["confidence"], reverse=True)
        return [f"Suggested Action: {r['action']} (Confidence: {r['confidence']}%, Conditions matched: {', '.join(r['matched'])})" for r in recommendations]

# Instantiate system with your CSV file
expert_system = AirlineExpertSystemFromCSV("airline_scheduling_data.csv")

# Widgets
condition_checkboxes = [widgets.Checkbox(value=False, description=cond, indent=False) for cond in expert_system.conditions_list]
submit_button = widgets.Button(description="Evaluate Schedule", button_style="info")
clear_button = widgets.Button(description="Clear", button_style="warning")
output = widgets.Output()

checkbox_grid = widgets.GridBox(
    condition_checkboxes,
    layout=widgets.Layout(grid_template_columns="repeat(3, 33%)")
)
button_box = widgets.HBox([submit_button, clear_button])

def on_submit_clicked(b):
    with output:
        clear_output()
        selected_conditions = [cb.description for cb in condition_checkboxes if cb.value]
        print("Airline Scheduling & Cargo Evaluation System")
        print("Selected conditions:", ", ".join(selected_conditions) if selected_conditions else "None")
        results = expert_system.evaluate(selected_conditions)
        print("\nEvaluation Results:")
        for res in results:
            print(f"- {res}")
        print("\nNote: This tool is for simulation. Always confirm with airline operations control.")

def on_clear_clicked(b):
    for cb in condition_checkboxes:
        cb.value = False
    with output:
        clear_output()

submit_button.on_click(on_submit_clicked)
clear_button.on_click(on_clear_clicked)

# Display UI
print("Select current conditions affecting scheduling:")
display(checkbox_grid, button_box, output)
