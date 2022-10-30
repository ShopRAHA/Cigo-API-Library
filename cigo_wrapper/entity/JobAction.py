import json


# All dates are in ISO-8601 format
class JobAction:
    action_id = None
    id = None
    status = None
    status_counters = None
    type = None
    description = None
    value = None
    unit_weight = None
    total_weight = None
    unit_volume = None
    total_volume = None
    piece_count = None
    piece_count_unit = None
    quantity = None
    quantity_unit = None
    handle_time = None
    stop_location_id = None
    invoice_number = None
    external_reference_id = None
    shipping_barcode = None
    create_datetime = None

    def __init__(self, ref_id, action_type, description):
        self.id = ref_id
        self.type = action_type
        self.description = description

    def to_json(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    @classmethod
    def from_json(cls, action_response):
        response_dic = action_response
        action = cls(
            ref_id=response_dic['id'],
            description=response_dic['description'],
            action_type=response_dic['type'],
        )

        for key in response_dic.keys():
            if key == 'action_id' and response_dic[key] is not None:
                action.action_id = response_dic[key]
            elif key == 'status' and response_dic[key] is not None:
                action.status = response_dic[key]
            elif key == 'status_counters' and response_dic[key] is not None:
                action.status_counters = response_dic[key]
            elif key == 'value' and response_dic[key] is not None:
                action.value = response_dic[key]
            elif key == 'unit_weight' and response_dic[key] is not None:
                action.unit_weight = response_dic[key]
            elif key == 'total_weight' and response_dic[key] is not None:
                action.total_weight = response_dic[key]
            elif key == 'unit_volume' and response_dic[key] is not None:
                action.unit_volume = response_dic[key]
            elif key == 'total_volume' and response_dic[key] is not None:
                action.total_volume = response_dic[key]
            elif key == 'piece_count' and response_dic[key] is not None:
                action.piece_count = response_dic[key]
            elif key == 'piece_count_unit' and response_dic[key] is not None:
                action.piece_count_unit = response_dic[key]
            elif key == 'quantity' and response_dic[key] is not None:
                action.quantity = response_dic[key]
            elif key == 'quantity_unit' and response_dic[key] is not None:
                action.quantity_unit = response_dic[key]
            elif key == 'handle_time' and response_dic[key] is not None:
                action.handle_time = response_dic[key]
            elif key == 'stop_location_id' and response_dic[key] is not None:
                action.stop_location_id = response_dic[key]
            elif key == 'invoice_number' and response_dic[key] is not None:
                action.invoice_number = response_dic[key]
            elif key == 'external_reference_id' and response_dic[key] is not None:
                action.external_reference_id = response_dic[key]
            elif key == 'shipping_barcode' and response_dic[key] is not None:
                action.shipping_barcode = response_dic[key]
            elif key == 'create_datetime' and response_dic[key] is not None:
                action.create_datetime = response_dic[key]

        return action
