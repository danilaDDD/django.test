from tours.models import ToursBanner


def handed_banner_params(request):
    """function handed request's params  baner_id and tour_type_id"""

    baner_id = request.GET.get('baner_id', None)
    tour_type_id = request.GET.get('tour_type_id', None)

    if baner_id is None:
        if tour_type_id is not None:
            filtered_baners = ToursBanner.objects.filter(tourtype__id=tour_type_id)

            if len(filtered_baners) > 0:
                baner_id = filtered_baners[0].id

            tour_type_id = int(tour_type_id)
    else:
        baner_id = int(baner_id)

    return baner_id, tour_type_id




