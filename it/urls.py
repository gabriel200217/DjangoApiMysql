from rest_framework import routers
from .api import dispositivosViewSet, empresasViewSet, departamentosViewSet, usuariosViewSet, ubicacionesViewSet, informacionViewSet, marcasViewSet, modelosViewSet, impresorasViewSet, equiposViewSet

router = routers.DefaultRouter()

# router.register('api/departamentos', departamentosViewSet , 'departamento')
router.register('api/empresas', empresasViewSet , 'empresas')
router.register('api/departamentos', departamentosViewSet , 'departamentos')
router.register('api/usuarios', usuariosViewSet , 'usuarios')
router.register('api/ubicaciones', ubicacionesViewSet , 'ubicaciones')
router.register('api/informacion', informacionViewSet , 'informacion')
router.register('api/marcas', marcasViewSet , 'marcas')
router.register('api/modelos', modelosViewSet , 'modelos')
router.register('api/dispositivos', dispositivosViewSet , 'dispositivos')
router.register('api/Impresoras', impresorasViewSet , 'Impresoras')
router.register('api/equipos', equiposViewSet, 'equipos')

urlpatterns = router.urls