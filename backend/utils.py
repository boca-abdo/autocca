def get_upload_path(instance, filename):
    return 'profile_pics/{0}/{1}'.format(instance, filename)

def get_upload_make_logo(instance, filename):
    return 'make_logo/{0}'.format(filename)

def get_upload_cvhu_logo(instance, filename):
    return 'cvhu_logo/{0}'.format(filename)



VGENRE = (
    ('', ''),
    ('VP', 'VP'),
    ('VU', 'VU'),
    ('MOTO', 'MOTO'),
)

VCOLOR = (
    ('',''),
    ('noir','Noir'),
    ('blanc','Blanc'),
)