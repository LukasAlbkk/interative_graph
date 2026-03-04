"""
Grafo Interativo Final para GitHub Pages
Versão otimizada com PyVis e descrições completas
"""
from pyvis.network import Network
import pydot

# Descrições CORRETAS conforme especificação (texto simples para tooltips)
node_descriptions = {
    'mitotic_rate': 'MITOTIC RATE\n\nA measure of how fast cancer cells are dividing and growing.',
    
    'os_months': 'OVERALL SURVIVAL MONTHS\n\nSurvival time, measured in months.',
    
    'os_status': 'OVERALL SURVIVAL STATUS\n\nWhether the patient is dead or alive.',
    
    'stage_at_diagnosis': 'STAGE AT DIAGNOSIS\n\nWhether the tumor is localized or in metastasis.',
    
    'tumor_grade': 'TUMOR GRADE\n\nClassification of tumor differentiation.\nExamples: "low", "high", "intermediate grade"',
    
    'treatment_response': 'TREATMENT RESPONSE\n\nResponse to applied treatment.\nExamples: "partial response", "complete response"',
    
    'treatment': 'TREATMENT\n\nType of treatment applied.\nExamples: Imatinib, Surgery',
    
    'treatment_details': 'TREATMENT DETAILS\n\nIndicates whether there was therapy involving medication.\nExample: "medical therapy"',
    
    'treatment_duration_days': 'TREATMENT DURATION\n\nDuration of treatment measured in days.',
    
    'tumor_site': 'TUMOR SITE\n\nAnatomical location of the tumor.\nIndicates whether there was metastasis.',
    
    'primary_site': 'PRIMARY SITE\n\nPrimary site of the tumor (organ of origin).',
    
    'primary_site_group': 'PRIMARY SITE GROUP\n\nGrouped classification of primary site.\nExamples: "stomach", "small bowel", "gastric"',
    
    'sample_type': 'SAMPLE TYPE\n\nType of biological sample collected.\nExamples: "primary", "metastasis", "local recurrence"',
    
    'age_at_diagnosis': 'AGE AT DIAGNOSIS\n\nAge of the patient (in years) at the time of diagnosis.',
    
    'tumor_size': 'TUMOR SIZE\n\nDimensions of the tumor measured in centimeters.'
}

print("="*80)
print(" " * 15 + "🎨 CREATING INTERACTIVE GRAPH FOR GITHUB PAGES")
print("="*80)

# Ler arquivo DOT
print("\n[1/5] 📖 Reading graph_gpt.dot...")
graphs = pydot.graph_from_dot_file('graph_gpt.dot')
dot_graph = graphs[0]

# Extrair estrutura
nodes_list = []
edges_list = []

for node in dot_graph.get_nodes():
    node_name = node.get_name().strip('"')
    if node_name and node_name not in ['node', 'edge', 'graph']:
        nodes_list.append(node_name)

for edge in dot_graph.get_edges():
    source = edge.get_source().strip('"')
    target = edge.get_destination().strip('"')
    edges_list.append((source, target))

print(f"      ✓ {len(nodes_list)} nodes")
print(f"      ✓ {len(edges_list)} edges")

# Criar rede PyVis
print("\n[2/5] 🎨 Creating visualization...")
net = Network(
    height='100vh',
    width='100%',
    bgcolor='#ffffff',
    font_color='#000000',
    directed=True,
    notebook=False,
    select_menu=False,
    filter_menu=False,
)

# Configuração otimizada
net.set_options('''
var options = {
  "configure": {
    "enabled": false
  },
  "edges": {
    "color": {
      "color": "#666666",
      "highlight": "#FF4444",
      "hover": "#FF4444",
      "opacity": 0.8
    },
    "arrows": {
      "to": {
        "enabled": true,
        "scaleFactor": 1.0,
        "type": "arrow"
      }
    },
    "smooth": {
      "enabled": true,
      "type": "cubicBezier",
      "forceDirection": "vertical",
      "roundness": 0.4
    },
    "width": 2,
    "selectionWidth": 3
  },
  "nodes": {
    "borderWidth": 2,
    "borderWidthSelected": 4,
    "color": {
      "border": "#2B7CE9",
      "background": "#D2E5FF",
      "highlight": {
        "border": "#2B7CE9",
        "background": "#FFA500"
      },
      "hover": {
        "border": "#2B7CE9",
        "background": "#FFEB3B"
      }
    },
    "font": {
      "size": 14,
      "face": "Arial",
      "color": "#000000",
      "bold": {
        "size": 14
      }
    },
    "shape": "box",
    "margin": {
      "top": 10,
      "bottom": 10,
      "left": 15,
      "right": 15
    },
    "widthConstraint": {
      "minimum": 120,
      "maximum": 200
    }
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "direction": "UD",
      "sortMethod": "directed",
      "shakeTowards": "leaves",
      "levelSeparation": 180,
      "nodeSpacing": 150,
      "treeSpacing": 200,
      "blockShifting": true,
      "edgeMinimization": true,
      "parentCentralization": true
    }
  },
  "physics": {
    "enabled": true,
    "hierarchicalRepulsion": {
      "centralGravity": 0.0,
      "springLength": 200,
      "springConstant": 0.01,
      "nodeDistance": 180,
      "damping": 0.09,
      "avoidOverlap": 1
    },
    "solver": "hierarchicalRepulsion",
    "stabilization": {
      "enabled": true,
      "iterations": 1000,
      "updateInterval": 50
    }
  },
  "interaction": {
    "dragNodes": true,
    "dragView": true,
    "hideEdgesOnDrag": false,
    "hideNodesOnDrag": false,
    "hover": true,
    "hoverConnectedEdges": true,
    "keyboard": {
      "enabled": true,
      "speed": {
        "x": 10,
        "y": 10,
        "zoom": 0.02
      },
      "bindToWindow": true
    },
    "multiselect": true,
    "navigationButtons": true,
    "selectable": true,
    "selectConnectedEdges": true,
    "tooltipDelay": 100,
    "zoomView": true,
    "zoomSpeed": 0.5
  }
}
''')

# Adicionar nós
print("\n[3/5] 📦 Adding nodes...")
for i, node_name in enumerate(nodes_list, 1):
    description = node_descriptions.get(node_name, node_name.upper() + '\n\nNo description available.')
    
    net.add_node(
        node_name,
        label=node_name,
        title=description,
        color='#D2E5FF',
        size=30,
        font={'size': 12, 'face': 'Arial', 'bold': True}
    )
    if i % 5 == 0:
        print(f"      ✓ {i}/{len(nodes_list)} nodes added...")

# Adicionar arestas
print("\n[4/5] 🔗 Adding edges...")
for i, (source, target) in enumerate(edges_list, 1):
    net.add_edge(source, target, width=2)
    if i % 10 == 0:
        print(f"      ✓ {i}/{len(edges_list)} edges added...")

# Salvar como index.html (padrão GitHub Pages)
output_file = 'index.html'
print(f"\n[5/5] 💾 Generating {output_file}...")
net.save_graph(output_file)

# Personalizar HTML para GitHub Pages
with open(output_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Adicionar header customizado
custom_header = '''
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        .custom-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .custom-header h1 {
            margin: 0 0 10px 0;
            font-size: 32px;
            font-weight: 700;
        }
        .custom-header p {
            margin: 5px 0 0 0;
            font-size: 15px;
            opacity: 0.95;
        }
        .instructions {
            background: #f8f9fa;
            padding: 15px;
            border-bottom: 3px solid #764ba2;
        }
        .instructions-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .instruction-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
        }
        .instruction-icon {
            font-size: 24px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: rgba(255,255,255,0.95);
            padding: 10px;
            text-align: center;
            font-size: 12px;
            color: #666;
            border-top: 1px solid #ddd;
        }
        .footer a {
            color: #667eea;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="custom-header">
        <h1>📊 Interactive Clinical Relations Graph</h1>
        <p>Analysis of Prognostic Factors in Oncology - GIST (Gastrointestinal Stromal Tumors)</p>
    </div>
    <div class="instructions">
        <div class="instructions-grid">
            <div class="instruction-item">
                <span class="instruction-icon">🖱️</span>
                <span><b>Hover:</b> Mouse over nodes for descriptions</span>
            </div>
            <div class="instruction-item">
                <span class="instruction-icon">👆</span>
                <span><b>Click:</b> Select nodes and edges</span>
            </div>
            <div class="instruction-item">
                <span class="instruction-icon">🔍</span>
                <span><b>Zoom:</b> Mouse scroll or navigation buttons</span>
            </div>
            <div class="instruction-item">
                <span class="instruction-icon">✋</span>
                <span><b>Pan:</b> Drag the background</span>
            </div>
            <div class="instruction-item">
                <span class="instruction-icon">🎯</span>
                <span><b>Move:</b> Drag any node to reorganize</span>
            </div>
            <div class="instruction-item">
                <span class="instruction-icon">⌨️</span>
                <span><b>Keyboard:</b> Arrow keys to navigate</span>
            </div>
        </div>
    </div>
'''

footer = '''
    <div class="footer">
        Created with PyVis & NetworkX | Data visualization for clinical research
    </div>
'''

html = html.replace('<body>', f'<body>{custom_header}')
html = html.replace('</body>', f'{footer}</body>')

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("      ✓ HTML customized for GitHub Pages!")

print("\n" + "="*80)
print(" " * 30 + "✅ DONE!")
print("="*80)
print(f"\n📄 File created: {output_file}")
print("\n🌐 GITHUB PAGES SETUP:")
print("   1. Push this file to your GitHub repository")
print("   2. Go to Settings → Pages")
print("   3. Select 'main' branch and '/ (root)' folder")
print("   4. Save and wait a few minutes")
print("   5. Access: https://YOUR-USERNAME.github.io/REPO-NAME/")
print("\n💡 The file 'index.html' will be automatically served by GitHub Pages")
print("="*80)

# Abrir no navegador
import webbrowser
import os
webbrowser.open('file://' + os.path.abspath(output_file))
print(f"\n🌐 Opening {output_file} in browser...\n")
