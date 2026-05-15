from flask import Blueprint, render_template

Confirm = Blueprint('confimar-pamento', __name__)

@Confirm.route('/confimar-pagamento/', methods=['POST'])
def ConfirmPagamento():
    return render_template('confirm_pay.html')

