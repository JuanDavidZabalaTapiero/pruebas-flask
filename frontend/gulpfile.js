const gulp = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const cleanCSS = require("gulp-clean-css");
const rename = require("gulp-rename");

// RUTAS
const paths = {
    scss: "./scss/pages/**/*.scss",
    cssDest: "../app/static/css"
};

// COMPILAR SCSS -> CSS minificado
function styles() {
    return gulp
        .src(paths.scss)
        .pipe(sass().on("error", sass.logError))
        .pipe(cleanCSS())
        .pipe(rename({ suffix: ".min" }))
        .pipe(gulp.dest(paths.cssDest));
}

// VIGILAR CAMBIOS
function watch() {
    gulp.watch(paths.scss, styles);
}

exports.styles = styles;
exports.watch = watch;