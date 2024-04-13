import json
from formuls import *

pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)



with open('parallelepipeds.json', 'r') as file:
    f = json.load(file)


num_figures = len(f)
print(f"Total number of figures {num_figures}")


with open('parallelepipeds.json') as f:
  parallelepipeds = json.load(f)


def str_round(a:str)->str:
  round_ = round(float(a),3)
  return str(round_)


def convert_dict(sample:dict)->dict:
  a, b, c = sample.values()
  diag_ = str_round(diag(a, b, c))
  converted_dict = {
      "diag": diag_,
      "volume": str_round(volume(a, b, c)),
      "surface_area": str_round(surface_area(a, b, c)),
      "alpha": str_round(alpha(a, diag_)),
      "beta": str_round(beta(b, diag_)),
      "gamma": str_round(gamma(c, diag_)),
      "radius_described_sphere": str_round(radius_described_sphere(diag_)),
      "volume_described_sphere": str_round(volume_described_sphere(diag_))
      }
  return converted_dict

characteristics = {k: convert_dict(v) for k, v in parallelepipeds.items()}


with open('characteristics.json', 'w') as f:
  json.dump(characteristics, f, indent=4)



avg_diag = []
avg_volume = []
avg_surface_area = []
avg_alpha = []
avg_beta = []
avg_gamma = []
avg_radius_described_sphere = []
avg_volume_described_sphere = []

def stat_dict(sample:dict)->None:
  a, b, c = sample.values()
  diag_ = float(diag(a, b, c))
  avg_diag.append(diag_)
  avg_volume.append(float(volume(a, b, c)))
  avg_surface_area.append(float(surface_area(a, b, c)))
  avg_alpha.append(float(alpha(a, diag_)))
  avg_beta.append(float(beta(b, diag_)))
  avg_gamma.append(float(gamma(c, diag_)))
  avg_radius_described_sphere.append(float(radius_described_sphere(diag_)))
  avg_volume_described_sphere.append(float(volume_described_sphere(diag_)))

for fig in parallelepipeds.values():
  stat_dict(fig)




def mean(list_:list)->float:
  return round(sum(list_)/len(list_), 3)



statistics = {
                      "avg_diag": str(mean(avg_diag)),
                      "avg_volume": str(mean(avg_volume)),
                      "avg_surface_area": str(mean(avg_surface_area)),
                      "avg_alpha": str(mean(avg_alpha)),
                      "avg_beta": str(mean(avg_beta)),
                      "avg_gamma": str(mean(avg_gamma)),
                      "avg_radius_described_sphere": str(mean(avg_radius_described_sphere)),
                      "avg_volume_described_sphere": str(mean(avg_volume_described_sphere)),
              }


with open('statistics.json', 'w') as f:
  json.dump(statistics, f, indent=4)

print(f"""
Среднее всех главных диагоналей: {statistics['avg_diag']}
Средний объем параллелограммов: {statistics['avg_volume']}
Средняя площадь поверхностей параллелограмов: {statistics['avg_surface_area']}
Средний угол между диагональю и стороной a: {statistics['avg_alpha']}
Средний угол между диагональю и стороной b: {statistics['avg_beta']}
Средний угол между диагональю и стороной c: {statistics['avg_gamma']}
Средний радиус описаной сферы: {statistics['avg_radius_described_sphere']}
Средний объем описаной сферы: {statistics['avg_volume_described_sphere']}
      """)