from log_reader import read_logs
from threat_detection import detections_threat
from report_generator import report_generate
import utils

def main():
    star = True
    answer = str(input("Iniciar analisis?: "))
    while star:
        if answer == "yes":
            star = False
            report_generate(detections_threat(read_logs(utils.path)))
            print("Comenzando analisis y generando reporte...")

        else:
            print("Finalizando...")
            star = False




if __name__ == "__main__":
    main()