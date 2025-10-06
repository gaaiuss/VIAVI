import flet as ft  # type: ignore

from converter import mergeJsonFiles, openReport, saveToExcel, writeCsv


def main(page: ft.Page):
    def select_json(e: ft.FilePickerResultEvent):
        path_list = []
        if e.files:
            for file in e.files:  # type: ignore
                path_list.append(file.path)
            selected_files.value = (
                "\n".join(map(lambda f: f.name, e.files)
                          ) if e.files else "Cancelled!"
            )
            selected_files.update()
            json_file = mergeJsonFiles(path_list)
            writeCsv(json_file)

    def generate_report(e: ft.FilePickerResultEvent):
        if e.path:
            excel_path = saveToExcel(e.path)
            save_dir.value = f'Report saved in: {excel_path}'
            openReport(excel_path)
        else:
            save_dir.value = "Cancelled!"
        save_dir.update()

    # Page Setup
    page.title = "VIAVI OLP-39 Report Generator"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Text Variables
    main_text = ft.Text("OLP-39 Report Generator", size=25)
    select_btn_text = ft.Text("Select Json Files")
    generate_btn_text = ft.Text('Generate Report')

    # Json
    pick_files_dialog = ft.FilePicker(on_result=select_json)
    page.overlay.append(pick_files_dialog)
    selected_files = ft.Text(text_align=ft.TextAlign.CENTER)

    # Generate Report
    generate_report_dialog = ft.FilePicker(on_result=generate_report)
    page.overlay.append(generate_report_dialog)
    save_dir = ft.Text(text_align=ft.TextAlign.CENTER)

    # Text Container
    text_container = ft.Container(
        content=main_text,
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        height=150,
    )

    # Buttons
    select_btn = ft.CupertinoButton(
        content=select_btn_text,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.DEEP_PURPLE_400,
        on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True),
    )

    generate_btn = ft.CupertinoButton(
        content=generate_btn_text,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.DEEP_PURPLE_400,
        on_click=lambda _: generate_report_dialog.get_directory_path(),
    )

    btn_row = ft.Row(
        [select_btn, generate_btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Logo
    logo_path = 'logo.png'
    logo = ft.Image(
        src=logo_path,
        width=400,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    # Add Page Content
    page.add(logo, text_container, btn_row, selected_files, save_dir)


ft.app(main, assets_dir='assets', upload_dir='src/uploads')
