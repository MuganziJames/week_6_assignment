# AgriSense AI Data Flow Diagram Generator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
import numpy as np

# Create the data flow diagram
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Define colors
sensor_color = '#4CAF50'  # Green
edge_color = '#2196F3'    # Blue
cloud_color = '#FF9800'   # Orange
ai_color = '#9C27B0'      # Purple
output_color = '#F44336'  # Red

# Title
ax.text(8, 11.5, 'AgriSense AI: Smart Agriculture Data Flow', 
        fontsize=20, fontweight='bold', ha='center')

# Layer 1: Field Sensors
ax.text(2, 10.5, 'FIELD SENSORS', fontsize=14, fontweight='bold', ha='center')

# Soil sensors
soil_box = FancyBboxPatch((0.5, 9), 1.5, 1, boxstyle="round,pad=0.1", 
                         facecolor=sensor_color, alpha=0.7)
ax.add_patch(soil_box)
ax.text(1.25, 9.5, 'Soil\nSensors', ha='center', va='center', fontsize=10, fontweight='bold')

# Weather sensors
weather_box = FancyBboxPatch((2.5, 9), 1.5, 1, boxstyle="round,pad=0.1", 
                           facecolor=sensor_color, alpha=0.7)
ax.add_patch(weather_box)
ax.text(3.25, 9.5, 'Weather\nSensors', ha='center', va='center', fontsize=10, fontweight='bold')

# Plant sensors
plant_box = FancyBboxPatch((0.5, 7.5), 1.5, 1, boxstyle="round,pad=0.1", 
                         facecolor=sensor_color, alpha=0.7)
ax.add_patch(plant_box)
ax.text(1.25, 8, 'Plant Health\nSensors', ha='center', va='center', fontsize=10, fontweight='bold')

# Infrastructure sensors
infra_box = FancyBboxPatch((2.5, 7.5), 1.5, 1, boxstyle="round,pad=0.1", 
                         facecolor=sensor_color, alpha=0.7)
ax.add_patch(infra_box)
ax.text(3.25, 8, 'Infrastructure\nSensors', ha='center', va='center', fontsize=10, fontweight='bold')

# Layer 2: Edge Computing
ax.text(6, 10.5, 'EDGE COMPUTING', fontsize=14, fontweight='bold', ha='center')

edge_box = FancyBboxPatch((5, 8.5), 2, 1.5, boxstyle="round,pad=0.1", 
                        facecolor=edge_color, alpha=0.7)
ax.add_patch(edge_box)
ax.text(6, 9.25, 'Raspberry Pi\nGateway', ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Edge processing details
ax.text(6, 7.8, '• Data Aggregation\n• Local Processing\n• Anomaly Detection', 
        ha='center', va='top', fontsize=9)

# Layer 3: Connectivity
ax.text(9.5, 10.5, 'CONNECTIVITY', fontsize=14, fontweight='bold', ha='center')

lorawan_box = FancyBboxPatch((8.5, 9), 1.5, 1, boxstyle="round,pad=0.1", 
                           facecolor='#607D8B', alpha=0.7)
ax.add_patch(lorawan_box)
ax.text(9.25, 9.5, 'LoRaWAN\nGateway', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

cellular_box = FancyBboxPatch((10.5, 9), 1.5, 1, boxstyle="round,pad=0.1", 
                            facecolor='#607D8B', alpha=0.7)
ax.add_patch(cellular_box)
ax.text(11.25, 9.5, 'Cellular\nBackup', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Layer 4: Cloud Platform
ax.text(13.5, 10.5, 'CLOUD PLATFORM', fontsize=14, fontweight='bold', ha='center')

cloud_box = FancyBboxPatch((12.5, 8.5), 2, 1.5, boxstyle="round,pad=0.1", 
                         facecolor=cloud_color, alpha=0.7)
ax.add_patch(cloud_box)
ax.text(13.5, 9.25, 'Data Storage\n& Processing', ha='center', va='center', fontsize=11, fontweight='bold', color='white')

# Cloud details
ax.text(13.5, 7.8, '• Time-series DB\n• Apache Kafka\n• Data Validation', 
        ha='center', va='top', fontsize=9)

# Layer 5: AI Processing
ax.text(8, 6.5, 'AI PROCESSING ENGINE', fontsize=14, fontweight='bold', ha='center')

# Crop yield model
yield_box = FancyBboxPatch((6, 5), 2, 1, boxstyle="round,pad=0.1", 
                         facecolor=ai_color, alpha=0.7)
ax.add_patch(yield_box)
ax.text(7, 5.5, 'Crop Yield\nPrediction', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Irrigation model
irrigation_box = FancyBboxPatch((8.5, 5), 2, 1, boxstyle="round,pad=0.1", 
                              facecolor=ai_color, alpha=0.7)
ax.add_patch(irrigation_box)
ax.text(9.5, 5.5, 'Irrigation\nOptimization', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Disease detection
disease_box = FancyBboxPatch((11, 5), 2, 1, boxstyle="round,pad=0.1", 
                           facecolor=ai_color, alpha=0.7)
ax.add_patch(disease_box)
ax.text(12, 5.5, 'Disease\nDetection', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Layer 6: Outputs
ax.text(8, 3.5, 'FARMER INTERFACE & AUTOMATION', fontsize=14, fontweight='bold', ha='center')

# Dashboard
dashboard_box = FancyBboxPatch((5.5, 2), 2, 1, boxstyle="round,pad=0.1", 
                             facecolor=output_color, alpha=0.7)
ax.add_patch(dashboard_box)
ax.text(6.5, 2.5, 'Web/Mobile\nDashboard', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Alerts
alerts_box = FancyBboxPatch((8, 2), 2, 1, boxstyle="round,pad=0.1", 
                          facecolor=output_color, alpha=0.7)
ax.add_patch(alerts_box)
ax.text(9, 2.5, 'Smart Alerts\n& Notifications', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Automation
automation_box = FancyBboxPatch((10.5, 2), 2, 1, boxstyle="round,pad=0.1", 
                              facecolor=output_color, alpha=0.7)
ax.add_patch(automation_box)
ax.text(11.5, 2.5, 'Automated\nIrrigation', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Data flow arrows
arrow_props = dict(arrowstyle='->', lw=2, color='#333333')

# Sensors to Edge
ax.annotate('', xy=(5, 9.2), xytext=(4, 9.2), arrowprops=arrow_props)
ax.annotate('', xy=(5, 8.2), xytext=(4, 8.2), arrowprops=arrow_props)

# Edge to Connectivity
ax.annotate('', xy=(8.5, 9.2), xytext=(7, 9.2), arrowprops=arrow_props)

# Connectivity to Cloud
ax.annotate('', xy=(12.5, 9.2), xytext=(11, 9.2), arrowprops=arrow_props)

# Cloud to AI
ax.annotate('', xy=(7, 6), xytext=(13, 8.5), arrowprops=arrow_props)
ax.annotate('', xy=(9.5, 6), xytext=(13.2, 8.5), arrowprops=arrow_props)
ax.annotate('', xy=(12, 6), xytext=(13.5, 8.5), arrowprops=arrow_props)

# AI to Outputs
ax.annotate('', xy=(6.5, 3), xytext=(7, 5), arrowprops=arrow_props)
ax.annotate('', xy=(9, 3), xytext=(9.5, 5), arrowprops=arrow_props)
ax.annotate('', xy=(11.5, 3), xytext=(12, 5), arrowprops=arrow_props)

# External data sources
external_box = FancyBboxPatch((13, 6.5), 2.5, 1, boxstyle="round,pad=0.1", 
                            facecolor='#795548', alpha=0.7)
ax.add_patch(external_box)
ax.text(14.25, 7, 'External Data\n(Weather, Market)', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# External to AI
ax.annotate('', xy=(11, 5.8), xytext=(13, 6.8), arrowprops=arrow_props)

# Add data types annotations
ax.text(4.5, 9.8, 'Moisture, pH, NPK\nTemperature, EC', ha='center', va='center', fontsize=8, 
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(4.5, 7.8, 'Chlorophyll, Growth\nWater Level, Power', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(6, 7, 'Aggregated\nSensor Data', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(9.75, 8, 'Compressed\nData Packets', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(13.5, 7, 'Time-series\nData Storage', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(8.5, 4, 'ML Predictions\n& Recommendations', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

ax.text(8.5, 1.2, 'Actionable Insights\nfor Farmers', ha='center', va='center', fontsize=8,
        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add legend
legend_x = 1
legend_y = 1.5
ax.text(legend_x, legend_y + 0.5, 'LEGEND:', fontsize=12, fontweight='bold')

legend_items = [
    (sensor_color, 'IoT Sensors'),
    (edge_color, 'Edge Computing'),
    (cloud_color, 'Cloud Platform'),
    (ai_color, 'AI Models'),
    (output_color, 'User Interface')
]

for i, (color, label) in enumerate(legend_items):
    y_pos = legend_y - i * 0.3
    legend_box = Rectangle((legend_x, y_pos), 0.3, 0.2, facecolor=color, alpha=0.7)
    ax.add_patch(legend_box)
    ax.text(legend_x + 0.4, y_pos + 0.1, label, fontsize=10, va='center')

plt.tight_layout()
plt.savefig('agrisense_data_flow_diagram.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Data Flow Diagram Generated: agrisense_data_flow_diagram.png")
print("\n📊 Diagram Components:")
print("   🌱 IoT Sensors: Collect environmental and crop data")
print("   💻 Edge Computing: Local processing and aggregation")
print("   📡 Connectivity: LoRaWAN and cellular communication")
print("   ☁️ Cloud Platform: Data storage and processing")
print("   🤖 AI Models: Machine learning for predictions")
print("   📱 User Interface: Dashboards and automation control")
