import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700
    page.padding = 0
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary='#192233',
            on_primary='#ffffff',
            background='#0d121c'
        )
    )

    layout = ft.Container (
        expand=True,
        padding=ft.padding.only(top=40, left=20, right=20, bottom=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.PRIMARY, ft.Colors.BLACK38]
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                ft.Text(
                    value='Gerador de Senhas',
                    size=30,
                    width=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=30, thickness=0.5),

                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(5),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                selectable=True,
                                size=20,
                                height=40,
                            ),
                            ft.IconButton(
                                icon=ft.Icons.COPY,
                                icon_color=ft.Colors.WHITE30,
                                selected_icon=ft.Icons.CHECK,
                                selected_icon_color=ft.Colors.INDIGO,
                                selected=False,
                            )
                        ]
                    )
                ),
                ft.Text (
                    value='CARACTERES',
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    border_radius=ft.border_radius.all(5),
                    content=ft.Slider(
                        value=10,
                        min=4,
                        max=20,
                        divisions=10,
                    )
                )
            ]
        )
    )

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)