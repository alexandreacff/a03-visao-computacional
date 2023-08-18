# Resumo
Realizamos um fine-tunning no modelo pré-treinado YOLO-NAS, que é uma arquitetura de rede neural que apresenta melhores métricas que o YOLOv8 na tarefa de detecção de objetos.
# Dataset
Para realizar o fine-tunning, realizmamos um treinamento sobre um modelo pré-treinado. Para isso criamos um dataset novo, que contêm as bounding-boxes e a classes que representa a imagem (0 para não queda e 1 para queda). Para melhor treinamento, realizamos, também, um data augmentation.

# Modelo
Utilizamos o YOLO-NAS l, que é o de maior quantidade de parâmetros dentre os modelos YOLO-NAS, e que apresenta melhor desempenho.
Importamos o modelo através da biblioteca SuperGradients e o treinamos em cima do nosso dataset. Salvamos, ao longo das épocas, o modelo que está sendo treinado , e escolhemos o que possuir 
melhor performance.

# Referências:
Baseamos nossa implementação no link a seguir. Para mais informações sobre como foi feito o detector de quedas acesse-o:
https://github.com/AarohiSingla/YOLO-NAS

Sobre o YOLO-NAS:
https://deci.ai/blog/yolo-nas-object-detection-foundation-model/

