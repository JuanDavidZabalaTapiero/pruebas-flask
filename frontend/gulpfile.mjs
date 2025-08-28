import gulp from "gulp";
import * as dartSass from "sass";
import gulpSass from "gulp-sass";
import cleanCSS from "gulp-clean-css";
import rename from "gulp-rename";
import { deleteSync } from "del";

const sass = gulpSass(dartSass);

const paths = {
    scssPages: "./scss/pages/**/*.scss",
    scssBootstrap: "./scss/bootstrap.scss",
    cssDest: "../app/static/css",
    jsDest: "../app/static/js",
    nodeModules: "../node_modules"
};

// LIMPIAR
function clean() {
    return deleteSync([paths.cssDest + "/*", paths.jsDest + "/*"]);
}

// COMPILAR PÁGINAS (un CSS por vista)
function stylesPages() {
    return gulp
        .src(paths.scssPages)
        .pipe(sass().on("error", sass.logError))
        .pipe(cleanCSS())
        .pipe(rename({ suffix: ".min" }))
        .pipe(gulp.dest(paths.cssDest));
}

// COMPILAR BOOTSTRAP (un solo archivo global)
function stylesBootstrap() {
    return gulp
        .src(paths.scssBootstrap)
        .pipe(sass().on("error", sass.logError))
        .pipe(cleanCSS())
        .pipe(rename("bootstrap.min.css"))
        .pipe(gulp.dest(paths.cssDest));
}

// JS DE BOOTSTRAP
function scriptsBootstrap() {
    return gulp
        .src("../node_modules/bootstrap/dist/js/bootstrap.bundle.min.js")
        .pipe(rename("bootstrap.bundle.min.js"))
        .pipe(gulp.dest(paths.jsDest));
}

// VIGILAR CAMBIOS
function watchFiles() {
    gulp.watch(paths.scssPages, stylesPages);
    gulp.watch(paths.scssBootstrap, stylesBootstrap);
}

// 🔹 Exportar tareas en formato ESM
export { clean, stylesPages, stylesBootstrap, scriptsBootstrap, watchFiles as watch };

// 🔹 Tareas compuestas
export const styles = gulp.series(stylesBootstrap, stylesPages);
export const scripts = scriptsBootstrap;
export default gulp.series(clean, stylesBootstrap, stylesPages, scriptsBootstrap);