const path = require('path');
module.exports = {
    runtimeCompiler: true,
    outputDir: '../tmp_static/home',
    assetsDir: 'assets',
    filenameHashing: false,
    configureWebpack: {
        devServer: {
            proxy: {
                '/api*': {
                    target: 'http://localhost:8000/',
                }
            }
        },
        resolve: {
            alias: {
                '~': path.resolve(__dirname, 'src3/')
            }
        }
    },
    chainWebpack: (config) => {
        if (process.env.NODE_ENV === 'production') {
            config.plugin('html').tap((opts) => {
                opts[0].filename = './templates/home.html';
                return opts;
            });
        }
        const cssRule = config.module.rule('css');
        cssRule
            .use('sass-loader')
            .loader('sass-loader')
            .tap(options => {
                // modify the options...
                return options
            });
    },
};