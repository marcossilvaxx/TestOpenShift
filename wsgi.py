import os

from app import app as application, run

if __name__ == '__main__':

    ip = os.environ.get('OPENSHIFT_PYTHON_IP', '0.0.0.0')
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8051))

    # Para detalhar melhor os Logs no OpenShift
    application.config['PROPAGATE_EXCEPTIONS'] = True

    run(ip, port)
