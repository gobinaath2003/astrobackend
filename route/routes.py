from flask import Blueprint
from controller.authcontroller import register_user, login_user
from controller.rasicontroller import get_rasi,add_rasi,get_single_rasi,update_rasi,delete_rasi
from controller.lagnamcontroller import  get_lagnam,add_lagnam,update_lagnam,delete_lagnam
from controller.pariharamcontroller import get_pariharam,add_pariharam,get_single_pariharam,update_pariharam,delete_pariharam
from controller.bhanavmmodel import get_bhavam,add_bhavam,get_single_bhavam,update_bhavam,delete_bhavam
from controller.mantrigamcontroller import get_mantrigam,get_single_mantrigam,update_mantrigam,delete_mantrigam,add_mantrigam
from controller.tantrigamcontroller import get_tantrigam,add_tantrigam,get_single_tantrigam,update_tantrigam,delete_tantrigam
from controller.twocombinationcontroller import get_twocombination,add_twocombination,get_single_twocombination,update_twocombination,delete_twocombination
from controller.threecombinationcontroller import get_threecombination,add_threecombination,get_single_threecombination,update_threecombination,delete_threecombination
auth_bp = Blueprint("auth", __name__)

auth_bp.route("/register", methods=["POST"])(register_user)
auth_bp.route("/login", methods=["POST"])(login_user)

auth_bp.route("/rasi", methods=["POST"])(add_rasi)
auth_bp.route("/getrasi", methods=["GET"])(get_rasi)
auth_bp.route("/updaterasi/<int:id>", methods=["PUT"])(update_rasi)
auth_bp.route("/deleterasi/<int:id>", methods=["DELETE"])(delete_rasi)
auth_bp.route("/lagnam", methods=["POST"])(add_lagnam)

auth_bp.route("/getlagnam", methods=["GET"])(get_lagnam)

auth_bp.route("/updatelagnam/<int:id>", methods=["PUT"])(update_lagnam)

auth_bp.route("/deletelagnam/<int:id>", methods=["DELETE"])(delete_lagnam)

auth_bp.route("/bhavam", methods=["POST"])(add_bhavam)

auth_bp.route("/bhavam", methods=["GET"])(get_bhavam)

auth_bp.route("/bhavam/<int:id>", methods=["GET"])(get_single_bhavam)

auth_bp.route("/bhavam/<int:id>", methods=["PUT"])(update_bhavam)

auth_bp.route("/bhavam/<int:id>", methods=["DELETE"])(delete_bhavam)

auth_bp.route("/pariharam", methods=["POST"])(add_pariharam)

auth_bp.route("/pariharam", methods=["GET"])(get_pariharam)

auth_bp.route("/pariharam/<int:id>", methods=["GET"])(get_single_pariharam)

auth_bp.route("/pariharam/<int:id>", methods=["PUT"])(update_pariharam)

auth_bp.route("/pariharam/<int:id>", methods=["DELETE"])(delete_pariharam)

auth_bp.route("/mantrigam", methods=["POST"])(add_mantrigam)

auth_bp.route("/mantrigam", methods=["GET"])(get_mantrigam)

auth_bp.route("/mantrigam/<int:id>", methods=["GET"])(get_single_mantrigam)

auth_bp.route("/mantrigam/<int:id>", methods=["PUT"])(update_mantrigam)

auth_bp.route("/mantrigam/<int:id>", methods=["DELETE"])(delete_mantrigam)


auth_bp.route("/tantrigam", methods=["POST"])(add_tantrigam)

auth_bp.route("/tantrigam", methods=["GET"])(get_tantrigam)

auth_bp.route("/tantrigam/<int:id>", methods=["GET"])(get_single_tantrigam)

auth_bp.route("/tantrigam/<int:id>", methods=["PUT"])(update_tantrigam)

auth_bp.route("/tantrigam/<int:id>", methods=["DELETE"])(delete_tantrigam)

auth_bp.route("/twocombination", methods=["POST"])(add_twocombination)

auth_bp.route("/twocombination", methods=["GET"])(get_twocombination)

auth_bp.route("/twocombination/<int:id>", methods=["GET"])(get_single_twocombination)

auth_bp.route("/twocombination/<int:id>", methods=["PUT"])(update_twocombination)

auth_bp.route("/twocombination/<int:id>", methods=["DELETE"])(delete_twocombination)


auth_bp.route("/threecombination", methods=["POST"])(add_threecombination)

auth_bp.route("/threecombination", methods=["GET"])(get_threecombination)

auth_bp.route("/threecombination/<int:id>", methods=["GET"])(get_single_threecombination)

auth_bp.route("/threecombination/<int:id>", methods=["PUT"])(update_threecombination)

auth_bp.route("/threecombination/<int:id>", methods=["DELETE"])(delete_threecombination)