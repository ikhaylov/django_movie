from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, MovieShots, Raiting, Reviews, RaitingStar, Movie, Genre, Actor


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email", "parent")


class MovieShotsInline(admin.StackedInline):
    model = MovieShots
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline, ]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    # fields = ("title", "tagline", "description", "poster",
    #           ("actors", "directors", "genres"),
    #           "year", "country", "world_premiere",
    #           "budget", "fees_in_usa", "fees_in_world", "category", "url", "draft", )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse", ),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Raiting)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "ip")


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Кадры фильма"


admin.site.register(RaitingStar)


admin.site.site_title = "Own Movies"
admin.site.site_header = "My Movies"




