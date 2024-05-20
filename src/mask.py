from src.config_log import setting_log

logger = setting_log(__name__)


def security_card(num: str) -> str:
    """маскирует номер карты"""
    if num.isdigit() and len(num) == 16:
        logger.info("masking...")
        list_num: list = []
        list_num.extend(num)
        list_num[4], list_num[8], list_num[12] = " " + list_num[4], " " + list_num[8], " " + list_num[12]
        num = "".join(list_num)
        list_num = num.split()
        list_num[1] = list_num[1][:2] + "**"
        list_num[2] = "****"
        mask_card = " ".join(list_num)
        logger.info(f"making card {mask_card}")
        return mask_card
    logger.info("не правильно введены данные")
    return "не правильно введены данные"


def security_num(num: str) -> str:
    """маскирует номер счета"""
    if num.isdigit() and len(num) == 20:
        logger.info("masking...")
        mask_num = "**" + num[-4:]
        logger.info(f"mask num {mask_num}")
        return mask_num
    logger.info("не правильно введены данные")
    return "не правильно введены данные"
