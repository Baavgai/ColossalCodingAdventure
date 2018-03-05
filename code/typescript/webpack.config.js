'use strict';

// var webpack = require('webpack');
var path = require("path");

var d = function (stub) {
  return path.join(__dirname, "build", stub);
};

module.exports = {
  // mode: "development || "production",
  entry: {
    cca: [d('cca-lib'), d('cca-web')],
    roomkey: d('roomKeyWeb.js')
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        cca: {
          chunks: 'initial',
          name: 'cca',
          test: 'cca',
          enforce: true
        },
      }
    }
  },
  output: {
    filename: '[name].js',
    path: d('web'),
  }
}

/*

var webpack = require('webpack');

console.log(__dirname);

var d = function(stub) { return __dirname + '/build/' + stub; };


module.exports = {  
  entry: {
    roomkey:  d('roomkey.js'),
    cca: [ d('cca-lib'), d('cca-web') ]
  },
  plugins: [
    new webpack.LoaderOptionsPlugin({ debug: true }),
    new webpack.optimize.CommonsChunkPlugin({
      name: 'cca'
    })
  ],
  output: {
    filename: '[name].js',
    path: d('web'),
  },
  resolve: {
    extensions: ['.webpack.js', '.web.js', '.ts', '.js']
  },
  performance: { hints: true }
};



var path = require("path");
module.exports = {
	// mode: "development || "production",
	entry: {
		vendor1: ["./vendor1"],
		vendor2: ["./vendor2"],
		pageA: "./pageA",
		pageB: "./pageB",
		pageC: "./pageC"
	},
	output: {
		path: path.join(__dirname, "dist"),
		filename: "[name].js"
	},
	optimization: {
		splitChunks: {
			cacheGroups: {
				vendor1: {
					name: "vendor1",
					test: "vendor1",
					enforce: true
				},
				vendor2: {
					name: "vendor2",
					test: "vendor2",
					enforce: true
				}
			}
		}
	}
};


module.exports = {
	// mode: "development" || "production",
	entry: {
		pageA: "./pageA",
		pageB: "./pageB",
		pageC: "./pageC"
	},
	optimization: {
		splitChunks: {
			cacheGroups: {
				commons: {
					chunks: "initial",
					minChunks: 2,
					maxInitialRequests: 5, // The default limit is too small to showcase the effect
					minSize: 0 // This is example is too small to create commons chunks
				},
				vendor: {
					test: /node_modules/,
					chunks: "initial",
					name: "vendor",
					priority: 10,
					enforce: true
				}
			}
		}
	},
	output: {
		path: path.join(__dirname, "dist"),
		filename: "[name].js"
	}
};

module.exports = {
  entry: {
    cca: [d('cca-lib'), d('cca-web')],
    roomkey: [d('roomKeyWeb.js')]
  },
  output: {
    filename: '[name].js',
    path: d('web'),
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        cca: {
          name: "cca",
          test: "cca",
          enforce: true
        },
        roomkey: {
          name: "roomkey",
          test: "roomkey",
          enforce: true
        },
      }
    }
  },
  resolve: {
    extensions: ['.webpack.js', '.web.js', '.ts', '.js']
  }
};



This is the default configuration:

splitChunks: {
	chunks: "async",
	minSize: 30000,
	minChunks: 1,
	maxAsyncRequests: 5,
	maxInitialRequests: 3,
	name: true,
	cacheGroups: {
		default: {
			minChunks: 2,
			priority: -20
			reuseExistingChunk: true,
		},
		vendors: {
			test: /[\\/]node_modules[\\/]/,
			priority: -10
		}
	}
}

// mode: "development || "production",
entry: {
  vendor: ['babel-polyfill', 'react', 'react-dom', 'redux'],
  client: './client.js',
},
output: {
  path: path.join(__dirname, '../dist'),
  filename: '[name].chunkhash.bundle.js',
  chunkFilename: '[name].chunkhash.bundle.js',
  publicPath: '/',
},
optimization: {
  splitChunks: {
    cacheGroups: {
      vendor: {
        chunks: 'initial',
        name: 'vendor',
        test: 'vendor',
        enforce: true
      },
    }
  },
  runtimeChunk: true
}
*/
