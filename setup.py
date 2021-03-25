from distutils.core import setup


setup(name='juno',
      version='0.0',
      description='A jupyter data viwer.',
      author='tor4z',
      scripts=['scripts/juno.server'],
      author_email='vwenjie@hotmail.com',
      package_data={'juno': ['server/template/*.html',
                             'server/asset/js/*.js',
                             'server/asset/css/*.css']},
      packages=['juno',
                'juno.server',
                'juno.server.http',
                'juno.server.http.handler',
                'juno.server.http.handler.base'],
     )
