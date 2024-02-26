import os

from ultralytics import YOLO
import cv2


for dataset_size in [10, 50, 100, 200, 500, 1000, 2000, 4000]:

    video_path = os.path.join('.', 'ducks.mp4')

    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    H, W, _ = frame.shape

    video_path_out = 'out_{}.mp4'.format(str(dataset_size))
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

    model_path = os.path.join('.', 'results', str(dataset_size), 'weights', 'last.pt')

    # Load a model
    model = YOLO(model_path)  # load a custom model

    threshold = 0.5

    while ret:

        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                # cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                #            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        out.write(frame)
        ret, frame = cap.read()

    out.release()
    cap.release()

cv2.destroyAllWindows()
